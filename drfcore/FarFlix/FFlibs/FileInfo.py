import os
import sys
sys.path.append(r"C:\SIMPLY_Official\\2024\\TechHome241\drfcore\\FarFlix")
import pandas as pd
import imdb
from datetime import datetime
now = datetime.now() # current date and time
from FFlibs.Globster import *
class FileInfo():
    def __init__(self):
        pass 
    # Function to convert file size to GB
    def convert_to_gb(self, size_in_bytes):
        size_In_GB =  size_in_bytes / (1024 * 1024 * 1024)
        sizeinGB = float("{:.2f}".format(size_In_GB))
        return sizeinGB

    def clean_file_name(self, file_name, substring):
        cleaned_name = file_name.replace(substring, '')
        return cleaned_name
    
    def do_basic_replacements (self,file_name):
        cleaned_name = file_name.replace("."," ").replace("_"," ")
        cleaned_name = ' '.join(cleaned_name.split())
        return cleaned_name.title()
    # Function to get file details
# Function to get file details
    def get_file_details(self,dir_path, isCleaningRequired, substring = ""):
        totalSize = 0 
        if isCleaningRequired == "Y":
            print(f"Substring to be cleaned {substring}")
            data = []
        
            for root, dirs, files in os.walk(dir_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    size_in_gb = FileInfo().convert_to_gb(os.path.getsize(file_path))
                    file_type = os.path.splitext(file)[1]
                    cleaned_name = FileInfo().clean_file_name(file, substring)
                    totalSize += size_in_gb
                    data.append([file_path, cleaned_name, size_in_gb, file_type])
            return data,root,totalSize
        else:
            # print("Reached Else Loop")
            data = []
            for root, dirs, files in os.walk(dir_path):
                for file in files:
                    # print(file)
                    file_path = os.path.join(root, file)
                    size_in_gb = FileInfo().convert_to_gb(os.path.getsize(file_path))
                    file_type = os.path.splitext(file)[1]
                    fileName = os.path.splitext(file)[0]
                    totalSize += size_in_gb
                    
                    # print(fileName)
                    cleaned_name = FileInfo().do_basic_replacements(fileName)
                    data.append([file_path, cleaned_name, size_in_gb, file_type])
            return data,root,totalSize
            
    def convertListIntoDataframe(self, InputList, Cols):
        dataFrame = pd.DataFrame(InputList, columns=Cols)
        return dataFrame
        
    def getFileDetails(self,dir_path,isCleaningRequired):
        data,root,totalSize = FileInfo().get_file_details(dir_path,isCleaningRequired)
        columns=['File Path', 'movieName_Disk','Size (GB)', 'File Type']
        df_FileDetails = FileInfo().convertListIntoDataframe(data, columns)
        movieNamesList = df_FileDetails['movieName_Disk'].tolist()
        return df_FileDetails,movieNamesList

    def getIMDBInfo(self,MovieList):
        ia = imdb.IMDb()
        LST_iMDB_MovieCode_YR_Genre = []
        for movie in MovieList:
            try:
                search = ia.search_movie(movie)
                movie_code = search[0].movieID
                # movieNameIMDB = ia.get_movie(movie_code)
                # actor = movieNameIMDB['cast']
                series = ia.get_movie(movie_code)
                Title = series.data['title']
                year = series.data['year']
                genres = series.data['genres']
                print(f"IMDB Code : {movie_code}, Title: {Title}, Year: {year},Genre: {genres}")
                LST_iMDB_MovieCode_YR_Genre.append([movie,movie_code,Title,year,genres])
            except Exception as e:
                print(f"MovieName : {movie} with Error {e}")
                continue
        return LST_iMDB_MovieCode_YR_Genre
    
    def FormatNdDeliver(self,FilePather,isCleaningRequired,DISINSERTED):
        df_FileDetails,movieNamesList = FileInfo().getFileDetails(FilePather,isCleaningRequired)
        LST_iMDB_MovieCode_YR_Genre = FileInfo().getIMDBInfo(movieNamesList)
        col_iMDB_MovieCode_YR_Genre = ["movieName_Disk","movieCode_IMDB","Title_IMDB","Year_IMDB","Genres_IMDB"]
        # Create a dataframe
        df = pd.DataFrame(LST_iMDB_MovieCode_YR_Genre, columns=col_iMDB_MovieCode_YR_Genre)
        # Assuming df1 and df2 are your dataframes and 'FileName' is your column
        merged_df = pd.merge(df_FileDetails,df, left_index=False, how='inner', on='movieName_Disk')
        print(f"########Disk Inserted : {DISINSERTED}##########")
        print("#################################################")
        merged_df['Classified'] = DISINSERTED
        FileNametoWrite = os.path.basename(FilePather) + ".csv"
        merged_df.to_csv(Globster().SavePath + FileNametoWrite, encoding='utf-8',index=False)
        return merged_df

# FilePather = r"D:\Simply_Movies\Bolly\Simply_Up_2_Date\Alphabet P"
# FilePather = r"D:\Simply_Movies\Bolly\Simply_Up_2_Date\OrganizedAdditionAfterFeb2024\2_F"
FilePather = r"D:\Simply_Movies\Bolly\2024_MoviesHut"
DiskNames = ["Bollywood","Series","Eng01","Eng02"]
DISINSERTED = DiskNames[0]
FileInfo().FormatNdDeliver(FilePather,"N",DISINSERTED)
