import pandas as pd
from datetime import datetime, timedelta
from pathlib import Path
import sys
path = Path(r"drfcore")
# Add the path to sys.path
sys.path.append(str(path.resolve()))
from home.mylibs.AnalyzeBhavcopy.DbConnections import DbConnections

class fetch52WkHighLow:
    # Your existing code...
    def __init__(self):
        self.con = DbConnections().connectToDB()
        
    def detailsDaily(self,ticker):
        query = f"SELECT * FROM equityHome_stockequitiesmodel WHERE SYMBOL = '{ticker}'"
        df = pd.read_sql_query(query, self.con)


        # Convert TIMESTAMP to datetime and set it as index
        df['TIMESTAMP'] = pd.to_datetime(df['TIMESTAMP'])
        df.set_index('TIMESTAMP', inplace=True)

        # Calculate 52 weeks high and low with dates
        one_year_ago = datetime.now() - timedelta(weeks=52)
        df_last_year = df[df.index >= one_year_ago]

        high_52_weeks = df_last_year['HIGH'].max()
        low_52_weeks = df_last_year['LOW'].min()

        high_date = df_last_year[df_last_year['HIGH'] == high_52_weeks].index[0]
        low_date = df_last_year[df_last_year['LOW'] == low_52_weeks].index[0]

        # Compare high and low dates
        if high_date < low_date:
            flag = 0
        else:
            flag = 1

        # Count the number of days from today when the last 52 weeks High/Low was achieved
        days_since_high = (datetime.now() - high_date).days
        days_since_low = (datetime.now() - low_date).days

        return {
            '52_weeks_high': high_52_weeks,
            'high_date': high_date,
            '52_weeks_low': low_52_weeks,
            'low_date': low_date,
            'flag': flag,
            'days_since_high': days_since_high,
            'days_since_low': days_since_low
        }

# mydict = fetch52WkHighLow().detailsDaily("UPL")
# print(mydict["52_weeks_high"])