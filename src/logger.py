import os
import logging
from datetime import datetime

# Create logs directory if it doesn't exist
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

# Set log file name based on current date
log_file = os.path.join(log_dir, f"{datetime.now().date()}.log")

# Configure logging
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="[%(asctime)s]: %(levelname)s: %(message)s"
)

