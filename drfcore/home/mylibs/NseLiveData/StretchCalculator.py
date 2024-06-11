from datetime import datetime, timedelta
import datetime, calendar, os
import requests,json
import pandas as pd
from pandas import json_normalize
import sys,time
sys.path.append(r"C:\SIMPLY_Official\\2024\\TechHome241\drfcore\\")
from home.mylibs.NseLiveData.Cookie import Cookie

BASE = os.path.dirname(os.path.abspath(__file__))
stretchdir = r"C:\SIMPLY_Official\2024\TechHome241\drfcore\home\mylibs\data\StretchData\\"
stretch = []
pd.set_option('display.width',1500)
pd.set_option('display.max_columns',225)
pd.set_option('display.max_rows',225)
pd.options.mode.chained_assignment = None  # default='warn'

hist_url = 'https://www1.nseindia.com/live_market/dynaContent/live_analysis/most_active/bankNiftyHistory.json'
class StretchCalc:
    def __init__(self):
        self.file_path = stretchdir + os.sep + "index_data.csv"
        pass

    def Index_Mean(self,index):
        for _ in range(3):
            try:
                index_history_df = StretchCalc().fetchIndexBase(index)
                if index_history_df is not None:
                    break  # Exit the loop if successful and not None
            except Exception as e:
                print(f"Error encountered: {e}")
                time.sleep(0.8)  # Wait before retrying
        else:
            print("Failed to fetch index data after 3 retries or received None. Exiting.")
            sys.exit(1)
        return index_history_df.tail(10)
    
    def calculateMean(self,index):
        stockDtl_data = StretchCalc().Index_Mean(index)
        stockDtl_data['Open'] = stockDtl_data['EOD_OPEN_INDEX_VAL'].astype(float)
        stockDtl_data['Low'] = stockDtl_data['EOD_LOW_INDEX_VAL'].astype(float)
        stockDtl_data['High'] = stockDtl_data['EOD_HIGH_INDEX_VAL'].astype(float)
        stockDtl_data['OpenLow'] = stockDtl_data['Open'] - stockDtl_data['Low']
        stockDtl_data['HighOpen'] = stockDtl_data['High'] - stockDtl_data['Open']
        stockDtl_data['min'] = stockDtl_data[['OpenLow', 'HighOpen']].min(axis=1)
        mean = round(stockDtl_data['min'].mean(), 2)
        return mean
    
    def writeMeanValue(self, index_name):
        today = datetime.datetime.now().strftime("%Y-%m-%d").upper()

        # Check if the file exists
        if not os.path.exists(self.file_path):
            df = pd.DataFrame(columns=["DateField", "IndexName", "Mean"])
            mean_value = StretchCalc().calculateMean(index_name)
            new_row = {"DateField": today, "IndexName": index_name, "Mean": mean_value}
            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
            df.to_csv(self.file_path, index=False)
            df.sort_values(by="DateField", ascending=False, inplace=True)
            return df.iloc[0]
        else:
            print(f"Reading from File {self.file_path} {index_name}")
            df = pd.read_csv(self.file_path)
            df = df.sort_index(ascending=False)
            print(df)
            first_row = df.iloc[0]
            second_row = df.iloc[1]
            print("### display from else loop : File Exists!")
            print(first_row)
            print(second_row)

            # Create a switch-like dictionary for index_name mapping
            index_mapping = {
                first_row['IndexName']: first_row,
                second_row['IndexName']: second_row
            }

            if first_row['DateField'] == second_row['DateField'] and first_row['DateField'] == today:
                if index_name in index_mapping:
                    print("MATCHED")
                    df = df.head(2)
                    selected_rows = df.loc[df['IndexName'] == 'BANKNIFTY']
                    mean_value = selected_rows['Mean'].iloc[0]
                    print(mean_value)
                    return mean_value
            else:
                print("Didn't match")
                mean_value = StretchCalc().calculateMean(index_name)
                new_row = {"DateField": today, "IndexName": index_name, "Mean": mean_value}
                df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
                df.to_csv(self.file_path, index=False)
                df = df.sort_index(ascending=False)
                return df.iloc[0]

    
    
    def from_to_date(self):
        date_1 = datetime.date.today()
        # Get the current hour
        current_hour = datetime.datetime.now().hour
        # Check if the current hour is less than 19 (7:00 PM)
        if current_hour < 19:
            effectiveDay = date_1
        else:
            effectiveDay = (date_1 - datetime.timedelta(days=1))
        # to_date = datetime.date.today().strftime('%d-%m-%Y')
        to_date = effectiveDay.strftime('%d-%m-%Y')
        print("todate",to_date)
        from_date = (effectiveDay - timedelta(days=30)).strftime('%d-%m-%Y')
        print(from_date)
        return from_date, to_date

    def fetchIndexBase(self,index="NIFTY"):
        try:
            fromdate, todate = StretchCalc.from_to_date(self)
            if index == 'NIFTY':
                index = 'NIFTY%2050'
            else:
                index = 'NIFTY%20BANK'
            url = "https://www.nseindia.com/api/historical/indicesHistory?indexType="+index+"&from="+fromdate+"&to="+todate
            # url = "https://www1.nseindia.com/products/dynaContent/equities/indices/historicalindices.jsp?indexType="+index+"&fromDate=" + fromdate + "&toDate=" + todate
            print(url)
            header = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
                "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip,deflate"}
            try:
                filename = r"C:\SIMPLY_Official\2024\TechHome241\cookies.txt"
                cookie_dict = json.loads(open(filename).read())
            except:
                print("Error reading cookies")
                cookie_dict = Cookie().get_cookies()
            session = requests.session()
            for cookies in cookie_dict:
                # print(cookies)
                if cookies == 'd':
                    session.cookies.set(cookies, cookie_dict[cookies])
            r = session.get(url, headers=header)
            dataR = r.json()  # Convert the Response object to a JSON object
            records = dataR['data']['indexCloseOnlineRecords']
            # Convert the list into a pandas DataFrame
            df = pd.DataFrame(records)
            return df
            # return dataR['data']
        except Exception as e:
            print(f"Error while making request: {e}")

# StretchCalc().writeMeanValue("NIFTYBANK")
# StretchCalc().writeMeanValue("NIFTY")
