import os.path
import zipfile
import glob
import os
import shutil
from datetime import datetime

currentPath = r'C:\SIMPLY_Official\2024\RealIT\\'
baseloc_Derivatives = currentPath + r'realApp\app\data\rawbhavcopy\Derivatives\\'
cwd_Derivatives = baseloc_Derivatives + 'Ongoing\\'
baseloc_Equity = currentPath + r'realApp\app\data\rawbhavcopy\Equity\\'
cwd_Equity = baseloc_Equity + 'Ongoing\\'
currentMonth = datetime.now().strftime('%h').upper()

class extractZipAndPlace():
    def __init__(self):
        pass

    def getZipFiles(self,type):
        if type == "Derivatives":
            files = glob.glob(cwd_Derivatives + '*.zip')
        elif type == "Equity":
            files = glob.glob(cwd_Equity + '*.zip')
        else:
            files = glob.glob(cwd_Derivatives + '*.zip')
        return files
    def doExtract(self,type,month):
        zipFiles = extractZipAndPlace().getZipFiles(type)
        for f in zipFiles:
            zf = zipfile.ZipFile(f, mode='r')
            if type == "Derivatives":
                zf.extractall(path=os.path.dirname(baseloc_Derivatives + currentMonth +'\\'), pwd='password'.encode('ascii'))
                zf.close()
                csvFilesList = [f for f in os.listdir(baseloc_Derivatives + currentMonth) if '.csv' in f.lower()]
            elif type == "Equity":
                zf.extractall(path=os.path.dirname(baseloc_Equity + currentMonth + '\\'),
                              pwd='password'.encode('ascii'))
                zf.close()
                csvFilesList = [f for f in os.listdir(baseloc_Equity + currentMonth) if '.csv' in f.lower()]
            else:
                zf.extractall(path=os.path.dirname(baseloc_Derivatives + currentMonth + '\\'),
                              pwd='password'.encode('ascii'))
                zf.close()
                csvFilesList = [f for f in os.listdir(baseloc_Derivatives + currentMonth) if '.csv' in f.lower()]

        print("Following files successfully Extracted:",csvFilesList)
        sendThisList = []
        sub = month
        for filename in csvFilesList:
            if sub in filename:
                sendThisList.append(filename)
        print(sendThisList)  
        return sendThisList

        # print(csvFilesList)
# extractZipAndPlace().doExtract("Equity")