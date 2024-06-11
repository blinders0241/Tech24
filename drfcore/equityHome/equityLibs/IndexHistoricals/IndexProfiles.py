from datetime import datetime
import pandas as pd
from pathlib import Path
import os, sys
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

pd.set_option('display.width',1500)
pd.set_option('display.max_columns',225)
pd.set_option('display.max_rows',225)

path = Path(r"drfcore")
# Add the path to sys.path
sys.path.append(str(path.resolve()))
from home.mylibs.AnalyzeBhavcopy.DbConnections import DbConnections

class IndexProfiles:
    def __init__(self):
        self.con = DbConnections().connectToDB()
    
    def returnmyDatabase(self,tablename):
        if tablename == "indexTable":
            df = pd.read_sql_query("SELECT * FROM equityHome_indexhistoricalmodel", self.con)
            return df
        else:
            df = pd.read_sql_query("SELECT * FROM equityHome_stockequitiesmodel", self.con)
            return df
    
    def generateMovingAverages(self,indexName):
        if indexName in ("NIFTY","BANKNIFTY"):
            df = IndexProfiles().returnmyDatabase("indexTable")
        else:
            df = IndexProfiles().returnmyDatabase("stocksTable")
        indexDF = df[df['SYMBOL'].str.match(indexName)]
        indexDF['TOTTRDQTY'] = indexDF['TOTTRDQTY'].astype(float)
        indexDF['TradedQty'] = indexDF['TOTTRDQTY'].div(1000000).round(2)
        indexDF['SMA_9'] = round(indexDF.CLOSE.rolling(9).mean())
        indexDF['SMA_20'] = round(indexDF.CLOSE.rolling(20).mean())
        indexDF['SMA_50'] = round(indexDF.CLOSE.rolling(50).mean())
        indexDF['SMA_100'] = round(indexDF.CLOSE.rolling(100).mean())
        indexDF['SMA_200'] = round(indexDF.CLOSE.rolling(200).mean())
        indexDF['SMA_9'] = indexDF['SMA_9'].round(decimals=2)
        df_movingAverages = indexDF.sort_values(by=['TIMESTAMP'], ascending=False).head(65)
        return df_movingAverages
    
    def T20HighLows(self,indexName):
        nan_value = ''
        indexDF = IndexProfiles().generateMovingAverages(indexName)
        LOW_20D = indexDF['LOW'].head(20).min()
        HIGH_20D = indexDF['HIGH'].head(20).max()
        df_TICKER = indexDF[['LOW', 'HIGH','TIMESTAMP']]
        df_T20_Low =  df_TICKER[df_TICKER.LOW == LOW_20D]
        df_T20_High =  df_TICKER[df_TICKER.HIGH == HIGH_20D]
        return df_T20_Low , df_T20_High
        
    def generateINDEXStretch(self,indexName='NIFTY'):
        if indexName in ("NIFTY","BANKNIFTY"):
            df = IndexProfiles().returnmyDatabase("indexTable")
        else:
            df = IndexProfiles().returnmyDatabase("stocksTable")
        indexDF = df[df['SYMBOL'].str.match(indexName)]
        indexDF['OH'] = indexDF['HIGH']-indexDF['OPEN']
        indexDF['OL'] = indexDF['OPEN']-indexDF['LOW']

        indexDF['Stretch'] = indexDF[['OH', 'OL']].min(axis=1)
        indexDF['FinalStretch'] = indexDF['Stretch'].rolling(10).mean()

        # Calculate the max of 'OH' and 'OL' columns
        indexDF['max_OH_OL'] = indexDF[['OH', 'OL']].max(axis=1)

        # Calculate the percentage move against the closing price
        indexDF['percentMove'] = (indexDF['max_OH_OL'] / indexDF['CLOSE']) * 100
        indexDF['percentMove'] = indexDF['percentMove'].round(decimals=2)

        indexDF = indexDF.sort_values(by=['TIMESTAMP'], ascending=False).head(65)
        cols = ['TIMESTAMP','OH','OL','max_OH_OL','FinalStretch','percentMove']
        df_Stretch = indexDF[cols]
        # print(df_Stretch)
        return df_Stretch

indexNam = "UPL"
df1 = IndexProfiles().generateMovingAverages(indexNam)
df2 = IndexProfiles().generateINDEXStretch(indexNam)
df3,df4 = IndexProfiles().T20HighLows(indexNam)

# print(df1)
# print(df2)
print(df3)
print(df4)