
import os,time,datetime

class Globster():
    def __init__(self):
        pass 
    
    def getSQLconnection(self):
        SQL_URL = r'C:\SIMPLY_Official\2024\TechHome241\drfcore'
        
    SQL_URL = r'C:\SIMPLY_Official\2024\TechHome24\drfcore'
    SavePath = r"C:\SIMPLY_Official\2024\TechHome24\drfcore\FarFlix\data\\"
    SaveMovieDetailsIMDB = r"C:\SIMPLY_Official\2024\TechHome24\drfcore\FarFlix\data\MovieDetailsFromIMDB\\"
    
    def returnBasePath(self):
        return os.path.dirname(os.path.abspath(__file__))

# print(Globster().returnBasePath())