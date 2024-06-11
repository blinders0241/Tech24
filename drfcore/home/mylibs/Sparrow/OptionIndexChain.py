import requests
import os,json
from .Cookie import *
import datetime

BASE = os.path.dirname(os.path.abspath(__file__))
today = datetime.datetime.now().strftime("%Y-%m-%d").upper()
# filename = BASE + os.sep + "data" + os.sep +today + "_OptionData.json"

class OptionIndexChain:
    def __init__(self):
        pass

    def return_optionData(self,TICKER):
        if TICKER in ("NIFTY","BANKNIFTY"):
            url = "https://nseindia.com/api/option-chain-indices?symbol=" + TICKER
        else:
            url = "https://www.nseindia.com/api/option-chain-equities?symbol=" + TICKER
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
            "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip,deflate"}
        try:
            filename = os.path.join(BASE, 'cookies.txt')
            cookie_dict = json.loads(open(filename).read())
        except:
            print("Error reading cookies")
            cookie_dict = Cookie().get_cookies()
        session = requests.session()
        for cookies in cookie_dict:
            if cookies == 'd':
                session.cookies.set(cookies, cookie_dict[cookies])
        optionData = session.get(url, headers=header).json()
        try:
            
            if optionData:
                filename = BASE + os.sep + "data" + os.sep + TICKER + "_"+ today + "_OptionData.json"
                with open(filename, 'w') as f:
                    json.dump(optionData, f, ensure_ascii=False)
        except Exception as e:
            print(e,"WRITEERROR")
        return optionData
    

# OptionIndexChain().return_optionData()