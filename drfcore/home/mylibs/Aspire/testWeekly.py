import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect('your_database.db')

# Query the database to get daily data for UPL
query = """
SELECT * FROM home_stockfuturesmodel
WHERE SYMBOL = 'UPL'
"""
df = pd.read_sql_query(query, conn)

# Ensure that the 'TIMESTAMP' column is a datetime object
df['TIMESTAMP'] = pd.to_datetime(df['TIMESTAMP'])

# Set 'TIMESTAMP' as the index
df.set_index('TIMESTAMP', inplace=True)

# Resample the data to get weekly data
weekly_df = df.resample('W').agg({'OPEN': 'first', 'HIGH': 'max', 'LOW': 'min', 'CLOSE': 'last'})

# Print the weekly data
print(weekly_df)
