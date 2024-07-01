import datetime
import holidays
# Define Indian holidays
ind_holidays = holidays.India()

class ExpiryDate():
    def __init__(self):
        pass
    def get_expiry_date_weekly(self):
        today = datetime.date.today()
        # Find next Thursday
        next_thursday = today + datetime.timedelta((2-today.weekday() + 7) % 7)
        # If next Thursday is a holiday, return Wednesday instead
        if next_thursday in ind_holidays:
            return (next_thursday - datetime.timedelta(days=1)).strftime("%d-%b-%Y").upper()
        else:
            return next_thursday.strftime("%d-%b-%Y").upper()

    def get_expiry_date_monthly(self,Index):
        if Index == "NIFTY":
            today = datetime.date.today()
            # Find the last day of the current month
            if today.month == 12:
                last_day = today.replace(day=31)
            else:
                last_day = today.replace(month=today.month+1, day=1) - datetime.timedelta(days=1)
            # Find the last Thursday of the month
            while last_day.weekday() != 2:  # 0 is Monday, 1 is Tuesday, ..., 3 is Thursday
                last_day -= datetime.timedelta(days=1)
            if last_day in ind_holidays:
                return (last_day - datetime.timedelta(days=1)).strftime("%d-%b-%Y").upper()
            else:
                return last_day.strftime("%d-%b-%Y").upper()
        else:
            today = datetime.date.today()
            # Find the last day of the current month
            if today.month == 12:
                last_day = today.replace(day=31)
            else:
                last_day = today.replace(month=today.month+1, day=1) - datetime.timedelta(days=1)
            # Find the last Thursday of the month
            while last_day.weekday() != 3:  # 0 is Monday, 1 is Tuesday, ..., 3 is Thursday
                last_day -= datetime.timedelta(days=1)
            if last_day in ind_holidays:
                return (last_day - datetime.timedelta(days=2)).strftime("%d-%b-%Y").upper()
            else:
                return (last_day - datetime.timedelta(days=1)).strftime("%d-%b-%Y").upper()
            

# def get_expiry_date_monthly():
#     today = datetime.date.today()
#     # Find last Thursday of the month
#     next_month = today.replace(day=28) + datetime.timedelta(days=4)  # this will never fail
#     last_thursday = next_month - datetime.timedelta(days=next_month.weekday())
#     print("Last Thursday of Month",last_thursday)
#     # If last Thursday is a holiday, return Wednesday instead
#     if last_thursday in ind_holidays:
#         return (last_thursday - datetime.timedelta(days=1)).strftime("%d-%b-%Y").upper()
#     else:
#         return last_thursday.strftime("%d-%b-%Y").upper()

# print("Next weekly expiry date:", ExpiryDate().get_expiry_date_weekly())
# print("Next monthly expiry date:", ExpiryDate().get_expiry_date_monthly())
