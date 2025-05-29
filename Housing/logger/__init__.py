import logging
import datetime
import os

log_dir = "housing_logs"

CURRENT_TIME_STAMP = f"{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"

LOG_FILE_NAME = f"log_{CURRENT_TIME_STAMP}.log"

os.makedirs(log_dir,exist_ok=True)

LOG_FILE_PATH = os.path.join(log_dir,LOG_FILE_NAME)
logging.basicConfig(
                    filename=LOG_FILE_PATH, 
                    filemode="w",
                    format= '[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO
                    )


