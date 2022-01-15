from robot.api import ResultVisitor


class TestResults(ResultVisitor):

    def __init__(self, test_list):
        self.test_list = test_list
    
    def visit_test(self, test):
        test_json = {
            "Suite Name" : test.parent,
            "Test Name" : test,
            "Status" : test.status,
            "Time" : test.elapsedtime,
            "Message" : test.message,
            "Tags" : test.tags 
        }
        self.test_list.append(test_json)