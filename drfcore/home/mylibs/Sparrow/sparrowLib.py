from .ExpiryDate import ExpiryDate
from time import sleep
from .OptionIndexChain import OptionIndexChain
import pandas as pd
import json,os
import datetime
# from datetime import datetime, time
pd.set_option('display.width',5500)
pd.set_option('display.max_columns',15)
pd.set_option('display.max_rows',30)

BASE = os.path.dirname(os.path.abspath(__file__))
today = datetime.datetime.now().strftime("%Y-%m-%d").upper()
filename = BASE + os.sep + "data" + os.sep +today + "_OptionData.json"

class sparrowLib:
    def __init__(self):
        pass
    
    def maxPain_calculator(self,ce_df,pe_df):
        cedf = ce_df.drop(
            columns=['expiryDate','identifier','askPrice', 'askQty', 'bidprice', 'bidQty', 'underlying', 'totalSellQuantity', 'totalBuyQuantity','pChange','underlyingValue','pchangeinOpenInterest','totalTradedVolume','impliedVolatility','lastPrice','type'],
            axis=1)
        pedf = pe_df.drop(
            columns=['expiryDate','identifier','askPrice', 'askQty', 'bidprice', 'bidQty', 'underlying', 'totalSellQuantity', 'totalBuyQuantity','pChange','underlyingValue','pchangeinOpenInterest','totalTradedVolume','impliedVolatility','lastPrice','type'],
            axis=1)
        df = pd.merge(cedf,pedf,on = "strikePrice")
        df['C'] = df['openInterest_x'].cumsum().mul(df['strikePrice'])
        df['SP'] = df[['openInterest_x', 'strikePrice']].prod(1).cumsum()
        df['D'] = df['openInterest_y'].iloc[::-1].cumsum().mul(df['strikePrice'])
        df['SP2'] = df[['openInterest_y', 'strikePrice']].iloc[::-1].prod(1).cumsum()
        df['CallValue'] = df['C'] - df['SP']
        df['PutValue'] = df['SP2'] - df['D']
        df['Total'] = df['CallValue'] + df['PutValue']
        df1 = df.drop(columns=['C', 'D', 'SP', 'SP2'])
        Maxpain = df1.loc[[df1.loc[df1.Total > 0, 'Total'].idxmin()].pop()]
        return Maxpain
    
    def getDataDF(self,Index,expiryType,mp_df = pd.DataFrame()):
        TICKER = Index
        print("########### Index Received, getDataDF",Index)
        # filename = BASE + os.sep + "data" + os.sep + "FullOptionData.json"
        additional_data = []
        
        
        if expiryType == "W" or expiryType == "Weekly":
            expiryDate = ExpiryDate().get_expiry_date_weekly()
        elif expiryType == "M" or expiryType == "Monthly":
            expiryDate = ExpiryDate().get_expiry_date_monthly(Index)
        else:
            expiryDate = ExpiryDate().get_expiry_date_monthly(Index)
        print("########### expiryDate Received, getDataDF",expiryDate)
        try:
            r = OptionIndexChain().return_optionData(Index)
        except Exception as e:
            
            filename = BASE + os.sep + "data" + os.sep + TICKER + "_"+ today + "_OptionData.json"
            print(f"!!!Server Not Responding with error {e}, Data Read from file {filename}")
            # print(f"File Name trying to Open {filename}")
            with open(filename, 'r') as f:
                r = json.load(f)
        
        if expiryDate:
            ce_values = [data["CE"] for data in r['records']['data'] if "CE" in data and str(data['expiryDate']).lower() == str(expiryDate).lower()]
            pe_values = [data["PE"] for data in r['records']['data'] if "PE" in data and str(data['expiryDate']).lower() == str(expiryDate).lower()]
        else:
            ce_values = [data["CE"] for data in r['records']['data'] if "CE" in data]
            pe_values = [data["PE"] for data in r['records']['data'] if "PE" in data]

        # print("++++++++++++==============")
        # print(ce_values)
        # print(pe_data.head())
        
        ce_data = pd.DataFrame(ce_values)
        pe_data = pd.DataFrame(pe_values)
        
        print("++++++++++++==============")
        print(ce_data.head())
        print(pe_data.head())
        
        # Sort the CE & PE Data
        ce_data = ce_data.sort_values(['strikePrice'])
        pe_data = pe_data.sort_values(['strikePrice'])
        
        ce_data['type'] = 'CE'
        pe_data['type'] = 'PE'
        
 
        ce_data.to_csv("CE_dataFrame.csv")
        
        MaxPain = sparrowLib().maxPain_calculator(ce_data,pe_data)

        required_columns = ['strikePrice', 'expiryDate','identifier' ,'openInterest', 'changeinOpenInterest', 
                            'pchangeinOpenInterest', 'totalSellQuantity','bidQty','bidprice','askQty','askPrice','totalTradedVolume', 'lastPrice', 'change', 
                            'pChange', 'underlyingValue', 'type' ]

        # keep only the required columns
        ce_data = ce_data[required_columns]
        pe_data = pe_data[required_columns]
        
        # add a new column with the current time
        ce_data['current_time'] = datetime.datetime.now().strftime("%H:%M")
        pe_data['current_time'] = datetime.datetime.now().strftime("%H:%M")
        
        # get the top 10 rows based on 'openInterest'
        CE_top_10_OI_strikeprice = ce_data.nlargest(10, 'openInterest')
        PE_top_10_OI_strikeprice = pe_data.nlargest(10, 'openInterest')
        CE_top_10_COI_strikeprice = ce_data.nlargest(10, 'changeinOpenInterest')
        PE_top_10_COI_strikeprice = pe_data.nlargest(10, 'changeinOpenInterest')

        #get the strikePrice with Max Open Interest
        
        
        pe_data['Time'] = datetime.datetime.now().strftime("%H:%M")
        PCR_TradedVolume = pe_data['totalTradedVolume'].sum()/ce_data['totalTradedVolume'].sum()
        pcr_OI = pe_data['openInterest'].sum()/ce_data['openInterest'].sum()
        total_OI_CE = ce_data['openInterest'].sum()
        total_OI_PE = pe_data['openInterest'].sum()
        total_COI_CE = ce_data['changeinOpenInterest'].sum()
        total_COI_PE = pe_data['changeinOpenInterest'].sum()
        
        
        mp_dict = {datetime.datetime.now().strftime("%H:%M"):
                                            {
                                                # 'Time':pe_data['Time'].iloc[-1],
                                                'MaxPain': MaxPain['strikePrice'],
                                                'PCR': round(pcr_OI,2),
                                                "PCR_TradedVol": round(PCR_TradedVolume,2),
                                                "total_OI_CE": total_OI_CE,
                                                "total_OI_PE": total_OI_PE,
                                                "total_COI_CE": total_COI_CE,
                                                "total_COI_PE": total_COI_PE,
                                                "call_decay": ce_data.nlargest(5, 'openInterest', keep='last')['change'].mean(),
                                                "put_decay":  pe_data.nlargest(5, 'openInterest', keep='last')['change'].mean(),
                                                'underlying': pe_data['underlyingValue'].iloc[-1],
                                                'ExpiryDate': expiryDate,
                                                # 'id':pe_data['id'].iloc[-1],
                                            }
        }
        
        mp_dict_transposed_DF = pd.DataFrame(mp_dict).transpose()
        # sort DataFrame based on index
        mp_dict_transposed_DF.sort_index(inplace=True)
        # reset index and move it to columns
        mp_dict_transposed_DF_reset = mp_dict_transposed_DF.reset_index()
        # rename 'index' column
        mp_dict_transposed_DF_reset.rename(columns={'index': 'Time'}, inplace=True)
        # now 'new_column_name' is a column in the DataFrame
        # print(mp_dict_transposed_DF_reset)
        additional_data.append(MaxPain['strikePrice'])
        # print(mp_dict_transposed_DF)
        # mp_df = pd.concat([mp_df,mp_dict_transposed_DF])
        return mp_dict_transposed_DF_reset, CE_top_10_OI_strikeprice , PE_top_10_OI_strikeprice, CE_top_10_COI_strikeprice, PE_top_10_COI_strikeprice
