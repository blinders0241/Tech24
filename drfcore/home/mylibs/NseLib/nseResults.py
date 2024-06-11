import sys
from pathlib import Path
path = Path('C:/SIMPLY_Official/2024/TechHome241/')
sys.path.append(str(path.resolve()))
from drfcore.home.mylibs.NseLib.initiateRequest import *
from bs4 import BeautifulSoup
import pandas as pd
import xml.dom.minidom

pd.set_option('display.width',1200)
pd.set_option('display.max_columns',15)
pd.set_option('display.max_rows',30)

class nseResults:
    def __init__(self):
        self.url = "https://www.nseindia.com/api/corporates-financial-results?index=equities&from_date=11-01-2024&to_date=11-04-2024&fo_sec=true&period=Quarterly"
        
    def buildRL(self,fromdate,todate,equity):
        pass
    def nse_results(self,index="equities",period="Quarterly"):
        if(index=="equities") or (index=="debt") or (index=="sme"):
            if(period=="Quarterly") or (period=="Annual")or (period=="Half-Yearly")or (period=="Others"):
                payload = initiateRequest().establishConnection(self.url)
                return pd.json_normalize(payload)
            else:
                print("Give Correct Period Input")
        else:
            print("Give Correct Index Input")


    def readXBRL(self):
        # Read XML data from a file
        with open(r'C:\SIMPLY_Official\2024\TechHome241\drfcore\home\mylibs\NseLib\rawfile.xml', 'r') as f:
            data = f.read()

        # Parse XML data
        dom = xml.dom.minidom.parseString(data)

        # Pretty print XML data
        pretty_xml = dom.toprettyxml()

        # Write pretty XML data to a file
        with open('output_pretty.xml', 'w') as f:
            f.write(pretty_xml)

    def nsesymbolpurify(self,symbol):
        symbol = symbol.replace('&','%26') #URL Parse for Stocks Like M&M Finance
        return symbol

    def nse_past_results(self,symbol):
        symbol = nseResults().nsesymbolpurify(symbol)
        return initiateRequest().establishConnection('https://www.nseindia.com/api/results-comparision?symbol='+symbol)

results = nseResults().nse_past_results("UPL")
print(results)
# results = nseResults().nse_results()
# nseResults().readXBRL()
# print(results.columns.to_list())
# print(results.head())