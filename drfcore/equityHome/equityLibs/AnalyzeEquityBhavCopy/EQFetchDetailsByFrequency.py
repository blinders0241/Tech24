from datetime import datetime
import pandas as pd
from home.mylibs.AnalyzeBhavcopy.DbConnections import DbConnections
from home.mylibs.AnalyzeBhavcopy.StocksMapper import *


class EQFetchDetailsByFrequency:
    def __init__(self):
        self.con = DbConnections().connectToDB()
        # self.symbol_map = {}

    def detailsDaily(self):
        mapper = StockMapper()
        mapper.process_files()
        df = pd.read_sql_query("SELECT * FROM equityHome_stockequitiesmodel", self.con)
        # Sort by TimeStamp
        df_sorted = df.sort_values(by='TIMESTAMP', ascending=False)
        latest_timestamp = df_sorted.iloc[0]['TIMESTAMP']
        df = df[df['TIMESTAMP'] == latest_timestamp]
        df['classifiedLists'] = df['SYMBOL'].map(mapper.symbol_map)
        df['freq']="D"
        # print(df.head())
        return df
    
    # def indexdetailsDaily(self):
    #     df = pd.read_sql_query("SELECT * FROM home_stockfuturesmodel", self.con)
    #     # Sort by TimeStamp
    #     df_sorted = df.sort_values(by='TIMESTAMP', ascending=False)
    #     latest_timestamp = df_sorted.iloc[0]['TIMESTAMP']
    #     df_filtered = df[df['TIMESTAMP'] == latest_timestamp]
    #     index_Futures_List = ['BANKNIFTY','NIFTY']
    #     df = df_filtered[df_filtered['SYMBOL'].isin(index_Futures_List) ]
    #     df = df_filtered[df_filtered['SYMBOL'].isin(index_Futures_List) ]
    #     df['pChange'] = (((df['CLOSE'] - df['OPEN'])/df['OPEN'])*100).round(2)
    #     df['pVolume'] = (df['VOLUME'] / df['VOLUME'].max() * 100).round(2)
    #     df['freq']="D"
    #     # print(df.head())
    #     return df
    
    # def detailsWeekly(self):
    #     weekly_df = pd.read_sql_query("SELECT \
    #         SYMBOL, date(TIMESTAMP, 'weekday 0', '-6 days') as Week,  \
    #         min(case when rn = 1 then OPEN end) as OPEN,    \
    #         max(HIGH) as HIGH,    \
    #         min(LOW) as LOW,\
    #         max(case when rn = 1 then CLOSE end) as CLOSE,  \
    #         sum(VOLUME) as VOLUME, \
    #         sum(OPEN_INT) as OPEN_INT,  \
    #         sum(CHG_IN_OI) as CHG_IN_OI  \
    #         FROM \
    #         (SELECT *, row_number() over(partition by SYMBOL, date(TIMESTAMP, 'weekday 0', '-6 days') \
    #         order by TIMESTAMP desc) as rn    FROM home_stockfuturesmodel  ) \
    #         GROUP BY SYMBOL, Week \
    #         ORDER BY SYMBOL, Week ;", self.con)

    #     # Assuming df is your DataFrame
    #     weekly_df['Week'] = pd.to_datetime(weekly_df['Week'])

    #     # Set the DataFrame index to be the timestamp
    #     weekly_df.set_index('Week', inplace=True)
        
    #     # # Calculate the WeeklyChange
    #     weekly_df['WeeklyChange'] = weekly_df.groupby('SYMBOL')['CLOSE'].diff()
    #     weekly_df['pChange'] = ((weekly_df['WeeklyChange'] / weekly_df['OPEN'])*100).round(2)
    #     weekly_df['pVolume'] = (weekly_df['VOLUME'] / weekly_df['VOLUME'].max() * 100).round(2)
        
    #     # Reset the index
    #     weekly_df.reset_index(inplace=True)

    #     # Add the WeekNumber
    #     weekly_df['WeekNumber'] = weekly_df['Week'].dt.isocalendar().week
    #     # Get the current date
    #     now = datetime.now()
    #     # Get the week number
    #     week_num = now.isocalendar()[1]
    #     print(f"The current week number is {week_num}")
    #     df_filtered = weekly_df[weekly_df['WeekNumber'] == week_num]
    #     df_filtered['freq']="W"
        
    #     #Exlude Index Futures        
    #     index_Futures_List = ['BANKNIFTY','FINNIFTY','MIDCPNIFTY','NIFTY','IDEA']
    #     df = df_filtered[~df_filtered['SYMBOL'].isin(index_Futures_List) ]
    #     print(df.columns.to_list())
    #     print(df.head())
        
    #     # Return the DataFrame Weekly
    #     return df
    
    # def indexdetailsWeekly(self):
    #     weekly_df = pd.read_sql_query("SELECT \
    #         SYMBOL, date(TIMESTAMP, 'weekday 0', '-6 days') as Week,  \
    #         min(case when rn = 1 then OPEN end) as OPEN,    \
    #         max(HIGH) as HIGH,    \
    #         min(LOW) as LOW,\
    #         max(case when rn = 1 then CLOSE end) as CLOSE,  \
    #         sum(VOLUME) as VOLUME, \
    #         sum(OPEN_INT) as OPEN_INT,  \
    #         sum(CHG_IN_OI) as CHG_IN_OI  \
    #         FROM \
    #         (SELECT *, row_number() over(partition by SYMBOL, date(TIMESTAMP, 'weekday 0', '-6 days') \
    #         order by TIMESTAMP desc) as rn    FROM home_stockfuturesmodel  ) \
    #         GROUP BY SYMBOL, Week \
    #         ORDER BY SYMBOL, Week ;", self.con)

    #     # Assuming df is your DataFrame
    #     weekly_df['Week'] = pd.to_datetime(weekly_df['Week'])

    #     # Set the DataFrame index to be the timestamp
    #     weekly_df.set_index('Week', inplace=True)
    #      #Exlude Index Futures 
    #     index_Futures_List = ['BANKNIFTY','NIFTY']
    #     weekly_df = weekly_df[weekly_df['SYMBOL'].isin(index_Futures_List) ]
    #     # # Calculate the WeeklyChange
    #     weekly_df['WeeklyChange'] = weekly_df.groupby('SYMBOL')['CLOSE'].diff()
    #     weekly_df['pChange'] = ((weekly_df['WeeklyChange'] / weekly_df['OPEN'])*100).round(2)
    #     weekly_df['pVolume'] = (weekly_df['VOLUME'] / weekly_df['VOLUME'].max() * 100).round(2)
        
    #     # Reset the index
    #     weekly_df.reset_index(inplace=True)

    #     # Add the WeekNumber
    #     weekly_df['WeekNumber'] = weekly_df['Week'].dt.isocalendar().week
    #     # Get the current date
    #     now = datetime.now()
    #     # Get the week number
    #     week_num = now.isocalendar()[1]
    #     print(f"The current week number is {week_num}")
    #     df_filtered = weekly_df[weekly_df['WeekNumber'] == week_num]
    #     df_filtered['freq']="W"
        
    #     # Return the DataFrame Weekly
    #     return df_filtered

    # def detailsMonthly(self):
    #     monthly_df = pd.read_sql_query("""
    #     SELECT 
    #         SYMBOL, 
    #         strftime('%Y-%m', TIMESTAMP) as Month,  
    #         min(case when rn = 1 then OPEN end) as OPEN,    
    #         max(HIGH) as HIGH,    
    #         min(LOW) as LOW,
    #         max(case when rn = 1 then CLOSE end) as CLOSE,  
    #         sum(VOLUME) as VOLUME, 
    #         sum(OPEN_INT) as OPEN_INT,  
    #         sum(CHG_IN_OI) as CHG_IN_OI  
    #     FROM 
    #         (SELECT *, row_number() over(partition by SYMBOL, strftime('%Y-%m', TIMESTAMP) 
    #         order by TIMESTAMP desc) as rn    
    #         FROM home_stockfuturesmodel) 
    #     GROUP BY SYMBOL, Month 
    #     ORDER BY SYMBOL, Month;
    #     """, self.con)

    #     # print(monthly_df.head()) 

    #     # Assuming df is your DataFrame
    #     monthly_df['Month'] = pd.to_datetime(monthly_df['Month'])

    #     # Set the DataFrame index to be the timestamp
    #     monthly_df.set_index('Month', inplace=True)

    #     # # Calculate the MonthlyChange
    #     # monthly_df['MonthlyChange'] = monthly_df.groupby('SYMBOL')['CLOSE'].diff()
        
    #      # # Calculate the MonthlyChange
    #     monthly_df['mChange'] = monthly_df.groupby('SYMBOL')['CLOSE'].diff()
    #     monthly_df['pChange'] = ((monthly_df['mChange']/monthly_df['OPEN'])*100).round(2)
    #     monthly_df['pVolume'] = (monthly_df['VOLUME'] / monthly_df['VOLUME'].max() * 100).round(2)


    #     # print(monthly_df)

    #     # Reset the index
    #     monthly_df.reset_index(inplace=True)

    #     # Add the MonthNumber
    #     monthly_df['MonthNumber'] = monthly_df['Month'].dt.month
    #     # Get the current date
    #     now = datetime.now()

    #     # Get the Month number
    #     Month_num = str(now.month).zfill(2)
    #     date_str = now.strftime('%Y-%m') + "-" + str(Month_num)

    #     print(f"The current Month number is {date_str}")
    #     df_filtered = monthly_df[monthly_df['Month'] == date_str]
    #     df_filtered['freq']="M"
        
    #     index_Futures_List = ['BANKNIFTY','FINNIFTY','MIDCPNIFTY','NIFTY','IDEA']
    #     df = df_filtered[~df_filtered['SYMBOL'].isin(index_Futures_List) ]
        
    #     # Display the DataFrame
    #     return df

    # def indexdetailsMonthly(self):
    #     monthly_df = pd.read_sql_query("""
    #     SELECT 
    #         SYMBOL, 
    #         strftime('%Y-%m', TIMESTAMP) as Month,  
    #         min(case when rn = 1 then OPEN end) as OPEN,    
    #         max(HIGH) as HIGH,    
    #         min(LOW) as LOW,
    #         max(case when rn = 1 then CLOSE end) as CLOSE,  
    #         sum(VOLUME) as VOLUME, 
    #         sum(OPEN_INT) as OPEN_INT,  
    #         sum(CHG_IN_OI) as CHG_IN_OI  
    #     FROM 
    #         (SELECT *, row_number() over(partition by SYMBOL, strftime('%Y-%m', TIMESTAMP) 
    #         order by TIMESTAMP desc) as rn    
    #         FROM home_stockfuturesmodel) 
    #     GROUP BY SYMBOL, Month 
    #     ORDER BY SYMBOL, Month;
    #     """, self.con)

    #     # Assuming df is your DataFrame
    #     monthly_df['Month'] = pd.to_datetime(monthly_df['Month'])

    #     # Set the DataFrame index to be the timestamp
    #     monthly_df.set_index('Month', inplace=True)

    #     index_Futures_List = ['BANKNIFTY','NIFTY']
    #     monthly_df = monthly_df[monthly_df['SYMBOL'].isin(index_Futures_List) ]
        
    #     # # Calculate the MonthlyChange
    #     monthly_df['mChange'] = monthly_df.groupby('SYMBOL')['CLOSE'].diff()
    #     monthly_df['pChange'] = ((monthly_df['mChange']/monthly_df['OPEN'])*100).round(2)
    #     monthly_df['pVolume'] = (monthly_df['VOLUME'] / monthly_df['VOLUME'].max() * 100).round(2)


    #     # Reset the index
    #     monthly_df.reset_index(inplace=True)

    #     # Add the MonthNumber
    #     monthly_df['MonthNumber'] = monthly_df['Month'].dt.month
    #     # print(monthly_df)
    #     # Get the current date
    #     now = datetime.now()

    #     # Get the Month number
    #     Month_num = str(now.month).zfill(2)
    #     date_str = now.strftime('%Y-%m') + "-" + str(Month_num)

    #     print(f"The current Month number is {date_str}")
    #     df_filtered = monthly_df[monthly_df['Month'] == date_str]
    #     df_filtered['freq']="M"
        

        
    #     # Display the DataFrame
    #     return df_filtered

    def get_lists(self, symbol):
        return self.symbol_map.get(symbol, [])


# FetchDetailsByFrequency().detailsWeekly()