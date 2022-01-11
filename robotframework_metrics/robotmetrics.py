import os
import pandas as pd
import numpy as np
from robot.api import ExecutionResult
from suite_results import SuiteResults
from test_results import TestResults
from keyword_results import KeywordResults
from jinja2 import Environment, FileSystemLoader


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

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

df = pd.DataFrame.from_records(kw_list)
kw_times = (df.groupby("Name").agg(times = ("Time", "count"), time_min = ("Time", min),
 time_max = ("Time", max), time_mean = ("Time", "mean")).reset_index())

with open(filename, 'w') as fh:
    fh.write(template.render(
        time = "10h",
        suites = suite_list,
        tests = test_list,
        keywords = kw_list,
        keyword_times = kw_times
    ))