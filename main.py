from src.components.data_ingestion import DataIngestion, DataIngestionConfig
from src.components.data_transformation import DataTransformation, DataTransformationConfig
from src.components.model_trainer import ModelTrainer, ModelTrainerConfig
from src.exception import CustomException
import sys


if __name__=="__main__":
    try:
        data_ingestion = DataIngestion()
        train_data, test_data = data_ingestion.initiate_data_ingestion()

        data_transformation = DataTransformation()
        train_arr, test_arr, _ = data_transformation.initiate_data_transformation(train_data, test_data)

        model_trainer = ModelTrainer()
        results = model_trainer.initiate_model_trainer(train_arr, test_arr)
        print(results)

        
    except Exception as e:
        raise CustomException(e, sys)