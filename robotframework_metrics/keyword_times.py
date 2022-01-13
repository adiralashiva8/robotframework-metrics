import pandas as pd

class KeywordTimes():

    def get_keyword_times(self, kw_list):
        keywords_data_frame = pd.DataFrame.from_records(kw_list)
        kw_times = (keywords_data_frame.groupby("Name").agg(times = ("Time", "count"), time_min = ("Time", min),
         time_max = ("Time", max), time_mean = ("Time", "mean")).reset_index())
        
        return kw_times