from robot.api import ResultVisitor


class KeywordStats(ResultVisitor):
    total_keywords = 0
    passed_keywords = 0
    failed_keywords = 0
    skipped_keywords = 0

    def __init__(self, ignore_type):
        self.ignore_type = ignore_type

    def start_keyword(self, kw):

        keyword_type = kw.type
        if any(library in keyword_type for library in self.ignore_type):
            pass
        else:
            self.total_keywords += 1
            if kw.status == "PASS":
                self.passed_keywords += 1
            elif kw.status == "FAIL":
                self.failed_keywords += 1
            else:
                self.skipped_keywords += 1
