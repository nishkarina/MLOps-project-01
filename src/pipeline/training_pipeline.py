import os 
import sys 
import pandas as pd
import numpy as np
from src.exception.exception import customexception
from src.logger.log_config import logging

from src.components.data_transformation import DataTransformation
from practice.src.components.data_ingestion import DataIngestion
from src.components.model_evaluation import ModelEvalluation
from src.components.model_trainer import ModelTrainer

obj = DataIngestion()

train_data_path, test_data_path =obj.initiate_data_ingestion()

data_transformation = DataTransformation()

train_arr, test_arr = data_transformation.initialize_data_transformation(train_data_path, test_data_path)
model_trainer_obj = ModelTrainer()
model_trainer_obj.initiate_model_trainings(train_arr, test_arr)
model_eval_obj = ModelEvalluation()
model_eval_obj.initiate_model_evaluation(train_arr, test_arr)