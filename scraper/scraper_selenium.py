import os
import time
import json
import logging
import xlsxwriter
from dotenv import load_dotenv

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException
from webdriver_manager.chrome import ChromeDriverManager

class DevCampCourseScraper:
    def __init__(self, headless=False):
        """
        Initialize the web scraper with Chrome WebDriver
        
        :param headless: Run browser in headless mode
        """
        # Configure logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)

        # Set up Chrome options
        chrome_options = Options()
        if headless:
            chrome_options.add_argument("--headless")
        
        # Additional Chrome options for stability
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")
        
        # Initialize WebDriver
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        
        # Course-specific URLs
        self.base_url = "https://basque.devcamp.com"
        self.login_url = f"{self.base_url}/users/sign_in"
        self.course_url = f"{self.base_url}/pt-full-stack-development-javascript-python-react"
        
        # Store scraped videos data
        self.videos_data = []

    def login(self, email, password):
        """
        Log in to the DevCamp platform
        
        :param email: User email address
        :param password: User password
        :return: Boolean indicating login success
        """
        try:
            # Navigate to login page
            self.logger.info("Navigating to login page")
            self.driver.get(self.login_url)
            
            # Wait for and interact with login form
            email_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "user_email"))
            )
            email_input.send_keys(email)
            
            # Find and fill password field
            password_input = self.driver.find_element(By.ID, "user_password")
            password_input.send_keys(password)
            
            # Submit login form
            login_button = self.driver.find_element(By.NAME, "commit")
            login_button.click()
            
            # Wait for successful login
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "navbar-content"))
            )
            
            self.logger.info("Login successful")
            return True
        
        except Exception as e:
            self.logger.error(f"Login failed: {e}")
            # Save screenshot for debugging
            self.driver.save_screenshot("login_error.png")
            return False

    def extract_course_content(self):
        """
        Extract course content and video details
        
        :return: List of video course details
        """
        try:
            # Navigate to course page
            self.logger.info("Navigating to course page")
            self.driver.get(self.course_url)
            
            # Wait for syllabus to load completely
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "syllabus-content"))
            )
            
            # Aggressive page interaction to trigger content loading
            self.interact_with_page()
            
            # Wait a bit for any dynamic content to load
            time.sleep(3)
            
            # Save the page source for debugging
            with open("course_page_source.html", "w", encoding="utf-8") as f:
                f.write(self.driver.page_source)
            
            # Find all module headers using multiple strategies
            modules = self.find_modules()
            
            self.logger.info(f"Found {len(modules)} modules")
            
            for module_index, module in enumerate(modules, 1):
                try:
                    # Get module title
                    try:
                        module_title = module.find_element(By.CLASS_NAME, "title").text.strip()
                    except:
                        module_title = f"Module {module_index}"
                    
                    self.logger.info(f"Processing {module_title}")
                    
                    # Find chapters container through multiple methods
                    chapters_container = self.find_chapters_container(module)
                    
                    if not chapters_container:
                        self.logger.warning(f"No chapters container found for {module_title}")
                        continue
                    
                    # Find all chapter items
                    items = self.find_chapter_items(chapters_container)
                    
                    self.logger.info(f"Found {len(items)} items in {module_title}")
                    
                    # Process each item
                    for item_index, item in enumerate(items, 1):
                        try:
                            # Extract item details
                            chapter_details = self.extract_item_details(item)
                            
                            # Skip if no title
                            if not chapter_details['title']:
                                continue
                            
                            # Try to extract duration
                            duration = self.extract_item_duration(chapter_details['link'])
                            
                            # Store video data
                            self.videos_data.append({
                                'module': module_title,
                                'chapter': chapter_details['title'],
                                'duration': duration,
                                'completed': chapter_details['completed']
                            })
                        
                        except Exception as item_error:
                            self.logger.error(
                                f"Error processing item {item_index} in {module_title}: {item_error}"
                            )
                
                except Exception as module_error:
                    self.logger.error(f"Error processing module: {module_error}")
            
            return self.videos_data
        
        except Exception as e:
            self.logger.error(f"Course content extraction failed: {e}")
            # Save screenshot for debugging
            self.driver.save_screenshot("course_extraction_error.png")
            return []

    def interact_with_page(self):
        """
        Interact with the page to trigger dynamic content loading
        """
        try:
            # Scroll techniques to trigger lazy loading
            self.driver.execute_script("""
                window.scrollTo(0, document.body.scrollHeight);
                var totalHeight = document.body.scrollHeight;
                var distance = 200;
                var currentHeight = 0;
                
                while(currentHeight < totalHeight){
                    window.scrollBy(0, distance);
                    currentHeight += distance;
                    window.scrollTo(0, currentHeight);
                }
            """)
            
            # Try to interact with possible dropdown or expand buttons
            try:
                expand_buttons = self.driver.find_elements(
                    By.XPATH, 
                    "//button[contains(text(), 'Expand') or contains(text(), 'Show More')]"
                )
                for button in expand_buttons:
                    try:
                        button.click()
                        time.sleep(0.5)
                    except:
                        pass
            except:
                pass
            
            time.sleep(2)
        except Exception as e:
            self.logger.warning(f"Error interacting with page: {e}")

    def find_modules(self):
        """
        Find modules using multiple strategies
        
        :return: List of module elements
        """
        strategies = [
            lambda: self.driver.find_elements(
                By.XPATH, 
                "//div[contains(@class, 'syllabus-section-header')]"
            ),
            lambda: self.driver.find_elements(
                By.XPATH, 
                "//div[contains(@class, 'module') or contains(@class, 'section')]"
            ),
            lambda: self.driver.execute_script("""
                return Array.from(document.querySelectorAll('.syllabus-section-header, .module, .section'));
            """)
        ]
        
        for strategy in strategies:
            try:
                modules = strategy()
                if modules:
                    return modules
            except Exception as e:
                self.logger.debug(f"Module finding strategy failed: {e}")
        
        return []

    def find_chapters_container(self, module):
        """
        Find chapters container using multiple strategies
        
        :param module: Module element
        :return: Chapters container element or None
        """
        strategies = [
            # Direct sibling with syllabus-section-content class
            lambda: module.find_element(
                By.XPATH, 
                "./following-sibling::div[contains(@class, 'syllabus-section-content')]"
            ),
            # Use JavaScript to find next sibling
            lambda: self.driver.execute_script("""
                const moduleHeader = arguments[0];
                const nextSibling = moduleHeader.nextElementSibling;
                return nextSibling && nextSibling.classList.contains('syllabus-section-content') ? nextSibling : null;
            """, module),
            # Try finding by index
            lambda: self.driver.find_elements(
                By.XPATH, 
                "//div[contains(@class, 'syllabus-section-content')]"
            )[module.get_attribute('data-index')]
        ]
        
        for strategy in strategies:
            try:
                container = strategy()
                if container:
                    return container
            except Exception as e:
                self.logger.debug(f"Chapters container strategy failed: {e}")
        
        return None

    def find_chapter_items(self, chapters_container):
        """
        Find chapter items using multiple strategies
        
        :param chapters_container: Chapters container element
        :return: List of chapter items
        """
        strategies = [
            # Direct .item-row class
            lambda: chapters_container.find_elements(
                By.CLASS_NAME, 'item-row'
            ),
            # XPath for various item classes
            lambda: chapters_container.find_elements(
                By.XPATH, 
                ".//*[contains(@class, 'item') or contains(@class, 'row') or contains(@class, 'lesson')]"
            ),
            # JavaScript to find items
            lambda: self.driver.execute_script("""
                const container = arguments[0];
                return Array.from(container.querySelectorAll('.item-row, .item, .row, .lesson'));
            """, chapters_container)
        ]
        
        for strategy in strategies:
            try:
                items = strategy()
                if items:
                    return items
            except Exception as e:
                self.logger.debug(f"Chapter items strategy failed: {e}")
        
        return []

    def extract_item_details(self, item):
        """
        Extract details of a single item
        
        :param item: Item element
        :return: Dictionary of item details
        """
        # Multiple strategies to extract title
        title_strategies = [
            lambda: item.find_element(By.CLASS_NAME, 'title').text.strip(),
            lambda: item.find_element(By.XPATH, ".//*[contains(@class, 'title')]").text.strip(),
            lambda: self.driver.execute_script("""
                const item = arguments[0];
                const titleElem = item.querySelector('.title, [class*="title"]');
                return titleElem ? titleElem.textContent.trim() : '';
            """, item)
        ]
        
        title = 'Unknown'
        for strategy in title_strategies:
            try:
                title = strategy()
                if title and title != 'Unknown':
                    break
            except:
                pass
        
        # Check if completed
        completed = 'icon-done-container' in item.get_attribute('innerHTML')
        
        # Find link
        try:
            link = item.find_element(By.TAG_NAME, 'a').get_attribute('href')
        except:
            link = None
        
        return {
            'title': title,
            'completed': completed,
            'link': link
        }

    def extract_item_duration(self, link):
        """
        Extract duration from an item's link
        
        :param link: URL of the item
        :return: Duration string
        """
        if not link or '/guide/' not in link:
            return "N/A"
        
        try:
            # Open link in a new tab
            self.driver.execute_script(f"window.open('{link}', '_blank');")
            
            # Switch to the new tab
            self.driver.switch_to.window(self.driver.window_handles[-1])
            
            # Wait for page to load
            time.sleep(2)
            
            # Try to find duration
            try:
                duration_elem = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located(
                        (By.CLASS_NAME, "vjs-duration-display")
                    )
                )
                duration = duration_elem.text.strip()
            except (TimeoutException, NoSuchElementException):
                duration = "N/A"
            
            # Close the tab
            self.driver.close()
            
            # Switch back to main tab
            self.driver.switch_to.window(self.driver.window_handles[0])
            
            return duration
        
        except Exception as e:
            self.logger.warning(f"Error extracting duration: {e}")
            return "N/A"

    def save_to_json(self, filename='course_videos.json'):
        """
        Save scraped video data to JSON file
        
        :param filename: Output JSON filename
        :return: Boolean indicating save success
        """
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(self.videos_data, file, indent=2, ensure_ascii=False)
            
            self.logger.info(f"Course data saved to {filename}")
            return True
        
        except Exception as e:
            self.logger.error(f"Error saving JSON: {e}")
            return False

    def save_to_excel(self, filename='course_videos.xlsx'):
        """
        Save scraped video data to Excel file
        
        :param filename: Output Excel filename
        :return: Boolean indicating save success
        """
        try:
            # Create Excel workbook
            workbook = xlsxwriter.Workbook(filename)
            worksheet = workbook.add_worksheet('Course Videos')

            # Add bold format for headers
            bold = workbook.add_format({'bold': True})

            # Write headers
            headers = ['Module', 'Chapter', 'Duration', 'Completed']
            for col, header in enumerate(headers):
                worksheet.write(0, col, header, bold)

            # Write data rows
            for row, video in enumerate(self.videos_data, start=1):
                worksheet.write(row, 0, video['module'])
                worksheet.write(row, 1, video['chapter'])
                worksheet.write(row, 2, video['duration'])
                worksheet.write(row, 3, '✓' if video['completed'] else '')

            # Close the workbook
            workbook.close()
            
            self.logger.info(f"Course data saved to {filename}")
            return True
        
        except Exception as e:
            self.logger.error(f"Error saving Excel: {e}")
            return False

    def print_summary(self):
        """
        Print formatted summary of scraped videos
        """
        if not self.videos_data:
            print("No video data available")
            return

        current_module = None
        for video in self.videos_data:
            if current_module != video['module']:
                current_module = video['module']
                print(f"\n{current_module}")
                print("=" * len(current_module))
            
            status = "✓" if video['completed'] else " "
            print(f"{status} {video['chapter']} - Duration: {video['duration']}")

    def close(self):
        """
        Close the browser
        """
        try:
            self.driver.quit()
            self.logger.info("Browser closed successfully")
        except Exception as e:
            self.logger.error(f"Error closing browser: {e}")

def main():
    """
    Main function to run the DevCamp Course Scraper
    """
    # Load environment variables
    load_dotenv()
    
    # Get credentials
    email = os.getenv('DEVCAMP_EMAIL')
    password = os.getenv('DEVCAMP_PASSWORD')
    
    if not email or not password:
        print("Please set DEVCAMP_EMAIL and DEVCAMP_PASSWORD in .env file")
        return
    
    # Create scraper instance
    scraper = DevCampCourseScraper(headless=False)
    
    try:
        # Login
        if not scraper.login(email, password):
            print("Login failed!")
            return
        
        # Extract course content
        scraper.extract_course_content()
        
        # Print summary
        scraper.print_summary()
        
        # Save to JSON and Excel
        scraper.save_to_json()
        scraper.save_to_excel()
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        # Always close the browser
        scraper.close()

if __name__ == "__main__":
    main()
