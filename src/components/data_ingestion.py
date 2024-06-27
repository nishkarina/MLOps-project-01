import pandas as pd
import numpy as np
from pathlib import Path
import os
import sys
from src.logger.log_config import logging
from src.exception.exception import customexception
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    # raw, train and test data
    raw_data_path: str = os.path.join("artifacts", "raw.csv")
    train_data_path: str = os.path.join("artifacts", "train.csv")
    test_data_path: str = os.path.join("artifacts", "test.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("data ingestion started..")
        try:
            data = pd.read_csv("https://raw.githubusercontent.com/Pratik-Bhujade/Diamond-Dataset/master/DiamondData.csv")
            logging.info("data imported..")
            os.makedirs(os.path.dirname(os.path.join(self.ingestion_config.raw_data_path)), exist_ok=True)
            data.to_csv(self.ingestion_config.raw_data_path, index=False)
            logging.info("Raw data saved in artifact folder")
            logging.info("Splitting the data into train test..")
            train_data, test_data = train_test_split(data, test_size=0.25, random_state=42)
            train_data.to_csv(self.ingestion_config.train_data_path, index=False)
            test_data.to_csv(self.ingestion_config.test_data_path, index=False)
            logging.info("ingestion of data is completed..")
            return (
                self.ingestion_config.test_data_path,
                self.ingestion_config.train_data_path,
            )

        except Exception as e:
            logging.info("exception raised at Data Ingestion..")
            raise customexception(e, sys)
            


if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()
