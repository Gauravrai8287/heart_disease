import os
import sys
from src.heart_disease_prediction.exception import CustomException
from src.heart_disease_prediction.logger import logging
import pandas as pd
import pymysql
from dotenv import load_dotenv
import pickle
import numpy as np
load_dotenv()

host=os.getenv('host')
user=os.getenv('user')
password =os.getenv('password')
db=os.getenv('db')

def read_sql_data():
    logging.info("Reading data from sql database")
    try:
        mydb = pymysql.connect(host=host, user=user, password=password, db=db)

        logging.info('Connection to database is successful',mydb)
        df=pd.read_sql('SELECT * FROM disease', con=mydb)
        return df
    except Exception as ex:
        raise CustomException(ex, sys)
def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'wb') as file_obj:
            pickle.dump(obj, file_obj)
    except Exception as e:
        raise CustomException(e, sys)
def load_object(file_path):
    try:
        print(f"Loading file: {file_path}")
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)
    except Exception as e:
        print(f"Error loading: {file_path}")
        raise CustomException(e, sys)