from src.heart_disease_prediction.exception import CustomException
import sys
from src.heart_disease_prediction.logger import logging
from src.heart_disease_prediction.pipelines.training_pipeline import TrainPipeline


if __name__ == "__main__":
    logging.info("Starting the ML project")
    try:
        
        pipeline = TrainPipeline()
        result = pipeline.start_training()
        
    except Exception as e:
        logging.error("An error occurred in the ML project"),
        logging.info("custom error")