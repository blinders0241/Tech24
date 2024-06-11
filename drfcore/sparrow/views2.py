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
    index = request.GET.get('inDexName', '')
    expiry = request.GET.get('expiry', '')
    print("# == Params received ==============================")
    print(f"IndexName: {index} , ExpiryType: {expiry}")
    dataFrame, CE_top_10_OI_strikeprice , PE_top_10_OI_strikeprice, CE_top_10_COI_strikeprice, PE_top_10_COI_strikeprice = sparrowLib().getDataDF(index,expiry)
    
    data = json.loads(dataFrame.to_json(orient='records'))
    
    # set the FileNAme to be read
    if index == "NIFTY":
        fileNametoRead =  os.path.join(BASE_DIR, 'static', 'dataN50.json')
    elif index == "BANKNIFTY":
        fileNametoRead =  os.path.join(BASE_DIR, 'static', 'dataBNF.json')
    else:
        fileNametoRead =  os.path.join(BASE_DIR, 'static', 'data.json')
    
    # Define the file path
    file_path = fileNametoRead
    # Load existing data
    try:
        with open(file_path, 'r') as f:
            file_content = f.read()
            if file_content.strip():  # Check if file is not empty or contains only whitespace
                existing_data = json.loads(file_content)
            else:
                existing_data = []
    except FileNotFoundError:
        existing_data = []

    # Append new data to existing data
    for new_item in data:
        print("new Item Received",new_item)
        if not any(existing_item['Time'] == new_item['Time'] and existing_item['ExpiryDate'] == new_item['ExpiryDate'] for existing_item in existing_data):
            existing_data.append(new_item)
                # Write the data into a JSON file
            with open(file_path, 'w') as f:
                json.dump(existing_data, f)
        else:
            print("##############No New Data")



    # Return the JSON data
    
    return JsonResponse(existing_data, safe=False)
