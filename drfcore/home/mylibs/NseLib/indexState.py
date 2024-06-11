import sys
from pathlib import Path
path = Path('C:/SIMPLY_Official/2024/TechHome241/')
sys.path.append(str(path.resolve()))
from drfcore.home.mylibs.NseLib.initiateRequest import *
import pandas as pd

class indexState:
    def __init__(self):
        pass
    # self.con = DbConnections().connectToDB()
    def nse_get_index_list(self):
        payload = initiateRequest().establishConnection('https://iislliveblob.niftyindices.com/jsonfiles/LiveIndicesWatch.json')
        payload = pd.DataFrame(payload["data"])
        return payload["indexName"].tolist()

indexState().nse_get_index_list()