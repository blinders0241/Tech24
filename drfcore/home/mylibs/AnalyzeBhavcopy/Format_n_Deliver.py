import json

class Format_n_Deliver:

    def __init__(self):
        pass
    def getJsonbySourceFile(data_frame):
        # convert_2_dataFrame_withDuplicates = df = learnData.convert_2_dataFrame_withDuplicates(data_frame)
        # dataFramewithFeatures = Format_n_Deliver().get_mappeddataframe(convert_2_dataFrame_withDuplicates)
        hdr = ['SYMBOL', 'OPEN', 'HIGH', 'LOW', 'CLOSE', 'VOLUME', 'OPEN_INT', 'CHG_IN_OI', 'TIMESTAMP']
        df_json = data_frame[hdr]
        json_data = df_json.to_json(orient='records')
        json_obj = json.loads(json_data)
        return json_obj
        # print("Format and Deliver")