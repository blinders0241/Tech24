from datetime import datetime
import pandas as pd
from .DbConnections import DbConnections
from .StocksMapper import *
from equityHome.equityLibs.Globster import *

pd.set_option('display.width',1200)
pd.set_option('display.max_columns',15)
pd.set_option('display.max_rows',30)


class FetchDetailsByFrequency:
    def __init__(self):
        self.con = DbConnections().connectToDB()
        # self.symbol_map = {}

    def detailsDaily(self):
        mapper = StockMapper()
        mapper.process_files()
        df = pd.read_sql_query("SELECT * FROM home_stockfuturesmodel", self.con)
        # Sort by TimeStamp
        df_sorted = df.sort_values(by='TIMESTAMP', ascending=False)
        latest_timestamp = df_sorted.iloc[0]['TIMESTAMP']
        df_filtered = df[df['TIMESTAMP'] == latest_timestamp]
        index_Futures_List = ['BANKNIFTY','FINNIFTY','MIDCPNIFTY','NIFTY','IDEA']
        df = df_filtered[~df_filtered['SYMBOL'].isin(index_Futures_List) ]
        df['classifiedLists'] = df['SYMBOL'].map(mapper.symbol_map)
        df['pChange'] = (((df['CLOSE'] - df['OPEN'])/df['OPEN'])*100).round(2)
        df['pVolume'] = (df['VOLUME'] / df['VOLUME'].max() * 100).round(2)
        df['freq']="D"
        # print(df.head())
        return df
    
    def indexdetailsDaily(self):
        df = pd.read_sql_query("SELECT * FROM home_stockfuturesmodel", self.con)
        # Sort by TimeStamp
        df_sorted = df.sort_values(by='TIMESTAMP', ascending=False)
        latest_timestamp = df_sorted.iloc[0]['TIMESTAMP']
        df_filtered = df[df['TIMESTAMP'] == latest_timestamp]
        index_Futures_List = ['BANKNIFTY','NIFTY']
        df = df_filtered[df_filtered['SYMBOL'].isin(index_Futures_List) ]
        df = df_filtered[df_filtered['SYMBOL'].isin(index_Futures_List) ]
        df['pChange'] = (((df['CLOSE'] - df['OPEN'])/df['OPEN'])*100).round(2)
        df['pVolume'] = (df['VOLUME'] / df['VOLUME'].max() * 100).round(2)
        df['freq']="D"
        # print(df.head())
        return df
    
    def detailsWeekly(self):
        # print("Weekly Method Called ####")
        weekly_df = pd.read_sql_query("SELECT \
            SYMBOL, date(TIMESTAMP, 'weekday 0', '-6 days') as Week,  \
            min(case when rn = 1 then OPEN end) as OPEN,    \
            max(HIGH) as HIGH,    \
            min(LOW) as LOW,\
            max(case when rn = 1 then CLOSE end) as CLOSE,  \
            sum(VOLUME) as VOLUME, \
            min(case when rn = 1 then OPEN_INT end) as OPEN_INT,    \
            sum(CHG_IN_OI) as CHG_IN_OI  \
            FROM \
            (SELECT *, row_number() over(partition by SYMBOL, date(TIMESTAMP, 'weekday 0', '-6 days') \
            order by TIMESTAMP desc) as rn    FROM home_stockfuturesmodel  ) \
            GROUP BY SYMBOL, Week \
            ORDER BY SYMBOL, Week ;", self.con)

        # Assuming df is your DataFrame
        weekly_df['Week'] = pd.to_datetime(weekly_df['Week'])

        # Set the DataFrame index to be the timestamp
        weekly_df.set_index('Week', inplace=True)
        
        # # Calculate the WeeklyChange
        weekly_df['WeeklyChange'] = weekly_df.groupby('SYMBOL')['CLOSE'].diff()
        weekly_df['pChange'] = ((weekly_df['WeeklyChange'] / weekly_df['OPEN'])*100).round(2)
        # wwekly_df[]
        weekly_df['pVolume'] = (weekly_df['VOLUME'] / weekly_df['VOLUME'].max() * 100).round(2)
        
        # Reset the index
        weekly_df.reset_index(inplace=True)

        # Add the WeekNumber
        weekly_df['WeekNumber'] = weekly_df['Week'].dt.isocalendar().week
        List_W_M_Y_Wn_H_M =  Globster().getWeekDay()
        week_num = List_W_M_Y_Wn_H_M[0]
        # print(f"The current week number is {week_num}")
        # print(List_W_M_Y_Wn_H_M[3])
        if List_W_M_Y_Wn_H_M[3] not in (3,4,5,6):
            week_num = week_num-1
        print("####",week_num)
        df_filtered = weekly_df[weekly_df['WeekNumber'] == week_num]
        df_filtered['freq']="W"
        
        #Exlude Index Futures        
        index_Futures_List = ['BANKNIFTY','FINNIFTY','MIDCPNIFTY','NIFTY','IDEA']
        df = df_filtered[~df_filtered['SYMBOL'].isin(index_Futures_List) ]
        # print(df.columns.to_list())
        print(df.head())
        
        # Return the DataFrame Weekly
        return df
    
    def indexdetailsWeekly(self):
        weekly_df = pd.read_sql_query("SELECT \
            SYMBOL, date(TIMESTAMP, 'weekday 0', '-6 days') as Week,  \
            min(case when rn = 1 then OPEN end) as OPEN,    \
            max(HIGH) as HIGH,    \
            min(LOW) as LOW,\
            max(case when rn = 1 then CLOSE end) as CLOSE,  \
            sum(VOLUME) as VOLUME, \
            min(case when rn = 1 then OPEN_INT end) as OPEN_INT,    \
            sum(CHG_IN_OI) as CHG_IN_OI  \
            FROM \
            (SELECT *, row_number() over(partition by SYMBOL, date(TIMESTAMP, 'weekday 0', '-6 days') \
            order by TIMESTAMP desc) as rn    FROM home_stockfuturesmodel  ) \
            GROUP BY SYMBOL, Week \
            ORDER BY SYMBOL, Week ;", self.con)

        # Assuming df is your DataFrame
        weekly_df['Week'] = pd.to_datetime(weekly_df['Week'])
        # Set the DataFrame index to be the timestamp
        weekly_df.set_index('Week', inplace=True)
         #Exlude Index Futures 
        index_Futures_List = ['BANKNIFTY','NIFTY']
        weekly_df = weekly_df[weekly_df['SYMBOL'].isin(index_Futures_List) ]
        # # Calculate the WeeklyChange
        weekly_df['WeeklyChange'] = weekly_df.groupby('SYMBOL')['CLOSE'].diff()
        weekly_df['pChange'] = ((weekly_df['WeeklyChange'] / weekly_df['OPEN'])*100).round(2)
        weekly_df['pVolume'] = (weekly_df['VOLUME'] / weekly_df['VOLUME'].max() * 100).round(2)
        # print("#######")
        # print(weekly_df)
        # Reset the index
        weekly_df.reset_index(inplace=True)

        # Add the WeekNumber
        weekly_df['WeekNumber'] = weekly_df['Week'].dt.isocalendar().week
        List_W_M_Y_Wn_H_M =  Globster().getWeekDay()
        week_num = List_W_M_Y_Wn_H_M[0]
        # print(f"The current week number is {week_num}")
        # print(List_W_M_Y_Wn_H_M[3])
        if List_W_M_Y_Wn_H_M[3] not in (3,4,5,6):
            week_num = week_num-1
        print("####",week_num)
        df_filtered = weekly_df[weekly_df['WeekNumber'] == week_num]
        df_filtered['freq']="W"
        # print("#######")
        # print(df_filtered)
        # Return the DataFrame Weekly
        return df_filtered

    def detailsMonthly(self):
        print("Monthly Method Called ####")
        monthly_df = pd.read_sql_query("""
        SELECT 
            SYMBOL, 
            strftime('%Y-%m', TIMESTAMP) as Month,  
            min(case when rn = 1 then OPEN end) as OPEN,    
            max(HIGH) as HIGH,    
            min(LOW) as LOW,
            max(case when rn = 1 then CLOSE end) as CLOSE,  
            sum(VOLUME) as VOLUME, 
            sum(OPEN_INT) as OPEN_INT,  
            sum(CHG_IN_OI) as CHG_IN_OI  
        FROM 
            (SELECT *, row_number() over(partition by SYMBOL, strftime('%Y-%m', TIMESTAMP) 
            order by TIMESTAMP desc) as rn    
            FROM home_stockfuturesmodel) 
        GROUP BY SYMBOL, Month 
        ORDER BY SYMBOL, Month;
        """, self.con)

        # print(monthly_df.head()) 

        # Assuming df is your DataFrame
        monthly_df['Month'] = pd.to_datetime(monthly_df['Month'])

        # Set the DataFrame index to be the timestamp
        monthly_df.set_index('Month', inplace=True)

        # # Calculate the MonthlyChange
        # monthly_df['MonthlyChange'] = monthly_df.groupby('SYMBOL')['CLOSE'].diff()
        
         # # Calculate the MonthlyChange
        monthly_df['mChange'] = monthly_df.groupby('SYMBOL')['CLOSE'].diff()
        monthly_df['pChange'] = ((monthly_df['mChange']/monthly_df['OPEN'])*100).round(2)
        monthly_df['pVolume'] = (monthly_df['VOLUME'] / monthly_df['VOLUME'].max() * 100).round(2)

        # Reset the index
        monthly_df.reset_index(inplace=True)
        # Add the MonthNumber
        monthly_df['MonthNumber'] = monthly_df['Month'].dt.month
        # print(monthly_df)
        List_W_M_Y_Wn_H_M =  Globster().getWeekDay()
        month_num = List_W_M_Y_Wn_H_M[1]
        print(f"The current Month number is {month_num}")
        df_filtered = monthly_df[monthly_df['MonthNumber'] == month_num]
        # print("MonthlyDF")
        # print(df_filtered)
        df_filtered['freq']="M"
        
        index_Futures_List = ['BANKNIFTY','FINNIFTY','MIDCPNIFTY','NIFTY','IDEA']
        df = df_filtered[~df_filtered['SYMBOL'].isin(index_Futures_List) ]
        
        # Display the DataFrame
        return df

    def indexdetailsMonthly(self):
        monthly_df = pd.read_sql_query("""
        SELECT 
            SYMBOL, 
            strftime('%Y-%m', TIMESTAMP) as Month,  
            min(case when rn = 1 then OPEN end) as OPEN,    
            max(HIGH) as HIGH,    
            min(LOW) as LOW,
            max(case when rn = 1 then CLOSE end) as CLOSE,  
            sum(VOLUME) as VOLUME, 
            sum(OPEN_INT) as OPEN_INT,  
            sum(CHG_IN_OI) as CHG_IN_OI  
        FROM 
            (SELECT *, row_number() over(partition by SYMBOL, strftime('%Y-%m', TIMESTAMP) 
            order by TIMESTAMP desc) as rn    
            FROM home_stockfuturesmodel) 
        GROUP BY SYMBOL, Month 
        ORDER BY SYMBOL, Month;
        """, self.con)

        # Assuming df is your DataFrame
        monthly_df['Month'] = pd.to_datetime(monthly_df['Month'])

        # Set the DataFrame index to be the timestamp
        monthly_df.set_index('Month', inplace=True)

        index_Futures_List = ['BANKNIFTY','NIFTY']
        monthly_df = monthly_df[monthly_df['SYMBOL'].isin(index_Futures_List) ]
        
        # # Calculate the MonthlyChange
        monthly_df['mChange'] = monthly_df.groupby('SYMBOL')['CLOSE'].diff()
        monthly_df['pChange'] = ((monthly_df['mChange']/monthly_df['OPEN'])*100).round(2)
        monthly_df['pVolume'] = (monthly_df['VOLUME'] / monthly_df['VOLUME'].max() * 100).round(2)


        # Reset the index
        monthly_df.reset_index(inplace=True)

        # Add the MonthNumber
        monthly_df['MonthNumber'] = monthly_df['Month'].dt.month
        List_W_M_Y_Wn_H_M =  Globster().getWeekDay()
        month_num = List_W_M_Y_Wn_H_M[1]
        print(f"The current Month number is {month_num}")
        df_filtered = monthly_df[monthly_df['MonthNumber'] == month_num]
        # print(df_filtered)
        df_filtered['freq']="M"
        return df_filtered

    def get_lists(self, symbol):
        return self.symbol_map.get(symbol, [])


# FetchDetailsByFrequency().detailsWeekly()