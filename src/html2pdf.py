import os
import tempfile
import subprocess
from logger import get_logger

# Setup module logger
logger = get_logger('html2pdf')

class HTMLToPDF:
    """
    A utility class for converting HTML content to PDF using wkhtmltopdf.
    """
    
    def __init__(self):
        self.logger = logger
    
    def convert_html_to_pdf(self, html_path):
        """
        Convert HTML file to PDF using wkhtmltopdf.
        
        Args:
            html_path: Path to the HTML file
            
        Returns:
            PDF content as bytes
        """
        try:
            # Create a temporary file for the PDF output
            with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as temp_pdf:
                temp_pdf_path = temp_pdf.name
            
            self.logger.debug(f"Converting HTML file to PDF: {html_path} -> {temp_pdf_path}")
            
            # Check if pdfkit is available
            try:
                # Use pdfkit if available
                self._convert_with_pdfkit(html_path, temp_pdf_path)
            except:
                # Fall back to alternative approach using Chrome headless
                self.logger.warning("pdfkit/wkhtmltopdf not available, falling back to Chrome headless")
                self._convert_with_chrome(html_path, temp_pdf_path)
            
            # Read the generated PDF file
            with open(temp_pdf_path, 'rb') as pdf_file:
                pdf_content = pdf_file.read()
            
            # Clean up the temporary PDF file
            if os.path.exists(temp_pdf_path):
                os.unlink(temp_pdf_path)
            
            self.logger.info(f"Successfully converted HTML to PDF ({len(pdf_content)} bytes)")
            return pdf_content
            
        except Exception as e:
            self.logger.error(f"Error converting HTML to PDF: {str(e)}")
            raise Exception(f"Failed to convert HTML to PDF: {str(e)}")
    
    def _convert_with_pdfkit(self, html_path, pdf_path):
        """
        Convert HTML to PDF using pdfkit (which uses wkhtmltopdf).
        
        Args:
            html_path: Path to the HTML file
            pdf_path: Path to save the PDF file
            
        Raises:
            Exception: If pdfkit is not available or conversion fails
        """
        try:
            import pdfkit
            
            # Configure pdfkit options
            options = {
                'page-size': 'Letter',
                'margin-top': '0.75in',
                'margin-right': '0.75in',
                'margin-bottom': '0.75in',
                'margin-left': '0.75in',
                'encoding': 'UTF-8',
                'quiet': ''
            }
            
            self.logger.debug(f"Running pdfkit to convert HTML to PDF")
            pdfkit.from_file(html_path, pdf_path, options=options)
            self.logger.debug("pdfkit conversion successful")
            
        except ImportError:
            self.logger.error("pdfkit not installed")
            raise Exception("pdfkit not installed")
        except Exception as e:
            self.logger.error(f"pdfkit conversion failed: {str(e)}")
            raise Exception(f"pdfkit conversion failed: {str(e)}")
    
    def _convert_with_chrome(self, html_path, pdf_path):
        """
        Convert HTML to PDF using Chrome in headless mode.
        This is a fallback method if wkhtmltopdf is not available.
        
        Args:
            html_path: Path to the HTML file
            pdf_path: Path to save the PDF file
            
        Raises:
            Exception: If Chrome is not available or conversion fails
        """
        try:
            from selenium import webdriver
            from selenium.webdriver.chrome.options import Options
            from selenium.webdriver.chrome.service import Service
            from webdriver_manager.chrome import ChromeDriverManager
            
            self.logger.debug("Initializing Chrome for PDF conversion")
            
            # Set up Chrome options for headless PDF printing
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--print-to-pdf=" + pdf_path)
            
            # Initialize Chrome driver
            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=chrome_options)
            
            # Load the HTML file
            file_url = f"file://{html_path}"
            self.logger.debug(f"Loading HTML file in Chrome: {file_url}")
            driver.get(file_url)
            
            # Wait for PDF to be generated
            import time
            time.sleep(5)
            
            # Close the driver
            driver.quit()
            
            self.logger.debug("Chrome successfully converted HTML to PDF")
            
        except Exception as e:
            self.logger.error(f"Error converting with Chrome: {str(e)}")
            raise Exception(f"Failed to convert with Chrome: {str(e)}") 