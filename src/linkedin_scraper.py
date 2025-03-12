import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import os
import tempfile
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from html2pdf import HTMLToPDF
import time
from logger import get_logger

# Setup module logger
logger = get_logger('linkedin_scraper')

class LinkedInScraper:
    """
    Class to handle LinkedIn profile scraping functionality.
    """
    
    def __init__(self):
        self.logger = logger
        self.html2pdf = HTMLToPDF()
    
    def is_valid_linkedin_url(self, url):
        """
        Validate if the URL is a LinkedIn profile URL.
        """
        try:
            parsed_url = urlparse(url)
            return (parsed_url.netloc == 'www.linkedin.com' or 
                    parsed_url.netloc == 'linkedin.com') and '/in/' in parsed_url.path
        except:
            return False
    
    def scrape_public_profile(self, url):
        """
        Scrape a public LinkedIn profile without requiring login.
        Uses Selenium with headless Chrome to render JavaScript.
        
        Args:
            url: LinkedIn profile URL
            
        Returns:
            Tuple of (extracted_text, pdf_bytes)
        """
        if not self.is_valid_linkedin_url(url):
            self.logger.error(f"Invalid LinkedIn URL: {url}")
            raise ValueError("Invalid LinkedIn profile URL. Please provide a URL in format: https://www.linkedin.com/in/username")
        
        self.logger.info(f"Scraping LinkedIn profile: {url}")
        
        try:
            # Configure headless Chrome browser
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--window-size=1920,1080")
            # Use a common User-Agent to avoid detection
            chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")
            
            self.logger.debug("Initializing Chrome WebDriver")
            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=chrome_options)
            
            # Visit the LinkedIn profile
            self.logger.debug(f"Navigating to URL: {url}")
            driver.get(url)
            
            # Wait for the page to load completely
            time.sleep(5)
            
            # Get the page source
            page_source = driver.page_source
            soup = BeautifulSoup(page_source, 'html.parser')
            
            # Extract text content from the page
            self.logger.debug("Extracting text content from LinkedIn profile")
            
            # Create a temporary HTML file with cleaned profile content
            profile_content = self._clean_linkedin_html(soup)
            
            # Extract plain text for processing
            extracted_text = self._extract_plain_text(soup)
            
            # Generate PDF from the HTML content
            with tempfile.NamedTemporaryFile(suffix='.html', delete=False) as temp_html:
                temp_html.write(profile_content.encode('utf-8'))
                temp_html_path = temp_html.name
            
            self.logger.debug(f"Converting LinkedIn profile to PDF")
            pdf_bytes = self.html2pdf.convert_html_to_pdf(temp_html_path)
            
            # Clean up temporary file
            if os.path.exists(temp_html_path):
                os.unlink(temp_html_path)
            
            # Close the browser
            driver.quit()
            
            self.logger.info(f"Successfully scraped LinkedIn profile: {url}")
            return extracted_text, pdf_bytes
            
        except Exception as e:
            self.logger.error(f"Error scraping LinkedIn profile: {str(e)}")
            raise Exception(f"Failed to scrape LinkedIn profile: {str(e)}")
    
    def _clean_linkedin_html(self, soup):
        """
        Clean the LinkedIn HTML to only keep relevant profile information.
        
        Args:
            soup: BeautifulSoup object of the LinkedIn profile page
            
        Returns:
            Clean HTML string with only relevant profile sections
        """
        # Create a basic HTML structure
        clean_html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>LinkedIn Profile</title>
            <style>
                body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
                h1, h2, h3 { color: #0077b5; }
                .section { margin-bottom: 20px; padding-bottom: 20px; border-bottom: 1px solid #eee; }
            </style>
        </head>
        <body>
        """
        
        # Extract profile name
        name_tag = soup.find('h1', class_='text-heading-xlarge')
        if name_tag:
            clean_html += f"<h1>{name_tag.get_text(strip=True)}</h1>"
        
        # Extract headline
        headline_tag = soup.find('div', class_='text-body-medium')
        if headline_tag:
            clean_html += f"<p><strong>{headline_tag.get_text(strip=True)}</strong></p>"
        
        # Extract about section
        about_section = soup.find('div', {'id': 'about'})
        if about_section:
            about_text = about_section.find('div', class_='display-flex')
            if about_text:
                clean_html += "<div class='section'><h2>About</h2>"
                clean_html += f"<p>{about_text.get_text(strip=True)}</p></div>"
        
        # Extract experience section
        experience_section = soup.find('div', {'id': 'experience'})
        if experience_section:
            clean_html += "<div class='section'><h2>Experience</h2>"
            experience_items = experience_section.find_all('li', class_='artdeco-list__item')
            for item in experience_items:
                position = item.find('div', class_='display-flex')
                if position:
                    clean_html += f"<div>{position.get_text(strip=True)}</div>"
            clean_html += "</div>"
        
        # Extract education section
        education_section = soup.find('div', {'id': 'education'})
        if education_section:
            clean_html += "<div class='section'><h2>Education</h2>"
            education_items = education_section.find_all('li', class_='artdeco-list__item')
            for item in education_items:
                education = item.find('div', class_='display-flex')
                if education:
                    clean_html += f"<div>{education.get_text(strip=True)}</div>"
            clean_html += "</div>"
        
        # Extract skills section
        skills_section = soup.find('div', {'id': 'skills'})
        if skills_section:
            clean_html += "<div class='section'><h2>Skills</h2>"
            skills_items = skills_section.find_all('li', class_='artdeco-list__item')
            for item in skills_items:
                skill = item.find('div', class_='display-flex')
                if skill:
                    clean_html += f"<div>{skill.get_text(strip=True)}</div>"
            clean_html += "</div>"
        
        # Close HTML tags
        clean_html += """
        </body>
        </html>
        """
        
        return clean_html
    
    def _extract_plain_text(self, soup):
        """
        Extract plain text from the LinkedIn profile for processing.
        
        Args:
            soup: BeautifulSoup object of the LinkedIn profile page
            
        Returns:
            Plain text representation of the profile
        """
        text_parts = []
        
        # Extract profile name
        name_tag = soup.find('h1', class_='text-heading-xlarge')
        if name_tag:
            text_parts.append(f"Name: {name_tag.get_text(strip=True)}")
        
        # Extract headline
        headline_tag = soup.find('div', class_='text-body-medium')
        if headline_tag:
            text_parts.append(f"Headline: {headline_tag.get_text(strip=True)}")
        
        # Extract about section
        about_section = soup.find('div', {'id': 'about'})
        if about_section:
            about_text = about_section.find('div', class_='display-flex')
            if about_text:
                text_parts.append(f"About: {about_text.get_text(strip=True)}")
        
        # Extract experience section
        experience_section = soup.find('div', {'id': 'experience'})
        if experience_section:
            text_parts.append("Experience:")
            experience_items = experience_section.find_all('li', class_='artdeco-list__item')
            for item in experience_items:
                position = item.find('div', class_='display-flex')
                if position:
                    text_parts.append(f"- {position.get_text(strip=True)}")
        
        # Extract education section
        education_section = soup.find('div', {'id': 'education'})
        if education_section:
            text_parts.append("Education:")
            education_items = education_section.find_all('li', class_='artdeco-list__item')
            for item in education_items:
                education = item.find('div', class_='display-flex')
                if education:
                    text_parts.append(f"- {education.get_text(strip=True)}")
        
        # Extract skills section
        skills_section = soup.find('div', {'id': 'skills'})
        if skills_section:
            text_parts.append("Skills:")
            skills_items = skills_section.find_all('li', class_='artdeco-list__item')
            for item in skills_items:
                skill = item.find('div', class_='display-flex')
                if skill:
                    text_parts.append(f"- {skill.get_text(strip=True)}")
        
        return "\n\n".join(text_parts) 