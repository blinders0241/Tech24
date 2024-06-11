import os,time,datetime
import sqlite3
import pandas as pd
from ..GlobsterHome import *
BASE = os.path.dirname(os.path.abspath(__file__))

class DbConnections():

    def connectToDB(self):
        # dbFilePath = os.path.join(BASE,"../../../db.sqlite3")
        connection = sqlite3.connect(GlobsterHome().SQL_URL + r"\db.sqlite3")
        # df = pd.read_sql_query("SELECT * FROM csvupload_Dashboard", con)
        return connection