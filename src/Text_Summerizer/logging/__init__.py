import os
import sys
import logging

logging_str = "[%(asctime)s | %(levelname)-8s | %(name)-12s | %(funcName)-20s:%(lineno)-4d] %(message)s"
log_directory = "logs"
log_filepath = os.path.join(log_directory, "running_logs.log")
os.makedirs(log_directory, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,  # Correct case: level (lowercase)
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("TextSummarizerLogger")
