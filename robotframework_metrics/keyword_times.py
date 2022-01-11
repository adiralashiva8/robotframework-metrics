from pandas import json_normalize

class KeywordTimes():

    def __init__(self, kw_list, kw_times):
        self.kw_list = kw_list
        self.kw_times = kw_times
    
    def capture_times(self):
        df = json_normalize(self.kw_list)
        print(df)