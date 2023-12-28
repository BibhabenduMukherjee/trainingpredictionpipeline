import os
import sys
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import pandas as pd
from dotenv import load_dotenv
import pymysql
load_dotenv()

host = os.getenv("host")
user = os.getenv("user")
passw = os.getenv("password")
db = os.getenv("db")

def read_sql_data():
    logging.info("Reading Sql data started")
    try :
        mydb = pymysql.connect(host=host, user=user , password=passw , db=db)
        logging.info("connected sql data base" , mydb)
        df = pd.read_sql_query('Select * from students',mydb)
        df.head()
        return df
    except Exception as e :
        raise CustomException(e,sys)

