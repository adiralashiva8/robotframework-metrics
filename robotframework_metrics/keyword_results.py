from robot.api import ResultVisitor


class KeywordResults(ResultVisitor):

    def __init__(self, kw_list, ignore_library, ignore_type):
        self.kw_list = kw_list
        self.ignore_library = ignore_library
        self.ignore_type = ignore_type
        
    def start_keyword(self, kw):
        if (kw.libname not in self.ignore_library) and (kw.type not in self.ignore_type):
            kw_json = {
                "Name" : kw.name,
                "Status" : kw.status,
                "Time" : kw.elapsedtime
            }
            self.kw_list.append(kw_json)