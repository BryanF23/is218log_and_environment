# main.py
import logging
import logging.config
from dotenv import load_dotenv
import os
from app import App    

# Load environment variables from .env file
load_dotenv()

# Access environment variables
environment = os.getenv('ENVIRONMENT')
debug = os.getenv('DEBUG')

print(f"Environment: {environment}")
print(f"Debug: {debug}")

# Load logging configuration
logging.config.fileConfig('logging.conf')

# Create a logger
logger = logging.getLogger(__name__)

# Log a test message
logger.info('This is a debug message')

# You must put this in your main.py because this forces the program to start when you run it from the command line.
if __name__ == "__main__":
    logger.info("Starting application...")
    app = App().start()  # Instantiate an instance of App
    logger.info("Application started.")
    