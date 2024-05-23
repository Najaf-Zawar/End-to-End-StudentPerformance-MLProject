import logging
import os
from datetime import datetime


LOG_FIle = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path= os.path.join(os.getcwd(), "logs", LOG_FIle)
os.makedirs(logs_path, exist_ok=True)


LOG_FIle_PATH = os.path.join(logs_path, LOG_FIle)

logging.basicConfig(
    filename=LOG_FIle_PATH,
    format= "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s ",
    level=logging.INFO,
)


# For Testing
'''
if __name__ == "__main__":
    logging.info("Logging has started")
'''
