from django.shortcuts import render
from django.db import IntegrityError
from pandas.tseries.frequencies import to_offset
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from equityHome.models import StockEquitiesModel,IndexHistoricalModel
import pandas as pd
from django.views.decorators.csrf import csrf_exempt
import json
from .equityLibs.AnalyzeEquityBhavCopy.EQFetchDetailsByFrequency import *
from .equityLibs.Globster import *
# Create your views here.
@csrf_exempt
def handleEquityDBUpload(request):
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
                obj = StockEquitiesModel.objects.create(
                SYMBOL= row['SYMBOL'],
                OPEN = row['OPEN'],
                HIGH = row['HIGH'],
                LOW = row['LOW'],
                CLOSE = row['CLOSE'],
                TOTTRDQTY = row['TOTTRDQTY'],
                TOTTRDVAL = row['TOTTRDVAL'],
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
    
@csrf_exempt
def uploadIndexHistoricals(request):
    indexName = request.GET.get('indexName', '')
    print(f"params1: {indexName}")
    if request.method == 'POST' and request.FILES.get('csvFile'):
        uploaded_file = request.FILES['csvFile']
        df = pd.read_csv(uploaded_file)
        df['Date '] = pd.to_datetime(df['Date '], format='%d-%b-%y')

        print("Recived Dataframe goes like this \n",df.tail())
        for index, row in df.iterrows():
            if row['Date '] == '':
                continue
            try:        # hdr = ['SYMBOL', 'OPEN', 'HIGH', 'LOW', 'CLOSE', 'VOLUME', 'OPEN_INT', 'CHG_IN_OI', 'TIMESTAMP']
                obj = IndexHistoricalModel.objects.create(
                SYMBOL= indexName,
                OPEN = row['Open '],
                HIGH = row['High '],
                LOW = row['Low '],
                CLOSE = row['Close '],
                TOTTRDQTY = row['Shares Traded '],
                TOTTRDVAL = row['Turnover'],
                TIMESTAMP = row['Date '],
                )
                obj.save()
            except IntegrityError as e:
                print("Error occurred while saving row to db", row['Issue key'], e)

        response = {"result": "Saved to DB"}
        return JsonResponse(response)
    else:
        response = {'error': 'Invalid request'}
        return JsonResponse(response, status=400)    
    
def displayEquityetails(request):
        timeFrame = request.GET.get('param1', '')
        print("# == Params received ============================================")
        print(f"params1: {timeFrame}")
        if timeFrame == "D":
            df = EQFetchDetailsByFrequency().detailsDaily()
            # print(df.columns.to_list())
            data = json.loads(df.to_json(orient='records',index=False))
            return JsonResponse(data, safe=False)
        else:
            print("RAN INTO ERRORS")

def clearDB(request):
    try:
        StockEquitiesModel.objects.all().delete()
        return JsonResponse({"result": "Cleared Equity DB succesfully"})
    except:
        print("Error occurred while deleting Equity table")
        return JsonResponse({"result": "Error occurred"})