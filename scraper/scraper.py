import requests
from bs4 import BeautifulSoup
import json
import os
from datetime import datetime
from dotenv import load_dotenv
import logging
import time
import re

class CourseVideoScraper:
    def __init__(self):
        # Configure logging first
        logging.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)
        
        # Initialize other attributes
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
        
    def format_duration(self, duration):
        """Format duration to MM:SS format"""
        try:
            # If duration is in seconds (string or float)
            duration = float(duration)
            minutes = int(duration // 60)
            seconds = int(duration % 60)
            return f"{minutes:02d}:{seconds:02d}"
        except (ValueError, TypeError):
            # If duration is already in MM:SS format
            if isinstance(duration, str):
                # Try to extract minutes and seconds from string
                match = re.search(r'(\d+):(\d+)', duration)
                if match:
                    return f"{int(match.group(1)):02d}:{int(match.group(2)):02d}"
            return "N/A"
        
        # Configure logging
        logging.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)
        
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

    def get_chapter_duration(self, chapter_url):
        """Extract video duration from the page"""
        try:
            self.logger.info(f"Getting duration from: {chapter_url}")
            
            # Add video-specific headers
            headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                'Connection': 'keep-alive',
                'Referer': self.course_url,
                'Cache-Control': 'no-cache',
                'X-Requested-With': 'XMLHttpRequest'
            }
            
            response = self.session.get(chapter_url, headers=headers)
            if response.status_code != 200:
                self.logger.error(f"Failed to get page: {response.status_code}")
                return "N/A"
                
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Debug HTML structure
            self.logger.debug("Looking for video duration elements...")
            
            # Method 1: Try to get duration from the duration display
            duration_display = soup.find('span', class_='vjs-duration-display')
            if duration_display:
                duration_text = duration_display.text.strip()
                if duration_text and duration_text != "":
                    self.logger.debug(f"Found duration in display: {duration_text}")
                    return self.format_duration(duration_text)
            
            # Method 2: Look for duration in video-js data
            video_container = soup.find('div', class_='video-js')
            if video_container:
                self.logger.debug("Found video-js container")
                # Check for data attributes
                for attr in video_container.attrs:
                    if 'duration' in attr.lower():
                        self.logger.debug(f"Found duration in attribute: {attr}")
                        return self.format_duration(video_container[attr])

            # Method 2: Look for duration in metadata
            meta_duration = soup.find('meta', {'property': 'video:duration'}) or \
                          soup.find('meta', {'name': 'duration'})
            if meta_duration:
                self.logger.debug(f"Found duration in metadata: {meta_duration['content']}")
                return self.format_duration(meta_duration['content'])

            # Method 3: Check for duration in video element
            video_elem = soup.find('video')
            if video_elem and video_elem.get('duration'):
                self.logger.debug(f"Found duration in video element: {video_elem['duration']}")
                return self.format_duration(video_elem['duration'])

            # Method 4: Look for time element or span
            time_elem = soup.find('time') or \
                       soup.find('span', class_=lambda x: x and 'duration' in x.lower())
            if time_elem:
                duration_text = time_elem.get_text().strip()
                if duration_text:
                    self.logger.debug(f"Found duration in time element: {duration_text}")
                    # Extract numbers from the text
                    numbers = re.findall(r'\d+', duration_text)
                    if len(numbers) >= 2:
                        return f"{numbers[0].zfill(2)}:{numbers[1].zfill(2)}"

            # Save HTML for debugging
            debug_filename = f'debug_chapter_{hash(chapter_url)}.html'
            with open(debug_filename, 'w', encoding='utf-8') as f:
                f.write(response.text)
            self.logger.warning(f"No duration found. Saved debug HTML to: {debug_filename}")
            
            return "N/A"

        except Exception as e:
            self.logger.error(f"Error getting chapter duration: {str(e)}")
            return "N/A"

    def extract_course_content(self):
        """Extract course structure and video durations"""
        try:
            # Get initial page
            response = self.session.get(self.course_url)
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find syllabus content
            syllabus_content = soup.find('div', class_='syllabus-content')
            if not syllabus_content:
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
                        
                        try:
                            page = self.session.get(page_url)
                            if page.status_code == 200:
                                page_soup = BeautifulSoup(page.text, 'html.parser')
                                duration_span = page_soup.find('span', class_='vjs-duration-display')
                                if duration_span:
                                    duration = duration_span.text.strip()
                            time.sleep(1)
                        except:
                            pass

                    # Save data
                    self.videos_data.append({
                        'module': module_title,
                        'chapter': title,
                        'duration': duration,
                        'completed': completed
                    })

            return True
        except Exception as e:
            self.logger.error(f"Error: {str(e)}")
            return False

    def save_to_json(self):
        """Save video data to JSON file"""
        if not self.videos_data:
            self.logger.error("No data to save")
            return False

        output_file = 'course_videos.json'
        try:
            with open(output_file, 'w', encoding='utf-8') as file:
                json.dump(self.videos_data, file, indent=2, ensure_ascii=False)
            self.logger.info(f"Data saved to {output_file}")
            return True
        except Exception as e:
            self.logger.error(f"Error saving JSON file: {str(e)}")
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
    else:
        print("Failed to extract course content")

if __name__ == "__main__":
    main()