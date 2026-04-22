import os
import sys
from src.heart_disease_prediction.exception import CustomException
from src.heart_disease_prediction.logger import logging
from src.heart_disease_prediction.utils import read_sql_data
import pandas as pd
from dataclasses import dataclass

class FeatureEngineering:
    def __init__(self):
        pass

    def initiate_feature_engineering(self):
        logging.info("Entered the feature engineering method or component")
        try:
            df = read_sql_data()
            df = df.dropna()
            df.drop_duplicates(inplace=True)
            print(df.head())
            return df
            logging.info("Feature engineering is completed")


        except Exception as e:
            raise CustomException(e, sys)