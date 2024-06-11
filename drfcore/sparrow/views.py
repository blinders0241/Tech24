from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from home.mylibs.Sparrow.sparrowLib import *
import pandas as pd
import json
import os
from pathlib import Path
from django.templatetags.static import static

BASE_DIR = Path(__file__).resolve().parent.parent

pd.set_option('display.width',1200)
pd.set_option('display.max_columns',15)
pd.set_option('display.max_rows',30)

@csrf_exempt
def sparrowHome(request):
    dataContainerList = []
    index = request.GET.get('inDexName', '')
    expiry = request.GET.get('expiry', '')
    
    print("# == Params received ==============================")
    print(f"IndexName: {index} , ExpiryType: {expiry}")
    if expiry == "Week" or expiry == "W":
        expiry="W"
    elif expiry == "Monthly" or expiry == "M":
        expiry = "M"
    else:
        expiry = "M"
        
    if index == "handleCallStrikersOINIFTY" or index == "handlePutStrikersOINIFTY":
        index = "NIFTY" 
    dataFrame, CE_top_10_OI_strikeprice , PE_top_10_OI_strikeprice, CE_top_10_COI_strikeprice, PE_top_10_COI_strikeprice = sparrowLib().getDataDF(index,expiry)
    
    column_names = list(dataFrame.columns.values.tolist())

    if index == "NIFTY":
        fileNametoRead = os.path.join(BASE_DIR, 'static', 'dataN50.csv')
    elif index == "BANKNIFTY":
        fileNametoRead = os.path.join(BASE_DIR, 'static', 'dataBNF.csv')
    else:
        fileNametoRead = os.path.join(BASE_DIR, 'static', 'data.csv')

    # Load existing data from CSV
    try:
        existing_data = pd.read_csv(fileNametoRead)
    except FileNotFoundError as e:
        # print(e)
        existing_data = pd.DataFrame(columns=column_names)

    # Append new data to existing data (avoid duplicates)
    new_data = dataFrame[~dataFrame.duplicated(subset=['Time', 'ExpiryDate'])]
    updated_data = pd.concat([existing_data, new_data], ignore_index=True)
    updated_data.to_csv(fileNametoRead, index=False)
    # Sort the DataFrame by 'Time' and 'ExpiryDate' (ascending order)
    updated_data.sort_values(by=['Time'], ascending=False, inplace=True)
    # Identify duplicate rows based on 'Time' and 'ExpiryDate'
    duplicate_mask = updated_data.duplicated(subset=['Time', 'ExpiryDate'], keep='last')
    # Keep only the last occurrence (non-duplicate rows)
    cleaned_data = updated_data[~duplicate_mask]
    # Now 'cleaned_data' contains the DataFrame without duplicate rows
    # print(cleaned_data.head())
    data = json.loads(cleaned_data.to_json(orient='records',index=False))
    data2 = json.loads(CE_top_10_OI_strikeprice.to_json(orient='records',index=False))
    data3 = json.loads(PE_top_10_OI_strikeprice.to_json(orient='records',index=False))
    data4 = json.loads(CE_top_10_OI_strikeprice.to_json(orient='records',index=False))
    data5 = json.loads(CE_top_10_OI_strikeprice.to_json(orient='records',index=False))
    dataContainerList.append(data)
    dataContainerList.append(data2)
    dataContainerList.append(data3)
    # print(dataContainerList)
    return JsonResponse(dataContainerList, safe=False)
    
    
