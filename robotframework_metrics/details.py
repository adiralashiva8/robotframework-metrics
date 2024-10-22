from robot.api import ExecutionResult, ResultVisitor
from datetime import timedelta
from robot.result.model import Keyword


class SuiteReportVisitor(ResultVisitor):
    def __init__(self, details_list):
        self.test_report = details_list

    def visit_suite(self, suite):

        self.tests = []
        self.keywords = []
        # Traverse each test in the suite
        for test in suite.tests:

            # Traverse each keyword in the test
            for keyword in test.body:
                if isinstance(keyword, Keyword):
                    _current_keyword = {
                        'keyword_name': keyword.name,
                        'keyword_status': keyword.status,
                        'keyword_start_time': keyword.starttime,
                        'keyword_end_time': keyword.endtime,
                        'keyword_elapsed_time': str(timedelta(milliseconds=keyword.elapsedtime)),
                        'keyword_documentation': keyword.doc,
                        'keyword_message': keyword.message if keyword.message else "",
                    }
                    self.keywords.append(_current_keyword)

            _current_test = {
                'test_name': test.name,
                'test_id': test.id,
                'start_time': test.starttime,
                'end_time': test.endtime,
                'elapsed_time': str(timedelta(milliseconds=test.elapsedtime)),
                'status': test.status,
                'tags': ", ".join(test.tags),
                'documentation': test.doc,
                'message': test.message if test.message else "",
                'keywords': self.keywords
            }
            self.tests.append(_current_test)


        tests_info = {
            'suite_name': suite.longname,
            'suite_id': suite.id,
            'start_time': suite.starttime,
            'end_time': suite.endtime,
            'elapsed_time': str(timedelta(milliseconds=suite.elapsedtime)),
            'status': suite.status,
            'pass_count': suite.statistics.passed,
            'fail_count': suite.statistics.failed,
            'skip_count': suite.statistics.skipped,
            'total': suite.statistics.total,
            'message': suite.message if suite.message else "",
            'tests': self.tests
        }

        self.test_report.append(tests_info)

        # Recursively visit nested suites
        for child_suite in suite.suites:
            child_suite.visit(self)
