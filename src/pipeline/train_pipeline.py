import sys
import os
from src.exception import CustomException
from src.logger import logging
from src.componenets.data_ingestion import DataIngestion
from src.componenets.data_transformation import DataTransformation
from src.componenets.model_trainer import ModelTrainer

class TrainPipeline:
    def __init__(self):
        pass

    def train(self):
        try:
            logging.info("Training pipeline started")
            data_ingestion = DataIngestion()
            train_path, test_path = data_ingestion.initiate_data_ingestion()

            data_transformation = DataTransformation()
            train_arr, test_arr, preprocessor_path = data_transformation.initiate_data_transformation(train_path, test_path)

            model_trainer = ModelTrainer()
            r2_score = model_trainer.initiate_model_trainer(train_arr, test_arr, preprocessor_path)

            logging.info(f"Training completed with R2 score: {r2_score}")
            return r2_score
        except Exception as e:
            raise CustomException(e, sys)

if __name__ == "__main__":
    train_pipeline = TrainPipeline()
    train_pipeline.train()
