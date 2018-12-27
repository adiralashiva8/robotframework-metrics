from robot.api import ResultVisitor


class KeywordStats(ResultVisitor):
    total_keywords = 0
    passed_keywords = 0
    failed_keywords = 0

    def __init__(self, ignore_library, ignore_type):
        self.ignore_library = ignore_library
        self.ignore_type = ignore_type

    def start_keyword(self, kw):
        # Ignore library keywords
        keyword_library = kw.libname

        if any(library in keyword_library for library in self.ignore_library):
            pass
        else:
            keyword_type = kw.type
            if any(library in keyword_type for library in self.ignore_type):
                pass
            else:
                self.total_keywords += 1
                if kw.status == "PASS":
                    self.passed_keywords += 1
                else:
                    self.failed_keywords += 1
