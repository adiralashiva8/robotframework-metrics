import os
from robot.api import ExecutionResult
from jinja2 import Environment, FileSystemLoader
from suite_results import SuiteResults
from test_results import TestResults
from keyword_results import KeywordResults
from keyword_times import KeywordTimes
from dashboard_stats import Dashboard

templates_dir = os.path.join(os.getcwd(), 'templates')
env = Environment( loader = FileSystemLoader(templates_dir) )
template = env.get_template('index.html')

filename = 'index.html'
ignore_library = ["SeleniumLibrary", "BuiltIn",
 "Collections", "DateTime", "Dialogs", "OperatingSystem"
 "Process", "Screenshot", "String", "Telnet", "XML"]
suite_list, test_list, kw_list, kw_times = [], [], [], []

result = ExecutionResult('output.xml')
result.visit(SuiteResults(suite_list))
result.visit(TestResults(test_list))
result.visit(KeywordResults(kw_list, ignore_library))
kw_times = KeywordTimes().get_keyword_times(kw_list)

dashboard_obj = Dashboard()
suite_stats = dashboard_obj.get_suite_statistics(suite_list)
test_stats = dashboard_obj.get_test_statistics(test_list)
kw_stats = dashboard_obj.get_keyword_statistics(kw_list)
error_stats = dashboard_obj.group_error_messages(test_list)

with open(filename, 'w') as fh:
    fh.write(template.render(
        suite_stats = suite_stats,
        test_stats = test_stats,
        kw_stats = kw_stats,
        suites = suite_list,
        tests = test_list,
        keywords = kw_list,
        keyword_times = kw_times,
        error_stats = error_stats
    ))