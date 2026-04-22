from src.heart_disease_prediction.exception import CustomException
import sys
from src.heart_disease_prediction.logger import logging
from src.heart_disease_prediction.components.data_ingestion import DataIngestion
from src.heart_disease_prediction.components.data_ingestion import DataIngestionConfig
from src.heart_disease_prediction.utils import read_sql_data

if __name__ == "__main__":
    logging.info("Starting the ML project")
    try:
        
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()
        
    except Exception as e:
        logging.error("An error occurred in the ML project"),
        logging.info("custom error")