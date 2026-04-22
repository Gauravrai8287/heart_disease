import os
import logging
from datetime import datetime

# Create logs directory
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# File name with timestamp
LOG_FILE = f"log_{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"

# Full path
LOG_PATH = os.path.join(os.getcwd(),"logs", LOG_FILE)
os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)
# Logging config
logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format="[%(asctime)s] - %(lineno)d - %(name)s-%(levelname)s - %(message)s"
)