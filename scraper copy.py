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
        """Extract video duration from the page"""
        try:
            self.logger.info(f"Getting duration from: {chapter_url}")
            
            # Add video-specific headers
            headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                'Connection': 'keep-alive',
                'Referer': self.course_url,
                'Cache-Control': 'no-cache'
            }
            
            response = self.session.get(chapter_url, headers=headers)
            if response.status_code != 200:
                self.logger.error(f"Failed to get page: {response.status_code}")
                return "N/A"
                
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Method 1: Duration display from video player
            duration_elem = soup.find('span', class_='vjs-duration-display', attrs={'aria-live': 'off'})
            if duration_elem:
                duration_text = duration_elem.text.strip()
                if duration_text and duration_text != "":
                    self.logger.debug(f"Found duration from display: {duration_text}")
                    return duration_text.replace('Duration Time ', '')

            # Method 2: Video element duration
            video_elem = soup.find('video', {'id': 'video_html5_api'})
            if video_elem:
                # Try getting from aria-valuetext
                progress_holder = soup.find('div', {'class': 'vjs-progress-holder'})
                if progress_holder and 'aria-valuetext' in progress_holder.attrs:
                    value_text = progress_holder['aria-valuetext']
                    match = re.search(r'of\s+(\d+:\d+)', value_text)
                    if match:
                        duration = match.group(1)
                        self.logger.debug(f"Found duration from aria-valuetext: {duration}")
                        return duration

            # Method 3: Look for duration in any text that matches MM:SS format
            duration_pattern = re.compile(r'\b\d{1,2}:\d{2}\b')
            duration_matches = soup.find_all(string=duration_pattern)
            if duration_matches:
                for match in duration_matches:
                    found_duration = duration_pattern.search(match).group()
                    if found_duration != "0:00":  # Skip initial time
                        self.logger.debug(f"Found duration from text: {found_duration}")
                        return found_duration

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
            self.logger.info("Accessing course page...")
            response = self.session.get(self.course_url)
            self.logger.debug(f"Course page status: {response.status_code}")
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Debug the HTML structure
            self.logger.debug("Looking for content container...")
            
            # List all div classes in the document for debugging
            all_divs = soup.find_all('div')
            classes = set()
            for div in all_divs:
                if div.get('class'):
                    classes.update(div.get('class'))
            self.logger.debug(f"Available div classes: {sorted(list(classes))}")
            
            # Try to find the container
            content_container = soup.find('div', {'class': 'container trails-campsites-guides'})
            if not content_container:
                self.logger.error("Could not find trails-campsites-guides container")
                # Save the HTML for debugging
                with open('debug_page.html', 'w', encoding='utf-8') as f:
                    f.write(response.text)
                self.logger.debug("Saved HTML to debug_page.html")
                return False

            # Get guide content
            guide_content = content_container.find('div', class_='guide-content')
            if not guide_content:
                self.logger.error("Could not find guide content")
                return False

            # Find all modules - div elements with module information
            module_elements = guide_content.find_all('div', class_='module-info')
            self.logger.info(f"Found {len(module_elements)} modules")
            
            # Debug the HTML structure
            self.logger.debug("HTML structure:")
            for section in module_sections[:2]:  # Log first two sections for debugging
                self.logger.debug(f"Section classes: {section.get('class', [])}")
                self.logger.debug(f"Section content preview: {section.text[:100]}")
            
            for module_elem in module_elements:
                # Get module title
                module_title = f"Module {module_elem.get('data-module-number', 'Unknown')}"
                self.logger.info(f"\nProcessing {module_title}")
                
                # Get chapters
                chapters_container = module_elem.find_next_sibling('div', class_='module-chapters')
                if not chapters_container:
                    continue

                # Find all chapter items
                chapter_items = chapters_container.find_all('div', class_=['chapter', 'chapter-locked'])
                self.logger.debug(f"Found {len(chapter_items)} chapters in {module_title}")
                
                module_title = module_title.text.strip()
                self.logger.info(f"\nProcessing Module: {module_title}")
                
                for chapter in chapter_items:
                    # Get chapter title
                    title_elem = chapter.find('a', class_='chapter-title')
                    if not title_elem:
                        continue
                        
                    title = title_elem.text.strip()
                    is_locked = 'chapter-locked' in chapter.get('class', [])
                    duration = 'N/A'
                    
                    # Only get duration for unlocked chapters
                    if not is_locked:
                        chapter_url = title_elem.get('href', '')
                        if chapter_url:
                            if not chapter_url.startswith('http'):
                                chapter_url = self.basque_url + chapter_url
                            self.logger.info(f"Getting duration for: {title}")
                            self.logger.debug(f"Chapter URL: {chapter_url}")
                            duration = self.get_chapter_duration(chapter_url)
                            time.sleep(2)  # Polite delay between requests
                    
                    self.videos_data.append({
                        'module': module_title,
                        'chapter': title,
                        'duration': duration,
                        'locked': is_locked
                    })
                
                for idx, item in enumerate(chapter_items, 1):
                    title_elem = item.find('div', class_='title')
                    if not title_elem:
                        continue
                        
                    title = title_elem.text.strip()
                    is_locked = 'item-row-locked' in item.get('class', [])
                    duration = 'N/A'
                    
                    # Only get duration for unlocked chapters that are links
                    if not is_locked and item.name == 'a':
                        chapter_url = item.get('href', '')
                        if chapter_url:
                            if not chapter_url.startswith('http'):
                                chapter_url = self.basque_url + chapter_url
                            self.logger.info(f"[{idx}/{len(chapter_items)}] Getting duration for: {title}")
                            self.logger.debug(f"Chapter URL: {chapter_url}")
                            duration = self.get_chapter_duration(chapter_url)
                            time.sleep(2)  # Polite delay between requests
                    
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