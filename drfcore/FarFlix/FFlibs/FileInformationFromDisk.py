import os
import pandas as pd
import sys
sys.path.append(r"C:\SIMPLY_Official\\2024\\TechHome241\drfcore\\FarFlix")
from FFlibs.DbConnections import DbConnections
from FFlibs.Globster import *
import shutil
CWD = os.getcwd()
class FileInformationFromDisk():
    def __init__(self) -> None:
        pass

    def saveInfo2Disk(self, ListofFiles, Filename):
        
        try:
            with open(Filename, 'w', encoding='utf-8') as f:
                for line in ListofFiles:
                    f.write(f"{line},\n")
            return True
        except Exception as e:
            print("Writing UnSuccessful", e)
            return False
    def do_basic_replacements (self,file_name):
        cleaned_name = file_name.replace("."," ").replace("_"," ")
        cleaned_name = ' '.join(cleaned_name.split())
        return cleaned_name.title()
    
  
    def fetchFilesfromDisk(self, DiskPath):
        Lst_FileName = []
        Lst_FilePath = []
        for root, dirs, files in os.walk(DiskPath):
            for file in files:
                file_path = os.path.join(root, file)
                file_type = os.path.splitext(file)[1]
                fileName = os.path.splitext(file)[0]
                # file_name = os.path.basename(file_path)
                Lst_FileName.append(fileName)
                Lst_FilePath.append(file_path)
                
        print(f"Total files : {len(Lst_FileName)}")
        DictFileInfo = dict(zip(Lst_FileName,Lst_FilePath))
        return Lst_FileName,DictFileInfo


    def findMissingMovies(self,path):
        """This method is used to compare the filenames present in the database against
            the actual files present on the Disk , that was ignored while fetching the information form IMDB, due to 
            badly naming conventioned
            Uncomment the lines 69 - 73 to use
        Returns:
            _type_: list of missing files in the DB
        """
        Lst_Movie_NotPresent = []
        con = DbConnections().connectToDB()
        df = pd.read_sql_query("SELECT * FROM FarFlix_farflixmoviesmodel where Classified = 'Bollywood'", con)
        Lst_Movie_CodesExisitsinDB = df['movieName_Disk'].to_list()
        Lst_FileName,DictFileInfo = FileInformationFromDisk().fetchFilesfromDisk(path)
        LSTcleanedFileName = []
        # LSTrawfilename = []
        for filename in Lst_FileName:
            newfilename = FileInformationFromDisk().do_basic_replacements(filename)
            # LSTrawfilename.append(filename)
            LSTcleanedFileName.append(newfilename)
        # dict_Raw_cleaned = dict(zip(LSTcleanedFileName,LSTrawfilename))
        
        for moviename in LSTcleanedFileName:
            if moviename not in  Lst_Movie_CodesExisitsinDB:   
                Lst_Movie_NotPresent.append(moviename)
        Flag = FileInformationFromDisk().saveInfo2Disk(Lst_Movie_NotPresent,"MissingItems.txt")
        print(Flag)
        return Flag
    
    def getdict_Raw_cleaned(self,path):
        Lst_FileName,DictFileInfo = FileInformationFromDisk().fetchFilesfromDisk(path)
        LSTcleanedFileName = []
        LSTrawfilename = []
        for filename in Lst_FileName:
            newfilename = FileInformationFromDisk().do_basic_replacements(filename)
            LSTrawfilename.append(filename)
            LSTcleanedFileName.append(newfilename)
        dict_Raw_cleaned = dict(zip(LSTcleanedFileName,LSTrawfilename))
        return dict_Raw_cleaned
        
    def load_file(self,file_path):
        with open(file_path, 'r',encoding='utf-8') as file:
            # Read the file and split it into lines
            lines = file.read().split('\n')
            # Split each line on commas and add the items to a list
            file_names = [item for line in lines for item in line.split(',') if item]
        
        return file_names

    def getFilePathforMissingMovieNames(self):
        path = r"D:\Simply_Movies\Bolly\Simply_Up_2_Date\\"
        
        filePath = CWD + os.sep + 'drfcore' + os.sep + 'FarFlix' + os.sep + 'data' + os.sep+'MissingMoviefromDB'
        # print(filePath)
        df = pd.read_csv(filePath + os.sep + "DictionaryFileNameDetails.csv")
        df['FilenameWithoutExt'] = df['FileName'].apply(lambda x: os.path.splitext(x)[0])
        file_names = FileInformationFromDisk().load_file(filePath + os.sep + "MissingItems.txt")
        # print(f"Filenames returned from text File",file_names)
        dict_Raw_cleaned = FileInformationFromDisk().getdict_Raw_cleaned(path)
        df_dict_Raw_cleaned = pd.DataFrame(dict_Raw_cleaned.items(), columns=['CleanFileName', 'RawFileName'])
        print(df_dict_Raw_cleaned.head())
        df_dict_Missing = df_dict_Raw_cleaned[df_dict_Raw_cleaned['CleanFileName'].isin(file_names)]
        file_names = df_dict_Missing['RawFileName'].to_list()
        print(f"count of missing files",len(file_names))
        filtered_df = df[df['FilenameWithoutExt'].isin(file_names)]
        filtered_df.to_csv(filePath + os.sep + "MissingItemswithFilePath.csv")

    def copying_file(self,source_path, destination_path):
        """
        Copying a file

        :type source_path: str
        :param source_path: path to the file that needs to be copied
        :type destination_path: str
        :param destination_path: path to where the file is going to be copied
        :rtype: bool
        :return: True if the file copied successfully, False otherwise
        """
        print(f"Moving....{source_path} to {destination_path}")
        shutil.move(source_path, destination_path)

        if os.path.exists(destination_path):
            print ("Done....")
            return True

        print ("Filed...")
        return False

    def copyMissingItems(self,path):
        print(path)
        df = pd.read_csv(path + os.sep + "MissingItemswithFilePath.csv")
        file_paths = df['FilePath'].to_list()
        
        new_location = r"D:\Simply_Movies\Bolly\Simply_Up_2_Date\MissingMovies\\"
        if not os.path.isdir(new_location):
            os.makedirs(new_location)
        # Move each file to the new location
        for file_path in file_paths:
            file_name = os.path.basename(file_path)
            if os.path.isfile(file_path):
                destinationPath = new_location + file_name
                Flag = FileInformationFromDisk().copying_file(file_path, destinationPath)
            print(Flag)

filePath = CWD + os.sep + 'drfcore' + os.sep + 'FarFlix' + os.sep + 'data' + os.sep+'MissingMoviefromDB'
FileInformationFromDisk().copyMissingItems(filePath)
# FileInformationFromDisk().getFilePathforMissingMovieNames()
    
# path = r"D:\Simply_Movies\Bolly\Simply_Up_2_Date\\"
# FileInformationFromDisk().findMissingMovies(path)



# file_info = FileInformationFromDisk()
# Lst_FileName,DictFileInfo = file_info.fetchFilesfromDisk(path)
# df = pd.DataFrame(DictFileInfo.items(), columns=['FileName', 'FilePath'])
# df.to_csv("DictionaryFileNameDetails.csv")
# Flag = file_info.saveInfo2Disk(Lst_FileName)
# print(Flag)
