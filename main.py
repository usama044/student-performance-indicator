from src.components.data_ingestion import DataIngestion, DataIngestionConfig


if __name__=="__main__":
    data_ingestion = DataIngestion()
    train_data, test_data = data_ingestion.initiate_data_ingestion()
    