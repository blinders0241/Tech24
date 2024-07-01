from pathlib import Path
import os,sys
import time
BASE_DIR = str(Path(__file__).resolve().parent.parent)
# Define the path to the parent directory of drfcore
path = Path('C:/SIMPLY_Official/2024/TechHome24/')
# Add the path to sys.path
sys.path.append(str(path.resolve()))
# Now you should be able to import the module
from drfcore.home.mylibs.GlobsterHome import *
from FileExtractor import *

nifty_200_symbols = GlobsterHome().EquitySctocks_JAN24_752  # Replace with your list of Nifty 200 symbols
#Raw File Path
raw_file_path = BASE_DIR +os.sep+ 'data' +os.sep+ 'RawFile' +os.sep+ 'Ongoing'
#OutPut Paths
output_path_cm = BASE_DIR +os.sep+ 'data' +os.sep+ 'ReadyBhavFile' +os.sep+ 'Equity'
output_path_fo = BASE_DIR +os.sep+ 'data' +os.sep+ 'ReadyBhavFile' +os.sep+ 'Derivatives'

class FormatNdDeliver:
    """
    This class handles the formatting and delivery of files.

    Methods:
    - getExtractedFiles: Retrieves and processes extracted files.
    """

    def __init__(self):
        pass
    
    def getExtractedFiles(self):
        """
        Retrieves and processes extracted files.

        Returns:
        - ReurnMsg: Message indicating the result of processing files.
        - ReurnMsgEquity: Message indicating the result of processing equity files.
        """
        print("################ Reached getExtractedFiles ################################")
        print(raw_file_path)
        extractedFiles = FileExtractor().extractZipFiles(raw_file_path)
        ReurnMsg = FileExtractor().processFiles(raw_file_path,extractedFiles,output_path_fo)
        ReurnMsgEquity = FileExtractor().processEquityFiles(raw_file_path,extractedFiles,output_path_cm,nifty_200_symbols)
        # # Move the extracted files to the 'completed' directory
        # Create a 'completed' directory if it doesn't exist
        completed_dir = Path(raw_file_path) / 'completed'
        completed_dir.mkdir(exist_ok=True)
        for file_name in extractedFiles:
            try:
                shutil.move(os.path.join(raw_file_path, file_name), completed_dir)
                print("Extracted files move to completed folder")
            except Exception as e:
                print(e)
        print("################### Success #############################")
        # print(ReurnMsg, ReurnMsgEquity)
        return ReurnMsg, ReurnMsgEquity

FormatNdDeliver().getExtractedFiles()