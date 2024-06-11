import os,sys,shutil
import zipfile
import pandas as pd
import numpy as np
from pathlib import Path

# Define the path to the parent directory of drfcore
path = Path('C:/SIMPLY_Official/2024/TechHome241/')

# Add the path to sys.path
sys.path.append(str(path.resolve()))

# Now you should be able to import the module
from drfcore.home.mylibs.GlobsterHome import *

class FileExtractor:
    def __init__(self):
        pass

    def extractZipFiles(self,file_path):
        print("################ Reached extractZipFiles ################################")
        # Get all the .zip files in the directory
        # print("file_path",file_path)
        try:
            zip_files = [f for f in os.listdir(file_path) if f.endswith('.zip')]
            print("zip_files", zip_files)
        except Exception as e:
            print("Exception",e)
        
        extracted_files = []

        for zip_file in zip_files:
            # Full path to the zip file
            full_path = os.path.join(file_path, zip_file)
            
            # Check if it is a file
            if os.path.isfile(full_path):
                # Create a ZipFile object
                with zipfile.ZipFile(full_path, 'r') as zip_ref:
                    # Extract all the contents of the zip file in the directory
                    zip_ref.extractall(file_path)
                    # Add the names of the extracted files to the list
                    extracted_files.extend(zip_ref.namelist())
                # Remove the zip file
                os.remove(full_path)
        print(extracted_files)
        return extracted_files

    def processFiles(self, file_path,file_list,targetfilePath):
        ListofExcelfiles = []
        for file_name in file_list:
            print("Processing File",file_name)
            if file_name.startswith('fo'):
                full_path = os.path.join(file_path, file_name)
                df = pd.read_csv(full_path)
                filterIndexData = df[np.logical_or(df.INSTRUMENT == 'FUTIDX', df.INSTRUMENT == 'FUTSTK')]
                data = []
                symbols_repeat = set()
                counter = -1

                for symbol in filterIndexData.SYMBOL:
                    counter += 1
                    if symbol in symbols_repeat:
                        data[-1]['OPEN_INT'] += filterIndexData['OPEN_INT'].iloc[counter]
                        data[-1]['CHG_IN_OI'] += filterIndexData['CHG_IN_OI'].iloc[counter]
                        data[-1]['CONTRACTS'] += filterIndexData['CONTRACTS'].iloc[counter]
                    else:
                        symbols_repeat.add(symbol)
                        index = filterIndexData.SYMBOL.tolist().index(symbol)
                        data.append({
                            'SYMBOL': filterIndexData['SYMBOL'].iloc[index],
                            'OPEN': filterIndexData['OPEN'].iloc[index],
                            'HIGH': filterIndexData['HIGH'].iloc[index],
                            'LOW': filterIndexData['LOW'].iloc[index],
                            'CLOSE': filterIndexData['CLOSE'].iloc[index],
                            'CONTRACTS': filterIndexData['CONTRACTS'].iloc[index],
                            'OPEN_INT': filterIndexData['OPEN_INT'].iloc[index],
                            'CHG_IN_OI': filterIndexData['CHG_IN_OI'].iloc[index],
                            'TIMESTAMP': filterIndexData['TIMESTAMP'].iloc[index],
                        })
            

                formatted_df = pd.DataFrame(data)
                status = formatted_df.to_csv(os.path.join(targetfilePath, file_name), index=False)
                print("%$%",status)
                ListofExcelfiles.append(os.path.join(targetfilePath, file_name))
            else:
                continue   
        # msg = "SuccessFully Done, Check TechHome241\drfcore\home\mylibs\data\ReadyBhavFile\Derivatives"
        # print(msg)
        # print("Printing all files Formatted",ListofExcelfiles)
        return ListofExcelfiles
    
    def processEquityFiles(self, file_path, file_list, targetfilePath, nifty_200_symbols):
        ListofExcelfiles = []
        for file_name in file_list:
            if file_name.startswith('cm'):
                full_path = os.path.join(file_path, file_name)
                df = pd.read_csv(full_path)
                filter_Stock_data = df[np.logical_and(df.SERIES == 'EQ', df.CLOSE >= 40)]
                df = filter_Stock_data.drop(columns=['SERIES', 'LAST', 'PREVCLOSE', 
                                                     'ISIN', 'TOTALTRADES', 'Unnamed: 13'])
                df_Nifty_200 = df[df.SYMBOL.isin(nifty_200_symbols)]
                status = df_Nifty_200.to_csv(os.path.join(targetfilePath, file_name), index=False)
                # print("##",status)
                ListofExcelfiles.append(os.path.join(targetfilePath, file_name))
            else:
                continue
        # print("Printing all files Formatted",ListofExcelfiles)
        
        return ListofExcelfiles

