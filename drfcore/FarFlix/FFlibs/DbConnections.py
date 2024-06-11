import os,time,datetime
import sqlite3
import pandas as pd
from .Globster import *
BASE = os.path.dirname(os.path.abspath(__file__))

class DbConnections():

    def connectToDB(self):
        dbFilePath = Globster().SQL_URL +os.sep + "db.sqlite3"
        assert os.path.exists(dbFilePath), "The file doesn't exist"
        connection = sqlite3.connect(dbFilePath)
        # df = pd.read_sql_query("SELECT * FROM csvupload_Dashboard", con)
        return connection