from robot.api import ResultVisitor


class TestStats(ResultVisitor):
    total_suite = 0
    passed_suite = 0
    failed_suite = 0

    def start_suite(self, suite):
        suite_test_list = suite.tests
        if not suite_test_list:
            pass
        else:
            self.total_suite += 1

            if suite.status == "PASS":
                self.passed_suite += 1
            else:
                self.failed_suite += 1
