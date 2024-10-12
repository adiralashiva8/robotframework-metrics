import pandas as pd


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

    def group_error_messages(self, test_list):
        test_data_frame = pd.DataFrame.from_records(test_list)
        grouped_data_frame = (
            test_data_frame.groupby("Message", as_index=False)  # Keep 'Message' as a column
            .agg(times=("Status", "count"))  # Count occurrences of each 'Status'
            .sort_values(by=['times'], ascending=False, ignore_index=True)  # Sort by count
        )

        return grouped_data_frame.head(6)
        # return (test_data_frame.groupby("Message", as_index=False).agg(times = ("Status", "count")).head(6).reset_index()).sort_values(by = ['times'], ascending = [False], ignore_index=True)

    def suite_error_statistics(self, suite_list):
        suite_data_frame = pd.DataFrame.from_records(suite_list)
        required_data_frame = pd.DataFrame(suite_data_frame, columns = ['Name', 'Total', 'Fail'])
        required_data_frame['percent'] = (required_data_frame['Fail'] / required_data_frame['Total'])*100
        filtered_data_frame = required_data_frame[required_data_frame['Fail'] > 0]
        # print(required_data_frame)
        return filtered_data_frame.sort_values(by = ['Fail'], ascending = [False], ignore_index=True).head(10).reset_index(drop=True)
