import json,os
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent


def append_to_json_file(file_path, data):
    # Load existing data
    try:
        with open(file_path, 'r') as f:
            existing_data = json.load(f)
    except FileNotFoundError:
        existing_data = []

    # Append new data to existing data
    existing_data.extend(data)

    # Write the data into the JSON file
    with open(file_path, 'w') as f:
        json.dump(existing_data, f)

# Usage
file_path = r'C:\\SIMPLY_Official\\2024\\TechHome241\\drfcore\\sparrow\\data2.json'

# file_path = '/path/to/your/json/file.json'
data = [{'ExpiryDate': '29-FEB-2024', 'MaxPain': 22000.0, 'PCR': 1.17, 'PCR_TradedVol': 0.98, 'Time': '14:41', 'call_decay': -7.76, 'put_decay': -5.0, 'total_COI_CE': 34692, 'total_COI_PE': 40730, 'total_OI_CE': 679213, 'total_OI_PE': 797261, 'underlying': 22142.3}]
append_to_json_file(file_path, data)
