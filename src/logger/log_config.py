import logging
import os
from datetime import datetime

# Generate log file name with current timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define the log directory and ensure it exists
log_path = os.path.join(os.getcwd(), "practice" , "logs")
os.makedirs(log_path, exist_ok=True)

# Define the full log file path
LOG_FILEPATH = os.path.join(log_path, LOG_FILE)

# Print statements for debugging
print(f"Log directory: {log_path}")
print(f"Log file path: {LOG_FILEPATH}")

# Configure logging
logging.basicConfig(level=logging.INFO,
                    filename=LOG_FILEPATH,
                    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s")

logging.info("This is test from log_config.py")
