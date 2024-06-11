
import requests,os,json,sys
import pandas as pd
# print(sys.path)
from .Cookie import Cookie
from .stk_Equity_Quotes import *
BASE = os.path.dirname(os.path.abspath(__file__))
class HeatMapGenerate:
    def __init__(self):
        pass
    def generateHeatMap(request,url):
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
            "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip,deflate"}
        try:
            filename = os.path.join(BASE, 'cookies')
            cookie_dict = json.loads(open(filename).read())
        except:
            print("Error reading cookies")
            cookie_dict = Cookie().get_cookies()
        session = requests.session()
        for cookies in cookie_dict:
            if cookies == 'd':
                session.cookies.set(cookies, cookie_dict[cookies])
        r = session.get(url, headers=header)
        positions = r['data'].json()
        # print(positions)
        return positions

    def generateIndexMap(self,url=url):
        IndexData, IndexStatus , IndexName , IndexDataFetchedOn = stk_Equity_Quotes().fetchData(url)
        print("############## Index Details #####################")
        print (IndexStatus)
        print (IndexName)
        print (IndexDataFetchedOn)
        df = IndexData
        len_df = len(df[(df['priority']<1)])
        len_positive_stks = len(df[(df['pChange']>0)])
        pos_stock_percent = (len_positive_stks / len_df) * 100
        i=0
        stk_data_list =[] ; chngPct_list = [] ; LTP_list = []
        for x in range(i, len_df):
            symbol = df.iloc[x]['symbol']
            ltp = df.iloc[x]['lastPrice']
            chngPercentage = df.iloc[x]['pChange']
            stk_data_list.append(symbol)
            chngPct_list.append(chngPercentage)
            LTP_list.append(ltp)
        change = dict(zip(stk_data_list, chngPct_list))
        value = dict(zip(stk_data_list, LTP_list))
        
        # Create a DataFrame from the dictionaries
        df = pd.DataFrame({'Symbol': list(change.keys()), '% Change': list(change.values()), 'Last Traded Value': list(value.values())})

        # Check the mapping
        for index, row in df.iterrows():
            symbol = row['Symbol']
            if change[symbol] != row['% Change'] or value[symbol] != row['Last Traded Value']:
                print(f"Error in mapping for symbol {symbol}")
        
        print(df.head())
        return df
# HeatMapGenerate().generateIndexMap(N50)