import os
import sys
import pickle
from dataclasses import dataclass
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, f1_score, precision_score, recall_score
from src.heart_disease_prediction.logger import logging
from src.heart_disease_prediction.exception import CustomException
from src.heart_disease_prediction.utils import save_object
@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join('data_file', 'model.pkl')

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self, train_array, test_array):
        try:
            logging.info("Splitting training and testing input data")
            X_train, y_train, X_test, y_test = (
                train_array[:, :-1],
                train_array[:, -1],
                test_array[:, :-1],
                test_array[:, -1]
            )
            model = XGBClassifier( n_estimators=200, learning_rate=0.01, max_depth=3,subsample=1.0 ,colsample_bytree=0.8, random_state=42)
            model.fit(X_train, y_train)

            logging.info("Predicting the test set results")
            y_pred = model.predict(X_test)

            accuracy = accuracy_score(y_test, y_pred)
            f1 = f1_score(y_test, y_pred,average='weighted')
            precision = precision_score(y_test, y_pred,average='weighted')
            recall = recall_score(y_test, y_pred,average='weighted')

            print( f"Accuracy: {accuracy}")
            print( f"F1 Score: {f1}")
            print( f"Precision: {precision}")
            print( f"Recall: {recall}")
            logging.info(f"Accuracy: {accuracy}")
            logging.info(f"F1 Score: {f1}")
            logging.info(f"Precision: {precision}")
            logging.info(f"Recall: {recall}")

            save_object(
            file_path=self.model_trainer_config.trained_model_file_path,
            obj=model
          )

            return accuracy, f1, precision, recall
            logging.info(f"Mean Absolute Error: {mae}")
            logging.info(f"Mean Squared Error: {mse}")

            save_object(
            file_path=self.model_trainer_config.trained_model_file_path,
            obj=model
          )

            return r2_square

        except Exception as e:
            raise CustomException(e, sys)