import sys
import os
import pandas as pd

from src.heart_disease_prediction.exception import CustomException
from src.heart_disease_prediction.utils import load_object
from src.heart_disease_prediction.logger import logging
from src.heart_disease_prediction.components.model_monitoring import ModelMonitoring



class PredictPipeline:
    def predict(self, features: pd.DataFrame):
        try:
            model = load_object("data_file/model.pkl")
            preprocessor = load_object("data_file/preprocessor.pkl")

            data_scaled = preprocessor.transform(features)
            preds = model.predict(data_scaled)

            monitor = ModelMonitoring()
            monitor.log_predictions(features, preds)

            return preds

        except Exception as e:
            raise CustomException(e, sys)