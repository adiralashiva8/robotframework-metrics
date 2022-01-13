from robot.api import ResultVisitor


class SuiteResults(ResultVisitor):

    def __init__(self, suite_list):
        self.suite_list = suite_list
    
    def start_suite(self, suite):
        if suite.tests:
            try:
                stats = suite.statistics.all
            except:
                stats = suite.statistics
            
            try:
                skipped = stats.skipped
            except:
                skipped = 0

            suite_json = {
                "Name" : suite.longname,
                "Status" : suite.status,
                "Total" : stats.total,
                "Pass" : stats.passed,
                "Fail" : stats.failed,
                "Skip" : skipped,
                "Time" : suite.elapsedtime,
            }
            self.suite_list.append(suite_json)