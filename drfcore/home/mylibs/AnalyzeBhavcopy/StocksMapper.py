import os
import pandas as pd
from .DbConnections import DbConnections
from ..GlobsterHome import *
# path2directory = r"C:\SIMPLY_Official\2024\DRF\drfcore\home\mylibs\data\Mapper\\"
fullGlobalEquityList = []
equityList =[]
duplicates = []
excludeList = ['NIFTY MIDCAP 100', 'NIFTY MIDCAP 50', 'NIFTY NEXT 50', 'NIFTY OIL & GAS', 'NIFTY PHARMA', \
    'NIFTY PRIVATE BANK', 'NIFTY PSU BANK', 'PSB', 'NIFTY REALTY','NIFTY 100','NIFTY-100', 'NIFTY-200', 'NIFTY-50', \
        'NIFTY-500', 'NIFTY-BANK', 'NIFTY-FINANCIAL-SERVICES', 'NIFTY-FINANCIAL-SERVICES-25_50', 'NIFTY-LARGEMIDCAP-250', 'NIFTY-PRIVATE-BANK']

class StockMapper:
    def __init__(self, directory=GlobsterHome().path2directory):
        self.directory = directory
        self.symbol_map = {}

    def process_files(self):
        for filename in os.listdir(self.directory):
            if filename.endswith('.csv'):
                # Trim the prefix & suffix of the filename
                trimmed_name = filename.replace('MW-', '').replace('-16-Jan-2024', '')
                # print(trimmed_name)
                # Read the CSV file
                df = pd.read_csv(os.path.join(self.directory, filename))
                df.columns = df.columns.str.replace('\n', ' ')
                # print(df.columns.to_list())
                df.columns = df.columns.str.strip(' ')
                df.columns = df.columns.str.replace("\r", "")
                df.columns = df.columns.str.replace(" ", "")
                # print(df.columns)
                # print(df.head())
                # Append the rows under 'SYMBOL' column to the list
                symbols = df['SYMBOL'].tolist()
                # Update the symbol_map
                for symbol in symbols:
                    if symbol not in self.symbol_map:
                        self.symbol_map[symbol] = []

                    self.symbol_map[symbol].append(trimmed_name.replace('.csv',''))
                

    def get_lists(self, symbol):
        return self.symbol_map.get(symbol, [])
    
    # Removes the sublist, if it exists and returns a new list, otherwise returns the old list.
    # Returns that starting and ending point (index) of the sublist, if it exists, otherwise 'None'.

    def findSublist(self,subList, inList):
        subListLength = len(subList)
        for i in range(len(inList)-subListLength):
            if subList == inList[i:i+subListLength]:
                return (i, i+subListLength)
        return None

    def removeSublistFromList(self,subList, inList):
        indices = StockMapper().findSublist(subList, inList)
        if not indices is None:
            return inList[0:indices[0]] + inList[indices[1]:]
        else:
            return inList
    
    def get_equity_names(self):
        
        for equity,map in self.symbol_map.items():
            if " " in equity:
                continue
            fullGlobalEquityList.append(equity)
        equityList = StockMapper().removeSublistFromList(excludeList,fullGlobalEquityList)
        if len(equityList) != len(set(equityList)):
            print("The List Has Duplicates")
        return equityList


