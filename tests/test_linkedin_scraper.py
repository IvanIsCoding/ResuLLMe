#!/usr/bin/env python3
"""
Test script for LinkedIn profile scraping functionality.
Run this script to test if the LinkedIn scraper works correctly.
"""

import os
import sys
import argparse

# Add parent directory to path to allow importing modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.linkedin_scraper import LinkedInScraper
from src.logger import get_logger

# Setup logger
logger = get_logger('test_linkedin_scraper')

def test_scraper(linkedin_url, output_dir=None):
    """
    Test the LinkedIn scraper with a given profile URL.
    
    Args:
        linkedin_url: URL of the LinkedIn profile to scrape
        output_dir: Directory to save the output PDF (optional)
    """
    logger.info(f"Testing LinkedIn scraper with URL: {linkedin_url}")
    
    try:
        # Initialize scraper
        scraper = LinkedInScraper()
        
        # Validate URL
        if not scraper.is_valid_linkedin_url(linkedin_url):
            logger.error(f"Invalid LinkedIn URL: {linkedin_url}")
            print(f"Error: Invalid LinkedIn URL. Please provide a URL in format: https://www.linkedin.com/in/username")
            return False
        
        # Scrape profile
        print(f"Scraping LinkedIn profile: {linkedin_url}")
        extracted_text, pdf_bytes = scraper.scrape_public_profile(linkedin_url)
        
        # Print extracted text preview
        print("\nExtracted Text Preview:")
        print("-----------------------")
        preview_lines = extracted_text.split('\n')[:10]
        print("\n".join(preview_lines))
        print("...")
        
        # Save PDF if output directory provided
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
            username = linkedin_url.rstrip('/').split('/')[-1]
            pdf_path = os.path.join(output_dir, f"{username}_linkedin.pdf")
            
            with open(pdf_path, 'wb') as f:
                f.write(pdf_bytes)
            
            print(f"\nPDF saved to: {pdf_path}")
        
        print("\nLinkedIn scraper test completed successfully!")
        return True
        
    except Exception as e:
        logger.error(f"Error testing LinkedIn scraper: {str(e)}")
        print(f"Error: {str(e)}")
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Test the LinkedIn profile scraper")
    parser.add_argument("url", help="LinkedIn profile URL to scrape")
    parser.add_argument("-o", "--output", help="Directory to save the output PDF", default=None)
    
    args = parser.parse_args()
    
    success = test_scraper(args.url, args.output)
    sys.exit(0 if success else 1) 