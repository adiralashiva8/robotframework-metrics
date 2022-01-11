from robot.api import ResultVisitor


class SuiteResults(ResultVisitor):

    # referece - https://robot-framework.readthedocs.io/en/stable/autodoc/robot.result.html

    def __init__(self, suite_list):
        self.suite_list = suite_list
    
    def start_suite(self, suite):
        if suite.tests:
            try:
                stats = suite.statistics.all
            except:
                stats = suite.statistics
            suite_json = {
                "Name" : suite.longname,
                "Status" : suite.status,
                "Total" : stats.total,
                "Pass" : stats.passed,
                "Fail" : stats.failed,
                "Skip" : stats.skipped if stats.skipped is not None else 0,
                "Time" : suite.elapsedtime,
            }
            self.suite_list.append(suite_json)