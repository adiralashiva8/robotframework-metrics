import pandas as pd
from datetime import datetime
import numpy as np


class Dashboard:

    def __init__(self):
        pass

    @classmethod
    def get_suite_statistics(self, suite_list):
        suite_data_frame = pd.DataFrame.from_records(suite_list)
        suite_stats = {
            "Total" : (suite_data_frame.Name).count(),
            "Pass"  : (suite_data_frame.Status == 'PASS').sum(),
            "Fail"  : (suite_data_frame.Status == 'FAIL').sum(),
            "Skip"  : (suite_data_frame.Status == 'SKIP').sum(),
            "Time"  : (suite_data_frame.Time).sum(),
            "Min"  : (suite_data_frame.Time).min(),
            "Max"  : (suite_data_frame.Time).max(),
            "Avg"  : (suite_data_frame.Time).mean()
        }
        return suite_stats
    
    @classmethod
    def get_test_statistics(self, test_list):
        test_data_frame = pd.DataFrame.from_records(test_list)
        test_stats = {
            "Total" : (test_data_frame.Status).count(),
            "Pass"  : (test_data_frame.Status == 'PASS').sum(),
            "Fail"  : (test_data_frame.Status == 'FAIL').sum(),
            "Skip"  : (test_data_frame.Status == 'SKIP').sum(),
            "Time"  : (test_data_frame.Time).sum(),
            "Min"  : (test_data_frame.Time).min(),
            "Max"  : (test_data_frame.Time).max(),
            "Avg"  : (test_data_frame.Time).mean()
        }
        return test_stats

    @classmethod
    def get_keyword_statistics(self, kw_list):
        kw_data_frame = pd.DataFrame.from_records(kw_list)
        if not kw_data_frame.empty:
            kw_stats = {
                "Total" : (kw_data_frame.Status).count(),
                "Pass"  : (kw_data_frame.Status == 'PASS').sum(),
                "Fail"  : (kw_data_frame.Status == 'FAIL').sum(),
                "Skip"  : (kw_data_frame.Status == 'SKIP').sum()
            }
        else:
            kw_stats = {
                "Total" : 0,
                "Pass"  : 0,
                "Fail"  : 0,
                "Skip"  : 0,
            }
        return kw_stats

    def suite_error_statistics(self, suite_list):
        suite_data_frame = pd.DataFrame.from_records(suite_list)
        required_data_frame = pd.DataFrame(suite_data_frame, columns = ['Name', 'Total', 'Fail'])
        required_data_frame['percent'] = (required_data_frame['Fail'] / required_data_frame['Total'])*100
        filtered_data_frame = required_data_frame[required_data_frame['Fail'] > 0]
        # print(required_data_frame)
        return filtered_data_frame.sort_values(by = ['Fail'], ascending = [False], ignore_index=True).head(10).reset_index(drop=True)

    def get_execution_info(self, test_list):
        data_frame = pd.DataFrame.from_records(test_list)
        data_frame['start_time'] = pd.to_datetime(data_frame['start_time'])
        data_frame['end_time'] = pd.to_datetime(data_frame['end_time'])
        initial_start_time = data_frame['start_time'].min()
        final_end_time = data_frame['end_time'].max()
        overall_execution_time = final_end_time - initial_start_time
        return [initial_start_time, final_end_time, overall_execution_time]

    def get_test_execution_trends(self, test_list):
        data_frame = pd.DataFrame.from_records(test_list)
        num_bins = 10
        min_time = round(data_frame['Time'].min()/60000, 2)
        max_time = round(data_frame['Time'].max()/60000, 2)
        if max_time == min_time:
            max_time += 0.1
        bins = np.linspace(min_time, max_time, num_bins + 1)
        labels = [f'{round(bins[i], 0)} - {round(bins[i+1], 0)} min' for i in range(len(bins)-1)]
        data_frame['time_group'] = pd.cut(round(data_frame['Time']/60000,2), bins=bins, labels=labels, include_lowest=True, ordered=False)
        result = data_frame.groupby('time_group').size().reset_index(name='test_case_count')
        return result
