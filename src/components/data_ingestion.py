""" 
related to reading the data 

dataclass is used to create class variables
if only defining variables, use dataclass
    otherwise use __init__

"""

import os
import sys
from src.exception import CustomException
from src.logger import logging

import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    """ this function is used for input """
    train_data_path: str = os.path.join('artifacts', "train.csv")
    test_data_path: str = os.path.join('artifacts', "test.csv")
    raw_data_path: str = os.path.join('artifacts', "raw.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered Data Ingestion component")
        try:
            df = pd.read_csv('notebook\data\stud.csv')
            logging.info("Read the dataset")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path, index= False, header= True)
            logging.info("Saved the raw data")


            train_set, test_set = train_test_split(df, test_size = 0.2, random_state = 38)

            train_set.to_csv(self.ingestion_config.train_data_path, index= False, header= True)
            test_set.to_csv(self.ingestion_config.test_data_path, index= False, header= True)
            logging.info("Ingestion of data is completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,

            )

        except Exception as e:
            raise CustomException(e, sys)
        
if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()



