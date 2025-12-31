from src.sensor.exception import SensorException
from src.sensor.logger import logging
import sys
import os

def test_exception():
    try:
        logging.info("starting")
        a = 1/0
    except Exception as e:
        raise SensorException(e, sys)


if __name__ == "__main__":
    try:
        test_exception()
    except Exception as e:
        print(e)