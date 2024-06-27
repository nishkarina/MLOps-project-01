from src.utils.utils import save_object, evaluate_model
from sklearn.linear_model import LinearRegression, ElasticNet, Ridge, Lasso
from dataclasses import dataclass
import os, sys
from src.exception.exception import customexception
from src.logger.log_config import logging
from pathlib import Path

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("artifact", "model.pkl")

class ModelTrainer:
    
    def __init__(self):
            self.model_trainer_config = ModelTrainerConfig()
        
    def initiate_model_trainings(self, train_array, test_array):
        try:
            logging.info("Splitting Dependent and Independent variables from train and test data")
            X_train,X_test,y_train,y_test = (
                 train_array[:,:-1],
                 test_array[:,:-1],
                 train_array[:,-1],
                 test_array[:,-1]
            )
            models = {
                "LinearRegression":LinearRegression(),
                "ElasticNet": ElasticNet(),
                "Lasso": Lasso(),
                "Ridge": Ridge(),
                }
            model_report: dict=evaluate_model(X_train, X_test, y_train, y_test)
            print(model_report)
            print("\n***********************************************\n")
            logging.info(f"Model Report: {model_report}")

            best_model_score = max(sorted(model_report.values()))

            best_model_name = list(model_report.keys())[list(model_report.values()).index(best_model_score)]
            best_model = models[best_model_name]

            print(f"Best Model name: {best_model}, R2 score: {best_model_score}")
            print("\n***************************************************\n")
            logging.info(f"Best Model name: {best_model}, R2 Score: {best_model_score}")

            save_object(file_path=self.model_trainer_config.trained_model_file_path,
                        obj = best_model)



        except Exception as e:
            logging.info("Exception occured at Model Training")
            raise customexception(e, sys)