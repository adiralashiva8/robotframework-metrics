from robot.api import ResultVisitor
from robot.utils.markuputils import html_format


class TestResults(ResultVisitor):

    def __init__(self, test_list):
        self.test_list = test_list
    
    def visit_test(self, test):
        suite_name = test.parent if test.parent else test.parent.name
        test_json = {
            "Suite Name" : suite_name,
            "Test Name" : test.name,
            "Test Id" : test.id,
            "Status" : test.status,
            "Documentation" : html_format(test.doc),
            "Time" : test.elapsedtime,
            # "Message" : html_format(test.message),
            "Message" : str(test.message).replace("*HTML*",""),
            "Tags" : test.tags 
        }
        self.test_list.append(test_json)
