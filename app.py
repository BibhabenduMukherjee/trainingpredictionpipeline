from src.mlproject.logger import logging
from src.mlproject.components.data_injestion import DataIngestion
from src.mlproject.exception import CustomException
import sys
if __name__ == '__main__':
   
    logging.info("The Execution is started")
    try:
        data_injestion = DataIngestion()
        data_injestion.initiate_data_ingestion()
    except Exception as e:
        logging.error("Custom error")
        raise CustomException(e,sys)

      