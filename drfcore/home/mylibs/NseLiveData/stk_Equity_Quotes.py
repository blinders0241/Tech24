import requests
import pandas as pd
pd.set_option('display.width',3500)
pd.set_option('display.max_columns',35)
pd.set_option('display.max_rows',325)

N50 = url = "https://www.nseindia.com/api/equity-stockIndices?index=NIFTY%2050"
mainurl = 'https://www.nseindia.com/market-data/live-equity-market?symbol=NIFTY%2050'
N200 = 'https://www.nseindia.com/api/equity-stockIndices?index=NIFTY%20200'
auto = 'https://www.nseindia.com/api/equity-stockIndices?index=NIFTY%20AUTO'
BNF = 'https://www.nseindia.com/api/equity-stockIndices?index=NIFTY%20BANK'
energy = 'https://www.nseindia.com/api/equity-stockIndices?index=NIFTY%20ENERGY'
finserv = 'https://www.nseindia.com/api/equity-stockIndices?index=NIFTY%20FINANCIAL%20SERVICES'
fmcg = 'https://www.nseindia.com/api/equity-stockIndices?index=NIFTY%20FMCG'
it = 'https://www.nseindia.com/api/equity-stockIndices?index=NIFTY%20IT'
media = 'https://www.nseindia.com/api/equity-stockIndices?index=NIFTY%20MEDIA'
metal = 'https://www.nseindia.com/api/equity-stockIndices?index=NIFTY%20METAL'
pharma = 'https://www.nseindia.com/api/equity-stockIndices?index=NIFTY%20PHARMA'
realty = 'https://www.nseindia.com/api/equity-stockIndices?index=NIFTY%20REALTY'


class stk_Equity_Quotes:
    def __init__(self):
        pass
    def marketDatafn(self,url):
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'}
        main_url = "https://www.nseindia.com/"
        session = requests.Session()
        response = session.get(main_url, headers=headers)
        cookies = response.cookies
        DataReq = session.get(url, headers=headers, cookies=cookies, timeout=15)
        DataJson = DataReq.json()
        indexData = DataJson['data']
        indexStatus = DataJson['advance']
        indexName = DataJson['name']
        indexDataFetchedOn = DataJson['timestamp']
        return indexData, indexStatus , indexName, indexDataFetchedOn
    
        
    def fetchData(self,url):
        indexData, indexStatus , indexName, indexDataFetchedOn = stk_Equity_Quotes().marketDatafn(url)
        IndexData = pd.json_normalize(indexData)
        IndexStatus = pd.json_normalize(indexStatus)
        return IndexData, IndexStatus , indexName , indexDataFetchedOn
    
    def getEquityDataLive(self,ticker,url):
        nifty50_Equity_Data = stk_Equity_Quotes().fetchData(url)
        nifty50_Eq_Data = nifty50_Equity_Data.reset_index()
        equityData = nifty50_Eq_Data[nifty50_Eq_Data['symbol'] == ticker]
        return equityData

    def stk_EQ_details_dictionary(self,ticker,indices=N50):
        d = stk_EQ_details_dictionary = dict()
        df_1 = stk_Equity_Quotes().getEquityDataLive(ticker,indices)
        df_1 = df_1.set_index(['symbol'])
        # print(df_1.head())
        d['TICKER'] = ticker
        d['LTP'] = df_1['lastPrice'][0]
        d['OPEN'] = df_1['open'][0]
        d['HIGH'] = df_1['dayHigh'][0]
        d['LOW'] = df_1['dayLow'][0]
        d['PrevClose'] = df_1['previousClose'][0]
        d['Chng'] = df_1['change'][0]
        d['pChange'] = df_1['pChange'][0]
        d['yHigh'] = df_1['yearHigh'][0]
        d['yLow'] = df_1['yearLow'][0]
        d['Volume'] = df_1['totalTradedVolume'][0]
        d['perChngeY'] = df_1['perChange365d'][0]
        d['perChngM'] = df_1['perChange30d'][0]
        # print(d)
        return stk_EQ_details_dictionary
    
# stk_Equity_Quotes().fetchData(url)
# stk_Equity_Quotes().stk_EQ_details_dictionary('UPL')