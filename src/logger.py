
import logging
import os
from datetime import datetime

LOG_DIR = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

logs_path = os.path.join(os.getcwd(), "logs", LOG_DIR)

os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, "running_logs.log")

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

if __name__ == "__main__":
    logging.info("Logging has started")

