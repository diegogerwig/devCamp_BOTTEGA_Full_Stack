import requests
from bs4 import BeautifulSoup
import json
import os
import re
from dotenv import load_dotenv
import logging
import time
import xlsxwriter

class CourseVideoScraper:
    def __init__(self):
        # Configure logging
        logging.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)
        
        # Initialize attributes
        self.base_url = "https://devcamp.com"
        self.basque_url = "https://basque.devcamp.com"
        self.login_url = f"{self.base_url}/users/sign_in"
        self.course_url = f"{self.basque_url}/pt-full-stack-development-javascript-python-react"
        self.session = requests.Session()
        self.videos_data = []
        
        # Configure session headers
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5'
        })

    def login(self, email, password):
        """Login to the platform"""
        try:
            # Get CSRF token
            self.logger.info("Getting CSRF token...")
            response = self.session.get(self.login_url)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            csrf_token = soup.find('meta', {'name': 'csrf-token'})
            if not csrf_token:
                self.logger.error("Could not find CSRF token")
                return False
                
            csrf_token = csrf_token['content']
            self.logger.debug(f"CSRF token found: {csrf_token[:10]}...")

            # Login data
            login_data = {
                'utf8': '✓',
                'authenticity_token': csrf_token,
                'user[email]': email,
                'user[password]': password,
                'user[remember_me]': '1',
                'commit': 'Log in'
            }

            # Set up headers
            headers = {
                'X-CSRF-Token': csrf_token,
                'Content-Type': 'application/x-www-form-urlencoded',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
            }

            # Perform login
            self.logger.info("Attempting login...")
            response = self.session.post(
                self.login_url,
                data=login_data,
                headers=headers,
                allow_redirects=True
            )

            # Verify login by checking a protected page
            verify_response = self.session.get(self.course_url)
            if 'sign_in' in verify_response.url.lower():
                self.logger.error("Login failed - redirected to sign in")
                return False

            # Double check by looking for authenticated content
            verify_soup = BeautifulSoup(verify_response.text, 'html.parser')
            if not verify_soup.find('a', {'rel': 'nofollow', 'data-method': 'DELETE', 'href': '/users/sign_out'}):
                self.logger.error("Login failed - no logout button found")
                return False

            self.logger.info("Login successful!")
            return True

        except Exception as e:
            self.logger.error(f"Login error: {str(e)}")
            return False

    def extract_duration(self, page_text):
        """Extract video duration from page text"""
        duration_patterns = [
            r'duration["\']?\s*[:=]\s*["\']?(\d+:\d+|\d+\.\d+)["\']?',
            r'(\d+:\d+)',
            r'duration\s*[:=]\s*(\d+)',
            r'length\s*[:=]\s*(\d+:\d+)',
            r'\b(\d+:\d+)\s*(?:total|video|length)\b'
        ]
        
        try:
            # Convert to lowercase for case-insensitive matching
            lower_text = page_text.lower()
            
            for pattern in duration_patterns:
                match = re.search(pattern, lower_text, re.IGNORECASE)
                if match:
                    duration = match.group(1)
                    
                    # Handle MM:SS or seconds
                    if ':' in duration:
                        minutes, seconds = map(int, duration.split(':'))
                        return f"{minutes:02d}:{seconds:02d}"
                    else:
                        total_seconds = int(float(duration))
                        minutes = total_seconds // 60
                        seconds = total_seconds % 60
                        return f"{minutes:02d}:{seconds:02d}"
            
            # Log failure to find duration
            self.logger.warning("No duration pattern matched")
            return "N/A"
        
        except Exception as e:
            self.logger.error(f"Duration extraction error: {e}")
            return "N/A"

    def extract_course_content(self):
        """Extract course structure and video durations"""
        try:
            # Get initial course page
            response = self.session.get(self.course_url)
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find syllabus content
            syllabus_content = soup.find('div', class_='syllabus-content')
            if not syllabus_content:
                self.logger.error("Could not find syllabus content")
                return False

            # Get all modules
            modules = syllabus_content.find_all('div', class_='syllabus-section-header')
            for module in modules:
                # Get module title
                title_elem = module.find('div', class_='title')
                module_title = title_elem.text.strip() if title_elem else "Unknown Module"
                
                # Get chapters container
                chapters = module.find_next_sibling('div', class_='syllabus-section-content')
                if not chapters:
                    continue

                # Get chapter items
                items = chapters.find_all('div', {'class': ['item-row', 'item-row-locked']})
                for item in items:
                    # Get chapter info
                    title_div = item.find('div', class_='title')
                    if not title_div:
                        continue
                    
                    title = title_div.text.strip()
                    completed = 'icon-done-container' in str(item)
                    duration = 'N/A'

                    # Try to get video link
                    video_link = item.find('a')
                    if video_link and video_link.get('href'):
                        page_url = video_link['href']
                        if not page_url.startswith('http'):
                            page_url = self.basque_url + page_url
                        
                        self.logger.info(f"Processing: {title}")
                        
                        try:
                            # Attempt to get video page
                            page_response = self.session.get(page_url)
                            
                            if page_response.status_code == 200:
                                # Extract duration from page text
                                duration = self.extract_duration(page_response.text)
                                
                                self.logger.info(f"Extracted duration for {title}: {duration}")
                            
                            time.sleep(1)  # Respect site request policy
                        except Exception as e:
                            self.logger.error(f"Error processing {title}: {str(e)}")

                    # Save data
                    self.videos_data.append({
                        'module': module_title,
                        'chapter': title,
                        'duration': duration,
                        'completed': completed
                    })

            return True
        except Exception as e:
            self.logger.error(f"General error: {str(e)}")
            return False

    def save_to_json(self, filename='course_videos.json'):
        """Save video data to JSON file"""
        if not self.videos_data:
            self.logger.error("No data to save")
            return False

        try:
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(self.videos_data, file, indent=2, ensure_ascii=False)
            self.logger.info(f"Data saved to {filename}")
            return True
        except Exception as e:
            self.logger.error(f"Error saving JSON file: {str(e)}")
            return False

    def save_to_excel(self, filename='course_videos.xlsx'):
        """Save video data to Excel file"""
        if not self.videos_data:
            self.logger.error("No data to save")
            return False

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

            self.logger.info(f"Data saved to {filename}")
            return True
        except Exception as e:
            self.logger.error(f"Error saving Excel file: {str(e)}")
            return False

    def print_summary(self):
        """Print formatted summary of videos"""
        if not self.videos_data:
            print("No data to display")
            return

        current_module = None
        for video in self.videos_data:
            if current_module != video['module']:
                current_module = video['module']
                print(f"\n{current_module}")
                print("=" * len(current_module))
            
            status = "✓" if video['completed'] else " "
            print(f"{status} {video['chapter']} - Duration: {video['duration']}")

def main():
    # Load environment variables
    load_dotenv()
    
    # Get credentials
    email = os.getenv('DEVCAMP_EMAIL')
    password = os.getenv('DEVCAMP_PASSWORD')
    
    if not email or not password:
        print("Please set DEVCAMP_EMAIL and DEVCAMP_PASSWORD in .env file")
        return
    
    # Create scraper instance
    scraper = CourseVideoScraper()
    
    # Login
    print("Logging in...")
    if not scraper.login(email, password):
        print("Login failed!")
        return
    
    # Extract videos data
    print("Extracting course content...")
    if scraper.extract_course_content():
        # Print summary
        scraper.print_summary()
        
        # Save to JSON
        scraper.save_to_json()
        
        # Save to Excel
        scraper.save_to_excel()
    else:
        print("Failed to extract course content")

if __name__ == "__main__":
    main()