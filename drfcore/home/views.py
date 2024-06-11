from django.db import IntegrityError
from pandas.tseries.frequencies import to_offset
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from . import serializers
from home.models import NotesModel
from home.models import StockFuturesModel
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
from .mylibs.AnalyzeBhavcopy.Format_n_Deliver import *
from .mylibs.AnalyzeBhavcopy.DbConnections import *
from .mylibs.GlobsterHome import *
from .mylibs.AnalyzeBhavcopy.FetchDetailsByFrequency import *
from .mylibs.NseLiveData.HeatMapGenerate import *

# Create your views here.
class HomeViewSet(viewsets.ModelViewSet):
    queryset = NotesModel.objects.all()
    serializer_class = serializers.NotesModelSerializers

@csrf_exempt
def handle_request(request):
    if request.method == 'POST' and request.FILES.get('csvFile'):
        uploaded_file = request.FILES['csvFile']
        data = pd.read_csv(uploaded_file)
        result = Format_n_Deliver.getJsonbySourceFile(data)
        response = {"result":result}
        return JsonResponse(response)
    else:
        response_data = {'error': 'Invalid request'}
        return JsonResponse(response_data, status=400)

@csrf_exempt
def displayNotes(request):
    msg = "HELLO"
    return JsonResponse({"result": msg})


"""Upload the CSV content to DB

Returns:
    _type_: _description_
"""
@csrf_exempt
def handleDBUpload(request):
    # print("Reached Upload area")
    if request.method == 'POST' and request.FILES.get('csvFile'):
        uploaded_file = request.FILES['csvFile']
        df = pd.read_csv(uploaded_file)
        df['TIMESTAMP'] = pd.to_datetime(df['TIMESTAMP'])
        print("Recived Dataframe goes like this \n",df.tail())
        for index, row in df.iterrows():
            if row['SYMBOL'] == '':
                continue
            try:        # hdr = ['SYMBOL', 'OPEN', 'HIGH', 'LOW', 'CLOSE', 'VOLUME', 'OPEN_INT', 'CHG_IN_OI', 'TIMESTAMP']
                obj = StockFuturesModel.objects.create(
                SYMBOL= row['SYMBOL'],
                OPEN = row['OPEN'],
                HIGH = row['HIGH'],
                LOW = row['LOW'],
                CLOSE = row['CLOSE'],
                VOLUME = row['CONTRACTS'],
                OPEN_INT = row['OPEN_INT'],
                CHG_IN_OI = row['CHG_IN_OI'],   
                TIMESTAMP = row['TIMESTAMP'],
                )
                obj.save()
            except IntegrityError as e:
                print("Error occurred while saving row to db", row['Issue key'], e)

        response = {"result": "Saved to DB"}
        return JsonResponse(response)
    else:
        response = {'error': 'Invalid request'}
        return JsonResponse(response, status=400)

def clearDB(request):
    try:
        StockFuturesModel.objects.all().delete()
        return JsonResponse({"result": "Cleared DB succesfully"})
    except:
        print("Error occurred while deleting table")
        return JsonResponse({"result": "Error occurred"})

def displayStockdetails(request):
        timeFrame = request.GET.get('param1', '')
        print("# == Params received ============================================")
        print(f"params1: {timeFrame}")
        if timeFrame == "D":
            df = FetchDetailsByFrequency().detailsDaily()
            # print(df.columns.to_list())
            data = json.loads(df.to_json(orient='records'))
            return JsonResponse(data, safe=False)
        elif timeFrame == "W":
            df = FetchDetailsByFrequency().detailsWeekly()
            data = json.loads(df.to_json(orient='records',index=False))
            return JsonResponse(data, safe=False)
        elif timeFrame == "M":
            df = FetchDetailsByFrequency().detailsMonthly()
            data = json.loads(df.to_json(orient='records',index=False))
            return JsonResponse(data, safe=False)
        else:
            print("RAN INTO ERRORS")

def displayIndexdetails(request):
        timeFrame = request.GET.get('param1', '')
        print("# == INDEX Params received ============================================")
        print(f"params1: {timeFrame}")
        if timeFrame == "D":
            df = FetchDetailsByFrequency().indexdetailsDaily()
            # print(df.columns.to_list())
            data = json.loads(df.to_json(orient='records',index=False))
            return JsonResponse(data, safe=False)
        elif timeFrame == "W":
            df = FetchDetailsByFrequency().indexdetailsWeekly()
            # print(df.columns.to_list())
            # print(df.head())
            data = json.loads(df.to_json(orient='records',index=False))
            return JsonResponse(data, safe=False)
        elif timeFrame == "M":
            df = FetchDetailsByFrequency().indexdetailsMonthly()
            print(df.columns.to_list())
            print(df.head())
            data = json.loads(df.to_json(orient='records',index=False))
            return JsonResponse(data, safe=False)
        else:
            print("RAN INTO ERRORS")
            
def stockMasterDetail( request):
    messagecalledCounter = 0
    timeFrame = request.GET.get('param1', '')
    stockName = request.GET.get('param2', '')
    print("# == Params received ============================================")
    print(f"params1: {timeFrame} and params2: {stockName}")
    
    # Get the required DB connection first
    con = DbConnections().connectToDB()

    def addSignaltoDataframe(dataframe):
        val = "Long BuildUp"
        if (dataframe['pCOI'] > 0 and dataframe['Change'] > 0):
            val = "Long BuildUp"
        elif dataframe['pCOI'] > 0 and dataframe['Change'] < 0:
            val = "Shorts BuildUp"
        elif dataframe['pCOI'] < 0 and dataframe['Change'] < 0:
            val = "Long Liquidation"
        elif dataframe['pCOI'] < 0 and dataframe['Change'] > 0:
            val = "Shorts Covering"
        else:
            val = "Check Manually"
        return val
    
    ## Logic for Resampling the data into Weekly & Monthly
    logic = {  
    'OPEN': 'first',
    'HIGH': 'max',
    'LOW': 'min',
    'CLOSE': 'last',
    'VOLUME': 'sum',
    'OPEN_INT': 'sum',
    'CHG_IN_OI': 'sum'
    }
    
    if timeFrame == "D":
        #create a dataframe from the database using pandas feature read_sql_query
        df = pd.read_sql_query("SELECT * FROM home_stockfuturesmodel", con)
        #setting the dataframe to fetch information of the stockname received
        df = df[df['SYMBOL'] == stockName]
        df = df.sort_values(by='TIMESTAMP', ascending=False)
        #Calculating Day Change , % Day change %Change in Open Interest for the Stock
        df['Change'] = df['CLOSE'].diff(periods=-1)
        df['pChange'] = ((df['Change'] /df['CLOSE'])*100).round(2)
        df['pCOI'] = ((df['CHG_IN_OI'] / df['OPEN_INT'])*100).round(2)
        #Finally we are generating the signal to provide an idea 
        df['Signal'] = df.apply(addSignaltoDataframe,axis=1)
        # df = df.fillna(method='ffill')
        df = df.head(15)
        dataOne = json.loads(df.to_json(orient='records'))
        return JsonResponse(dataOne, safe=False)
    
    elif timeFrame == "W":
        weekly_df = pd.read_sql_query("SELECT       SYMBOL,       date(TIMESTAMP, 'weekday 0', '-6 days') as Week,        (SELECT OPEN FROM home_stockfuturesmodel AS hsm2        WHERE hsm2.SYMBOL = hsm.SYMBOL AND              date(hsm2.TIMESTAMP, 'weekday 0', '-6 days') = date(hsm.TIMESTAMP, 'weekday 0', '-6 days') AND              hsm2.TIMESTAMP = (SELECT MIN(TIMESTAMP) FROM home_stockfuturesmodel AS hsm3                                WHERE hsm3.SYMBOL = hsm2.SYMBOL AND                                      date(hsm3.TIMESTAMP, 'weekday 0', '-6 days') = date(hsm2.TIMESTAMP, 'weekday 0', '-6 days'))) as OPEN,          max(HIGH) as HIGH,          min(LOW) as LOW,      (SELECT CLOSE FROM home_stockfuturesmodel AS hsm2        WHERE hsm2.SYMBOL = hsm.SYMBOL AND              date(hsm2.TIMESTAMP, 'weekday 0', '-6 days') = date(hsm.TIMESTAMP, 'weekday 0', '-6 days') AND              hsm2.TIMESTAMP = (SELECT MAX(TIMESTAMP) FROM home_stockfuturesmodel AS hsm3                                WHERE hsm3.SYMBOL = hsm2.SYMBOL AND                                      date(hsm3.TIMESTAMP, 'weekday 0', '-6 days') = date(hsm2.TIMESTAMP, 'weekday 0', '-6 days'))) as CLOSE,        sum(VOLUME) as VOLUME,       (SELECT OPEN_INT FROM home_stockfuturesmodel AS hsm2        WHERE hsm2.SYMBOL = hsm.SYMBOL AND              date(hsm2.TIMESTAMP, 'weekday 0', '-6 days') = date(hsm.TIMESTAMP, 'weekday 0', '-6 days') AND              hsm2.TIMESTAMP = (SELECT MAX(TIMESTAMP) FROM home_stockfuturesmodel AS hsm3                                WHERE hsm3.SYMBOL = hsm2.SYMBOL AND                                      date(hsm3.TIMESTAMP, 'weekday 0', '-6 days') = date(hsm2.TIMESTAMP, 'weekday 0', '-6 days'))) as OPEN_INT,        sum(CHG_IN_OI) as CHG_IN_OI    FROM       (SELECT *, row_number() over(partition by SYMBOL, date(TIMESTAMP, 'weekday 0', '-6 days')       order by TIMESTAMP desc) as rn          FROM home_stockfuturesmodel) as hsm  GROUP BY SYMBOL, Week   ORDER BY SYMBOL, Week;", con)
        # print("WEEKLY DATA RESAMPLING initiating....Weekly:",stockName)
        weekly_df = weekly_df[weekly_df['SYMBOL'] == stockName]
        # Convert 'TIMESTAMP' to datetime
        weekly_df['Week'] = pd.to_datetime(weekly_df['Week'])
        print("Row Count of the before adding Symbol",weekly_df.shape[0])
        weekly_df.set_index('Week', inplace=True)
        # weekly_df = weekly_df[weekly_df['SYMBOL'] == stockName]
        weekly_df = weekly_df.sort_values(by='Week', ascending=False)
        #Calculating Weekly Change , % Week change %Change in Open Interest for the Stock
        weekly_df['Change'] = weekly_df['CLOSE'].diff(periods=-1)
        weekly_df['pChange'] = ((weekly_df['Change'] /weekly_df['CLOSE'])*100).round(2)
        weekly_df['pCOI'] = ((weekly_df['CHG_IN_OI'] / weekly_df['OPEN_INT'])*100).round(2)
        #Finally we are generating the signal to provide an idea 
        weekly_df['Signal'] = weekly_df.apply(addSignaltoDataframe,axis=1)
        # Reset the index
        weekly_df.reset_index(inplace=True)
        print("Inside Dataframe")
        # print(weekly_df.head())
        weekly_df = weekly_df.head(9)
        dataOne = json.loads(weekly_df.to_json(orient='records',index=False))
        return JsonResponse(dataOne, safe=False)
   
    # print(timeFrame)
    elif timeFrame == "M":
        messagecalledCounter += 1
        ReachedRightLoopBanner = f"""
                    Hello, MR SimplyALI , you have reached the right method. Cross verify the params received
                    stockName : {stockName} type : {type(stockName)}
                    timeFrame : {timeFrame} type : {type(timeFrame)}
                    ^Message# {messagecalledCounter}
                    """
        print(ReachedRightLoopBanner)
        # Apply your logic here
        #create a dataframe from the database using pandas feature read_sql_query
        monthly_df = pd.read_sql_query("""
            SELECT 
                SYMBOL, 
                strftime('%Y-%m', TIMESTAMP) as Month,  
                (SELECT OPEN FROM home_stockfuturesmodel AS hsm2 
                WHERE hsm2.SYMBOL = hsm.SYMBOL AND 
                    strftime('%Y-%m', hsm2.TIMESTAMP) = strftime('%Y-%m', hsm.TIMESTAMP) AND 
                    hsm2.TIMESTAMP = (SELECT MIN(TIMESTAMP) FROM home_stockfuturesmodel AS hsm3 
                                        WHERE hsm3.SYMBOL = hsm2.SYMBOL AND 
                                            strftime('%Y-%m', hsm3.TIMESTAMP) = strftime('%Y-%m', hsm2.TIMESTAMP))) as OPEN,    
                max(HIGH) as HIGH,    
                min(LOW) as LOW,
                max(case when rn = 1 then CLOSE end) as CLOSE,  
                sum(VOLUME) as VOLUME,
                max(case when rn = 1 then OPEN_INT end) as OPEN_INT,   
                sum(CHG_IN_OI) as CHG_IN_OI  
            FROM 
                (SELECT *, row_number() over(partition by SYMBOL, strftime('%Y-%m', TIMESTAMP) 
                order by TIMESTAMP desc) as rn    
                FROM home_stockfuturesmodel) as hsm
            GROUP BY SYMBOL, Month 
            ORDER BY SYMBOL, Month;

        """, con)
        
        # Convert 'TIMESTAMP' to datetime
        monthly_df['Month'] = pd.to_datetime(monthly_df['Month'])
        # Set 'TIMESTAMP' as the index
        monthly_df.set_index('Month', inplace=True)
        monthly_df = monthly_df[monthly_df['SYMBOL'] == stockName]
        print("Row Count of the returned dataframea after sampling",monthly_df.shape[0])
        monthly_df = monthly_df.sort_values(by='Month', ascending=False)
        #Calculating Day Change , % Day change %Change in Open Interest for the Stock
        monthly_df['Change'] = monthly_df['CLOSE'].diff(periods=-1)
        monthly_df['pChange'] = ((monthly_df['Change'] /monthly_df['CLOSE'])*100).round(2)
        monthly_df['pCOI'] = ((monthly_df['CHG_IN_OI'] / monthly_df['OPEN_INT'])*100).round(2)
        #Finally we are generating the signal to provide an idea 
        monthly_df['Signal'] = monthly_df.apply(addSignaltoDataframe,axis=1)
        monthly_df = monthly_df.head(9).fillna(0)
        
        monthly_df.reset_index(inplace=True)
        print(monthly_df.head())
        # monthly_df.set_index('SYMBOL', inplace=True)
        # print("Log Message",monthly_df)
        dataOne = json.loads(monthly_df.to_json(orient='records',index=False,date_format='iso'))
        return JsonResponse(dataOne, safe=False)

    else:
        print("####################################")
        print(f'params doesnt meet this function call prerequisite to enter MONTHLY')

# @csrf_exempt
# def prepareBhavCopy(request):
#     print("Running For the day",datetime.datetime.now())
#     createList = []
#     ReurnDerivatived_df, ReurnMsgEquity_df = FormatNdDeliver().getExtractedFiles()
#     data = json.loads(ReurnDerivatived_df.to_json(orient='records',index=False))
#     data2 = json.loads(ReurnMsgEquity_df.to_json(orient='records',index=False))
#     createList.append(data)
#     createList.append(data2)
#     return JsonResponse(data, safe=False)
    

def heatMapGenerate(request):
        indexName = request.GET.get('index', '')
        print("# == Params received ============================================")
        print(f"params1: {indexName}")
        requireURL = GlobsterHome().get_url(indexName)
        df = HeatMapGenerate().generateIndexMap(requireURL)
        data = json.loads(df.to_json(orient='records',index=False))
        return JsonResponse(data, safe=False)