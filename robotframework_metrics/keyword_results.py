from robot.api import ResultVisitor


class KeywordResults(ResultVisitor):

    # referece - https://robot-framework.readthedocs.io/en/stable/autodoc/robot.result.html

    def __init__(self, kw_list, ignore_library):
        self.kw_list = kw_list
        self.ignore_library = ignore_library
    
    def start_test(self, test):
        self.test = test

    def end_test(self, test):
        self.test = None
    
    def start_keyword(self, kw):
        if kw.type == "KEYWORD" and (kw.libname not in self.ignore_library):
            kw_json = {
                "TestName" : self.test.name,
                "Name" : kw.name,
                "Status" : kw.status,
                "Time" : kw.elapsedtime
            }
            self.kw_list.append(kw_json)