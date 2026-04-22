import os
import sys
from src.heart_disease_prediction.exception import CustomException
from src.heart_disease_prediction.logger import logging
import pandas as pd
from src.heart_disease_prediction.components.feature_engineering import FeatureEngineering
from dataclasses import dataclass
from sklearn.model_selection import train_test_split
@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('data_file','train.csv')
    test_data_path: str=os.path.join('data_file','test.csv')
    raw_data_path: str=os.path.join('data_file','data.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df = FeatureEngineering().initiate_feature_engineering()

            logging.info("Read the dataset as dataframe")
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            logging.info("Train test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Ingestion of the data is completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e, sys)
        
    