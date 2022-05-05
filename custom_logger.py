import logging
import os

# Disable WebDriver manager logs
os.environ["WDM_LOG_LEVEL"] = "0"


def get_custom_logger(name):
    formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(name)s>>%(lineno)d - %(message)s')

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.propagate = False
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)
    return logger
