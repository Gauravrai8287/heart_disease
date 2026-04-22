from src.heart_disease_prediction.logger import logging
from src.heart_disease_prediction.exception import CustomException
import sys
from src.heart_disease_prediction.components.data_ingestion import DataIngestion
from src.heart_disease_prediction.components.data_ingestion import DataIngestionConfig
from src.heart_disease_prediction.components.data_Transformation import DataTransformation, DataTransformationConfig
from src.heart_disease_prediction.components.model_trainer import ModelTrainer, ModelTrainerConfig

class TrainPipeline:
    def start_training(self):
        logging.info("Starting the ML Project")

        try:
            # Data Ingestion
            data_ingestion = DataIngestion()
            train_path, test_path = data_ingestion.initiate_data_ingestion()

            # Data Transformation
            data_transformation = DataTransformation()
            train_arr, test_arr, preprocessor_path = data_transformation.initiate_data_transformation(
                train_path=train_path,
                test_path=test_path
            )

            # Model Training
            model_trainer = ModelTrainer()
            result = model_trainer.initiate_model_trainer(
                train_array=train_arr,
                test_array=test_arr
            )

            return result

        except Exception as e:
            logging.error("An error occurred in the ML project")
            raise CustomException(e, sys)