import requests
from bs4 import BeautifulSoup
import json
import os
from datetime import datetime
from dotenv import load_dotenv
import logging
import time

class CourseVideoScraper:
    def __init__(self):
        self.base_url = "https://devcamp.com"
        self.basque_url = "https://basque.devcamp.com"
        self.login_url = f"{self.base_url}/users/sign_in"
        self.course_url = f"{self.basque_url}/pt-full-stack-development-javascript-python-react"
        self.session = requests.Session()
        self.videos_data = []
        
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

            # Perform login
            self.logger.info("Attempting login...")
            response = self.session.post(
                self.login_url,
                data=login_data,
                headers={'X-CSRF-Token': csrf_token},
                allow_redirects=True
            )

            # Verify login
            verify_response = self.session.get(self.course_url)
            if 'sign_in' in verify_response.url.lower():
                self.logger.error("Login failed")
                return False

            self.logger.info("Login successful!")
            return True

        except Exception as e:
            self.logger.error(f"Login error: {str(e)}")
            return False

    def get_chapter_duration(self, chapter_url):
        """Extract video duration from chapter page"""
        try:
            self.logger.info(f"Getting duration from: {chapter_url}")
            
            headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1',
                'Cache-Control': 'max-age=0'
            }
            
            # First request to get the page
            response = self.session.get(chapter_url, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Look for video source
            video_elem = soup.find('video')
            if video_elem and video_elem.get('src'):
                # Get video metadata
                video_url = video_elem['src']
                if not video_url.startswith('http'):
                    video_url = self.basque_url + video_url
                
                # Make HEAD request to get video duration
                video_response = self.session.head(video_url, headers=headers)
                content_length = video_response.headers.get('Content-Length')
                if content_length:
                    # Estimate duration based on file size (rough estimation)
                    size_mb = int(content_length) / (1024 * 1024)
                    estimated_duration = int(size_mb * 0.5)  # Rough estimate: 2MB per minute
                    minutes = estimated_duration // 60
                    seconds = estimated_duration % 60
                    self.logger.debug(f"Estimated duration from file size: {minutes}:{seconds:02d}")
                    return f"{minutes}:{seconds:02d}"
            
            # Look for duration in the page
            duration_display = soup.find('span', class_='vjs-duration-display')
            if duration_display:
                duration = duration_display.text.strip()
                if duration != "0:00":
                    self.logger.debug(f"Found duration in player: {duration}")
                    return duration
            
            # Try to find any element with time format
            time_pattern = r'\b(\d{1,2}):(\d{2})\b'
            for element in soup.find_all(text=True):
                match = re.search(time_pattern, element)
                if match:
                    duration = match.group()
                    # Validate duration format
                    try:
                        minutes, seconds = map(int, duration.split(':'))
                        if 0 <= minutes < 180 and 0 <= seconds < 60:  # Reasonable duration limits
                            self.logger.debug(f"Found duration in text: {duration}")
                            return duration
                    except ValueError:
                        continue
            
            self.logger.warning(f"No valid duration found for chapter: {chapter_url}")
            
            # Save failed chapter HTML for debugging
            with open(f'failed_chapter_{hash(chapter_url)}.html', 'w', encoding='utf-8') as f:
                f.write(response.text)
            
            return 'N/A'
            
        except Exception as e:
            self.logger.error(f"Error getting chapter duration: {str(e)}")
            import traceback
            self.logger.error(traceback.format_exc())
            return 'N/A'

    def extract_course_content(self):
        """Extract course structure and video durations"""
        try:
            self.logger.info("Accessing course page...")
            response = self.session.get(self.course_url)
            self.logger.debug(f"Course page status: {response.status_code}")
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Find the content container
            content = soup.find('div', class_='syllabus-content')
            if not content:
                self.logger.error("Could not find syllabus content")
                with open('error_page.html', 'w', encoding='utf-8') as f:
                    f.write(response.text)
                self.logger.debug("Saved error page to error_page.html")
                return False
                
            # Find all modules
            modules = content.find_all('div', class_='syllabus-section-header')
            self.logger.info(f"Found {len(modules)} modules")
            
            for module in modules:
                module_title = module.find('div', class_='title')
                if not module_title:
                    continue
                    
                module_title = module_title.text.strip()
                self.logger.info(f"\nProcessing Module: {module_title}")
                
                module_id = module.get('href', '').replace('#', '')
                
                # Find chapters
                if module_id:
                    chapter_container = soup.find('div', id=module_id)
                    if chapter_container:
                        chapter_items = chapter_container.find_all(['div', 'a'], class_=['item-row', 'item-row-locked'])
                        
                        for idx, item in enumerate(chapter_items, 1):
                            title_elem = item.find('div', class_='title')
                            if not title_elem:
                                continue
                                
                            title = title_elem.text.strip()
                            is_locked = 'item-row-locked' in item.get('class', [])
                            duration = 'N/A'
                            
                            if not is_locked and item.name == 'a':
                                chapter_url = self.basque_url + item.get('href', '')
                                self.logger.info(f"[{idx}/{len(chapter_items)}] Getting duration for: {title}")
                                duration = self.get_chapter_duration(chapter_url)
                                # Add small delay to avoid overwhelming the server
                                time.sleep(1)
                            
                            self.videos_data.append({
                                'module': module_title,
                                'chapter': title,
                                'duration': duration,
                                'locked': is_locked
                            })
            
            return True
            
        except Exception as e:
            self.logger.error(f"Error extracting course content: {str(e)}")
            return False

    def save_to_json(self, output_file=None):
        """Save video data to JSON file"""
        if not self.videos_data:
            self.logger.error("No data to save")
            return False

        if output_file is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_file = f'course_videos_{timestamp}.json'

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
            
            status = "🔒" if video['locked'] else "✓"
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