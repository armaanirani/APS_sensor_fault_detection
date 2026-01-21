from src.exception import SensorException
from src.logger import logging
from src.utils import dump_csv_file_to_mongodb_collection
import sys
import os



if __name__ == "__main__":
    file_path = r"C:\CS\kish naik\APS_sensor_fault_detection\aps_failure_training_set1.csv"
    database_name = "aps"
    collection_name = "sensor"
    
    dump_csv_file_to_mongodb_collection(
        file_path=file_path, 
        database_name=database_name, 
        collection_name=collection_name
    )