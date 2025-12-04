import time
import logging

from config import get_logger

logger = get_logger(__name__)

def main():
    logger.info("Starting KoalixCRM Background Service...")
    while True:
        logger.info("Background service is running...")
        time.sleep(60)

if __name__ == "__main__":
    main()
