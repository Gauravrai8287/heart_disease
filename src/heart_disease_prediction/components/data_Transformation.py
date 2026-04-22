import sys
import os
from dataclasses import dataclass
import numpy as np
import pandas as pd
from sklearn.preprocessing import  StandardScaler
from sklearn.impute import SimpleImputer
from src.heart_disease_prediction.exception import CustomException
from src.heart_disease_prediction.logger import logging
from src.heart_disease_prediction.utils import  save_object
from src.heart_disease_prediction.components.data_ingestion import DataIngestion
@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path: str = os.path.join('data_file', 'preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self,df):
        # This function is responsible for data transformation
        try:
            logging.info("Data Transformation initiated")
            
            preprocessor =  StandardScaler()
                         
            return preprocessor
        
        except Exception as e:
            logging.info("Error in Data Transformation")
            raise CustomException(e, sys)
        
    def initiate_data_transformation(self, train_path, test_path):
        try:
            logging.info("Data Transformation initiated")
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            logging.info("Read train and test data completed")
            
            logging.info("Obtaining preprocessing object")
            
            target_column_name = 'target'
            # divide the train data into input feature and target feature
            input_feature_train_df = train_df.drop(columns=[target_column_name])
            target_feature_train_df = train_df[target_column_name]
            # divide the test data into input feature and target feature
            input_feature_test_df = test_df.drop(columns=[target_column_name])
            target_feature_test_df = test_df[target_column_name]
            logging.info("Applying preprocessing object on training and testing data")
            #PASS TRAIN INPUT DATA HERE
            preprocessor_obj = self.get_data_transformer_object(input_feature_train_df)

            input_feature_train_arr = preprocessor_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr =  preprocessor_obj.transform(input_feature_test_df)
             # Combine input + target
            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]
            logging.info("Saved preprocessing object")
            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessor_obj
            )
            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path
            )
        except Exception as e:
            logging.info("Error in Data Transformation")
            raise CustomException(e, sys)
                