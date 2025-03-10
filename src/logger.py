import logging
import os
import sys
from datetime import datetime

# Create logs directory if it doesn't exist
os.makedirs('logs', exist_ok=True)

# Configure the root logger
def setup_logger():
    """
    Set up and configure the application logger.
    Logs will be sent to both the console and a log file.
    """
    # Create a unique log file for this session
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = f"logs/resullme_{timestamp}.log"
    
    # Configure the root logger
    logger = logging.getLogger('resullme')
    logger.setLevel(logging.DEBUG)  # Capture all levels in the logger
    
    # Clear any existing handlers
    if logger.handlers:
        logger.handlers.clear()
    
    # Create console handler with a higher log level (INFO)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(console_format)
    
    # Create file handler which logs even debug messages
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)
    file_format = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
    file_handler.setFormatter(file_format)
    
    # Add the handlers to the logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    
    logger.info(f"Logger initialized. Logs will be stored in {log_file}")
    return logger

# Create the global logger instance
logger = setup_logger()

def get_logger(name=None):
    """
    Get a named logger that inherits from the main logger.
    This allows for better identification of log sources.
    
    Args:
        name: Optional name of the module requesting the logger
        
    Returns:
        A logger instance configured with the given name
    """
    if name:
        return logging.getLogger(f'resullme.{name}')
    return logging.getLogger('resullme') 