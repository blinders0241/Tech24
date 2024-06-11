
import os,time,datetime

class Globster():
    SQL_URL = r'C:\SIMPLY_Official\2024\DRF\drfcore'
    def __init__(self):
        pass 
    
    # SQL_URL = r'C:\SIMPLYALI\2024\DRF\drfcore'
    def getWeekDay(self):
        my_date = datetime.datetime.now()
        W_M_Y_Wn_H_M = []
        # Get the week number
        week = my_date.isocalendar()[1]
        W_M_Y_Wn_H_M.append(week)
        month = my_date.month
        W_M_Y_Wn_H_M.append(month)
        Year = my_date.year
        W_M_Y_Wn_H_M.append(Year)
        dayOfWeek = my_date.weekday()
        W_M_Y_Wn_H_M.append(dayOfWeek)
        hour = my_date.hour
        W_M_Y_Wn_H_M.append(hour)
        minutes = my_date.minute
        W_M_Y_Wn_H_M.append(minutes)
        # print(W_M_Y_Wn_H_M)
        return W_M_Y_Wn_H_M

# Globster().getWeekDay()