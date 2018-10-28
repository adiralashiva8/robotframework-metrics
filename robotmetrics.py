#!/usr/bin/env python
from __future__ import print_function
import sys
import os
import math
import smtplib
import time
from bs4 import BeautifulSoup
from datetime import datetime
from datetime import timedelta
from robot.api import ExecutionResult, ResultVisitor
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders

# ======================== START OF CUSTOMIZE REPORT ================================== #

# URL or filepath of your company logo
logo = "https://cdn.pixabay.com/photo/2016/08/02/10/42/wifi-1563009_960_720.jpg"

# Ignores following library keywords in metrics report
ignore_library = [
    'BuiltIn',
    'SeleniumLibrary',
    'String',
    'Collections',
    'DateTime',
    ]

# Ignores following type keywords in metrics report
ignore_type = [
    'foritem',
    'for',
    ]

# ======================== END OF CUSTOMIZE REPORT ================================== #

# Report to support file location as arguments
# Source Code Contributed By : Ruud Prijs
def getopts(argv):
        opts = {}
        while argv:
            if argv[0][0] == '-':
                if argv[0] in opts:
                    opts[argv[0]].append(argv[1])
                else:
                    opts[argv[0]] = [argv[1]]
            argv = argv[1:]
        return opts

myargs = getopts(sys.argv)

# input directory
if '-inputpath' in myargs:
    path = os.path.abspath(os.path.expanduser(myargs['-inputpath'][0]))
else:
    path = os.path.curdir

# report.html file
if '-report' in myargs:
    report_name = myargs['-report'][0]
else:
    report_name = 'report.html'

# log.html file
if '-log' in myargs:
    log_name = myargs['-log'][0]
else:
    log_name = 'log.html'

# output.xml file
if '-output' in myargs:
    output_name = os.path.join(path,myargs['-output'][0])
else:
    output_name = os.path.join(path,'output.xml')

# email status
if '-email' in myargs:
    send_email = myargs['-email'][0]
else:
    send_email = True

mtTime = datetime.now().strftime('%Y%m%d-%H%M%S')
# Output result file location
result_file_name = 'metrics-'+ mtTime + '.html'
result_file = os.path.join(path,result_file_name)

# Read output.xml file
result = ExecutionResult(output_name)
result.configure(stat_config={'suite_stat_level': 2,
                              'tag_stat_combine': 'tagANDanother'})

							  
print("Converting .xml to .html file. This may take few minutes...")

# ======= START OF EMAIL SETUP CONTENT ====== #
if send_email in ['true', '1', 't', 'y', 'yes']:
    server = smtplib.SMTP('smtp.gmail.com:587')

msg = MIMEMultipart() 
msg['Subject'] = 'MyProject Automation Status'

sender = 'me@gmail.com'
recipients = ['user1@gmail.com', 'user2@yahoo.com']
ccrecipients = ['user3@gmail.com', 'user4@yahoo.com']

msg['From'] = sender
msg['To'] = ", ".join(recipients)
msg['Cc'] = ", ".join(ccrecipients)
password = "*************"
msg.add_header('Content-Type', 'text/html')

# ======= END OF EMAIL SETUP CONTENT ====== #

head_content = """
<!doctype html>
<html lang="en">

<head>
    <link rel="shortcut icon" href="https://png.icons8.com/windows/50/000000/bot.png" type="image/x-icon" />
    <title>RF Metrics Report</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="viewport" content="width=device-width, initial-scale=1">

	<link href="https://cdn.datatables.net/1.10.19/css/jquery.dataTables.min.css" rel="stylesheet"/>
	<link href="https://cdn.datatables.net/buttons/1.5.2/css/buttons.dataTables.min.css" rel="stylesheet"/>

    <link href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.1.3/css/bootstrap.min.css" rel="stylesheet"/>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet">
    
   <script src="https://code.jquery.com/jquery-3.3.1.js" type="text/javascript"></script>
   
    <!-- Bootstrap core Googleccharts -->
   <script src="https://www.gstatic.com/charts/loader.js" type="text/javascript"></script>
   <script type="text/javascript">google.charts.load('current', {packages: ['corechart']});</script>

   <!-- Bootstrap core Datatable-->
	<script src="https://code.jquery.com/jquery-3.3.1.js" type="text/javascript"></script>
	<script src="https://cdn.datatables.net/1.10.19/js/jquery.dataTables.min.js" type="text/javascript"></script>
	<script src="https://cdn.datatables.net/buttons/1.5.2/js/dataTables.buttons.min.js" type="text/javascript"></script>
	<script src="https://cdn.datatables.net/buttons/1.5.2/js/buttons.flash.min.js" type="text/javascript"></script>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/jszip/3.1.3/jszip.min.js" type="text/javascript"></script>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/pdfmake/0.1.36/pdfmake.min.js" type="text/javascript"></script>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/pdfmake/0.1.36/vfs_fonts.js" type="text/javascript"></script>
	<script src="https://cdn.datatables.net/buttons/1.5.2/js/buttons.html5.min.js" type="text/javascript"></script>
	<script src="https://cdn.datatables.net/buttons/1.5.2/js/buttons.print.min.js" type="text/javascript"></script>

    <style>        
        .sidebar {
          position: fixed;
          top: 0;
          bottom: 0;
          left: 0;
          z-index: 100; /* Behind the navbar */
          box-shadow: inset -1px 0 0 rgba(0, 0, 0, .1);
        }
        
        .sidebar-sticky {
          position: relative;
          top: 0;
          height: calc(100vh - 48px);
          padding-top: .5rem;
          overflow-x: hidden;
          overflow-y: auto; /* Scrollable contents if viewport is shorter than content. */
        }
        
        @supports ((position: -webkit-sticky) or (position: sticky)) {
          .sidebar-sticky {
            position: -webkit-sticky;
            position: sticky;
          }
        }
        
        .sidebar .nav-link {
          color: black;
        }
        
        .sidebar .nav-link.active {
          color: #007bff;
        }
        
        .sidebar .nav-link:hover .feather,
        .sidebar .nav-link.active .feather {
          color: inherit;
        }

        [role="main"] {
          padding-top: 8px;
        }
        
		/* Set height of body and the document to 100% */
		body {
			height: 100%;
			margin: 0;
			//font-family:  Comic Sans MS;
			background-color: white;
		}

		/* Style tab links */
		.tablinkLog {
			cursor: pointer;
		}
		
        @import url(https://fonts.googleapis.com/css?family=Droid+Sans);
		.loader {
			position: fixed;
			left: 0px;
			top: 0px;
			width: 100%;
			height: 100%;
			z-index: 9999;
			background: url('http://www.downgraf.com/wp-content/uploads/2014/09/01-progress.gif?e44397') 50% 50% no-repeat rgb(249,249,249);
		}

		/* TILES */
		.tile {
		  width: 100%;
		  float: left;
		  margin: 0px;
		  list-style: none;
		  font-size: 30px;
		  color: #FFF;
		  -moz-border-radius: 5px;
		  -webkit-border-radius: 5px;
		  margin-bottom: 5px;
		  position: relative;
		  text-align: center;
		  color: white!important;
		}

		.tile.tile-fail {
		  background: #f44336!important;
		}
		.tile.tile-pass {
		  background: #4CAF50!important;
		}
		.tile.tile-info {
		  background: #009688!important;
		}
		.tile.tile-head {
		  background: #616161!important;
		}
        .dt-buttons {
            margin-left: 5px;
        }
    </style>
</head>
"""

soup = BeautifulSoup(head_content,"html.parser")

body = soup.new_tag('body')
soup.insert(20, body)

icons_txt= """
<div class="loader"></div>
 <div class="container-fluid">
        <div class="row">
            <nav class="col-md-2 d-none d-md-block bg-light sidebar" style="font-size:16px;">
                <div class="sidebar-sticky">
                    <ul class="nav flex-column">                            
                  <img src="%s" style="height:18vh!important;width:95%%;"/>
                
				<br>
				
				<h6 class="sidebar-heading d-flex justify-content-between align-items-center text-muted">
                        <span>Metrics</span>
                        <a class="d-flex align-items-center text-muted" href="#"></a>
                    </h6>

                        <li class="nav-item">
                            <a class="tablink nav-link" href="#" id="defaultOpen" onclick="openPage('dashboard', this, 'orange')">
								<i class="fa fa-dashboard"></i> Dashboard
							</a>
                        </li>
                        <li class="nav-item">
                            <a class="tablink nav-link" href="#" onclick="openPage('suiteMetrics', this, 'orange');executeDataTable('#sm',5)" >
								<i class="fa fa-th-large"></i> Suite Metrics
							</a>
                        </li>
                        <li class="nav-item">
                            <a class="tablink nav-link" href="#" onclick="openPage('testMetrics', this, 'orange');executeDataTable('#tm',3)">
							  <i class="fa fa-list-alt"></i> Test Metrics
							</a>
                        </li>
                        <li class="nav-item">
                            <a class="tablink nav-link" href="#" onclick="openPage('keywordMetrics', this, 'orange');executeDataTable('#km',3)">
							  <i class="fa fa-table"></i> Keyword Metrics
							</a>
                        </li>
                        <li class="nav-item">
                            <a class="tablink nav-link" href="#" onclick="openPage('log', this, 'orange');">
							  <i class="fa fa-wpforms"></i> Robot Logs
							</a>
                        </li>
                        <li class="nav-item">
                            <a class="tablink nav-link" href="#" onclick="openPage('statistics', this, 'orange');">
							  <i class="fa fa-envelope-o"></i> Email Metrics
							</a>
                        </li>
                    </ul>
					<h6 class="sidebar-heading d-flex justify-content-between align-items-center text-muted">
                        <span>Project</span>
                        <a class="d-flex align-items-center text-muted" href="#"></a>
                    </h6>
                    <ul class="nav flex-column mb-2">
                        <li class="nav-item">
                            <a style="color:blue;" class="tablink nav-link" target="_blank" href="https://www.github.com">
							  <i class="fa fa-external-link"></i> Git Hub
							</a>
                        </li>
						<li class="nav-item">
                            <a style="color:blue;" class="tablink nav-link" target="_blank" href="https://www.jira.com">
							  <i class="fa fa-external-link"></i> JIRA
							</a>
                        </li>
                    </ul>
                </div>
            </nav>
        </div>
"""%(logo)

body.append(BeautifulSoup(icons_txt, 'html.parser'))


page_content_div = soup.new_tag('div')
page_content_div["role"] = "main"
page_content_div["class"] = "col-md-9 ml-sm-auto col-lg-10 px-4"
body.insert(50, page_content_div)

print("1 of 6: Capturing dashboard content...")
### ============================ START OF DASHBOARD ======================================= ####
total_suite = 0
passed_suite = 0
failed_suite = 0

class SuiteResults(ResultVisitor):
    
    def start_suite(self,suite):
       
        suite_test_list = suite.tests
        if not suite_test_list:
            pass
        else:        
            global total_suite
            total_suite+= 1
            if suite.status== "PASS":
                global passed_suite
                passed_suite+= 1
            else:
                global failed_suite
                failed_suite += 1

result.visit(SuiteResults())
suitepp = math.ceil(passed_suite*100.0/total_suite)

elapsedtime = datetime(1970, 1, 1) + timedelta(milliseconds=result.suite.elapsedtime)
elapsedtime = elapsedtime.strftime("%X")

myResult = result.generated_by_robot

if myResult:
	generator = "Robot"
else:
	generator = "Rebot"
	
stats = result.statistics
total= stats.total.all.total
passed= stats.total.all.passed
failed= stats.total.all.failed

testpp = round(passed*100.0/total,2)

total_keywords = 0
passed_keywords = 0
failed_keywords = 0

class KeywordResults(ResultVisitor):
    
    def start_keyword(self,kw):
        # Ignore library keywords
        keyword_library = kw.libname

        if any (library in keyword_library for library in ignore_library):
            pass
        else:
            keyword_type = kw.type            
            if any (library in keyword_type for library in ignore_type):
                pass
            else:
                global total_keywords
                total_keywords+= 1
                if kw.status== "PASS":
                    global passed_keywords
                    passed_keywords+= 1
                else:
                    global failed_keywords
                    failed_keywords += 1

result.visit(KeywordResults())

# Handling ZeroDivisionError exception when no keywords are found
if total_keywords > 0:
    kwpp = round(passed_keywords*100.0/total_keywords,2)
else:
    kwpp = 0

dashboard_content="""
<div class="tabcontent" id="dashboard">
			
				<div class="d-flex flex-column flex-md-row align-items-center p-1 mb-3 bg-light border-bottom shadow-sm">
				  <h5 class="my-0 mr-md-auto font-weight-normal"><i class="fa fa-dashboard"></i> Dashboard</h5>
				  <nav class="my-2 my-md-0 mr-md-3" style="color:red">
					<a class="p-2"><b style="color:black;">Execution Time: </b>%s h</a>
					<a class="p-2"><b style="color:black;cursor: pointer;" data-toggle="tooltip" title=".xml file is created by">Generated By: </b>%s</a>
				  </nav>                  
				</div>
			
				<div class="row">
					<div class="col-md-3"  onclick="openPage('suiteMetrics', this, '')" data-toggle="tooltip" title="Click to view Suite metrics" style="cursor: pointer;">                        
						<a class="tile tile-head">
							Suite
							<p style="font-size:12px">Statistics</p>
						</a>
					</div>
					<div class="col-md-3">                        
						<a class="tile tile-info">
							%s
							<p style="font-size:12px">Total</p>
						</a>
					</div>
					<div class="col-md-3">                        
						<a class="tile tile-pass">
							%s
							<p style="font-size:12px">Pass</p>
						</a>
					</div>						
					<div class="col-md-3">                        
						<a class="tile tile-fail">
							%s
							<p style="font-size:12px">Fail</p>
						</a>
					</div>
                </div>
				
				<div class="row">
					<div class="col-md-3"  onclick="openPage('testMetrics', this, '')" data-toggle="tooltip" title="Click to view Test metrics" style="cursor: pointer;">                        
						<a class="tile tile-head">
							Test
							<p style="font-size:12px">Statistics</p>
						</a>
					</div>
					<div class="col-md-3">                        
						<a class="tile tile-info">
							%s
							<p style="font-size:12px">Total</p>
						</a>
					</div>
					<div class="col-md-3">                        
						<a class="tile tile-pass">
							%s
							<p style="font-size:12px">Pass</p>
						</a>
					</div>						
					<div class="col-md-3">                        
						<a class="tile tile-fail">
							%s
							<p style="font-size:12px">Fail</p>
						</a>
					</div>
                </div>
				
				<div class="row">
					<div class="col-md-3"  onclick="openPage('keywordMetrics', this, '')" data-toggle="tooltip" title="Click to view Keyword metrics" style="cursor: pointer;">                        
						<a class="tile tile-head">
							Keyword
							<p style="font-size:12px">Statistics</p>
						</a>
					</div>
					<div class="col-md-3">                        
						<a class="tile tile-info">
							%s
							<p style="font-size:12px">Total</p>
						</a>
					</div>
					<div class="col-md-3">                        
						<a class="tile tile-pass">
							%s
							<p style="font-size:12px">Pass</p>
						</a>
					</div>						
					<div class="col-md-3">                        
						<a class="tile tile-fail">
							%s
							<p style="font-size:12px">Fail</p>
						</a>
					</div>
                </div>
				
				<hr></hr>
				<div class="row">
					<div class="col-md-4" style="background-color:white;height:280px;width:auto;border:groove;">
						<span style="font-weight:bold">Suite Status:</span>
                        <div id="suiteChartID" style="height:250px;width:auto;"></div>
					</div>
					<div class="col-md-4" style="background-color:white;height:280px;width:auto;border:groove;">
						<span style="font-weight:bold">Test Status:</span>
                        <div id="testChartID" style="height:250px;width:auto;"></div>
					</div>
					<div class="col-md-4" style="background-color:white;height:280px;width:auto;border:groove;">
						<span style="font-weight:bold">Keyword Status:</span>
                        <div id="keywordChartID" style="height:250px;width:auto;"></div>
					</div>
				</div>

                <hr></hr>
				<div class="row">
					<div class="col-md-12" style="background-color:white;height:450px;width:auto;border:groove;">
						<span style="font-weight:bold">Top 10 Suite Performance(sec):</span>
                        <div id="suiteBarID" style="height:400px;width:auto;"></div>
					</div>
					<div class="col-md-12" style="background-color:white;height:450px;width:auto;border:groove;">
						<span style="font-weight:bold">Top 10 Test Performance(sec):</span>
                        <div id="testsBarID" style="height:400px;width:auto;"></div>
					</div>
					<div class="col-md-12" style="background-color:white;height:450px;width:auto;border:groove;">
						<span style="font-weight:bold">Top 10 Keywords Performance(sec):</span>
                        <div id="keywordsBarID" style="height:400px;width:auto;"></div>
					</div>
				</div>
				<div class="row">
				<div class="col-md-12" style="height:25px;width:auto;">
					<p class="text-muted" style="text-align:center;font-size:9px">robotframework-metrics</p>
				</div>
				</div>
   
   <script>
    window.onload = function(){
    executeDataTable('#sm',5);
    executeDataTable('#tm',3);
    executeDataTable('#km',3);
	createPieChart(%s,%s,'suiteChartID','Suite Status:');
	createBarGraph('#sm',0,5,10,'suiteBarID','Elapsed Time(s): ','Suite');	
	createPieChart(%s,%s,'testChartID','Tests Status:');	
	createBarGraph('#tm',1,3,10,'testsBarID','Elapsed Time(s): ','Test'); 
	createPieChart(%s,%s,'keywordChartID','Keywords Status:');
	createBarGraph('#km',1,3,10,'keywordsBarID','Elapsed Time(s): ','Keyword');
	};
   </script>
   <script>
function openInNewTab(url,element_id) {
  var element_id= element_id;
  var win = window.open(url, '_blank');
  win.focus();
  $('body').scrollTo(element_id); 
}
</script>
  </div>
""" % (elapsedtime,generator,total_suite,passed_suite,failed_suite,total,passed,failed,total_keywords,passed_keywords,failed_keywords,passed_suite,failed_suite,passed,failed,passed_keywords,failed_keywords)
page_content_div.append(BeautifulSoup(dashboard_content, 'html.parser'))

### ============================ END OF DASHBOARD ============================================ ####
print("2 of 6: Capturing suite metrics...")
### ============================ START OF SUITE METRICS ======================================= ####

# Tests div
suite_div = soup.new_tag('div')
suite_div["id"] = "suiteMetrics"
suite_div["class"] = "tabcontent"
page_content_div.insert(50, suite_div)

test_icon_txt="""
<h4><b><i class="fa fa-table"></i> Suite Metrics</b></h4>
<hr></hr>
"""
suite_div.append(BeautifulSoup(test_icon_txt, 'html.parser'))

# Create table tag
table = soup.new_tag('table')
table["id"] = "sm"
table["class"] = "table table-striped table-bordered"
suite_div.insert(10, table)

thead = soup.new_tag('thead')
table.insert(0, thead)

tr = soup.new_tag('tr')
thead.insert(0, tr)

th = soup.new_tag('th')
th.string = "Suite Name"
tr.insert(0, th)

th = soup.new_tag('th')
th.string = "Status"
tr.insert(1, th)

th = soup.new_tag('th')
th.string = "Total"
tr.insert(2, th)

th = soup.new_tag('th')
th.string = "Pass"
tr.insert(3, th)

th = soup.new_tag('th')
th.string = "Fail"
tr.insert(4, th)

th = soup.new_tag('th')
th.string = "Time (s)"
tr.insert(5, th)

tbody = soup.new_tag('tbody')
table.insert(11, tbody)

### =============== GET SUITE METRICS =============== ###

class SuiteResults(ResultVisitor):

    def start_suite(self, suite):

        suite_test_list = suite.tests
        if not suite_test_list:
            pass
        else:
            stats = suite.statistics
            table_tr = soup.new_tag('tr')
            tbody.insert(0, table_tr)

            table_td = soup.new_tag('td',style="word-wrap: break-word;max-width: 250px; white-space: normal;cursor: pointer; text-decoration: underline; color:blue")
            table_td.string = str(suite)
            table_td['onclick']="openInNewTab('%s%s%s','%s%s')"%(log_name,'#',suite.id,'#',suite.id)
            table_td['data-toggle']="tooltip"
            table_td['title']="Click to view '%s' logs"% suite
            table_tr.insert(0, table_td)

            table_td = soup.new_tag('td')
            table_td.string = str(suite.status)
            table_tr.insert(1, table_td)

            table_td = soup.new_tag('td')
            table_td.string = str(stats.all.total)
            table_tr.insert(2, table_td)

            table_td = soup.new_tag('td')
            table_td.string = str(stats.all.passed)
            table_tr.insert(3, table_td)

            table_td = soup.new_tag('td')
            table_td.string = str(stats.all.failed)
            table_tr.insert(4, table_td)

            table_td = soup.new_tag('td')
            table_td.string = str(suite.elapsedtime/float(1000))
            table_tr.insert(5, table_td)

result.visit(SuiteResults())
test_icon_txt="""
<div class="row">
<div class="col-md-12" style="height:25px;width:auto;">
</div>
</div>
"""
suite_div.append(BeautifulSoup(test_icon_txt, 'html.parser'))
### ============================ END OF SUITE METRICS ============================================ ####
print("3 of 6: Capturing test metrics...")
### ============================ START OF TEST METRICS ======================================= ####
# Tests div
tm_div = soup.new_tag('div')
tm_div["id"] = "testMetrics"
tm_div["class"] = "tabcontent"
page_content_div.insert(100, tm_div)

test_icon_txt="""
<h4><b><i class="fa fa-table"></i> Test Metrics</b></h4>
<hr></hr>
"""
tm_div.append(BeautifulSoup(test_icon_txt, 'html.parser'))

# Create table tag
table = soup.new_tag('table')
table["id"] = "tm"
table["class"] = "table table-striped table-bordered"
tm_div.insert(10, table)

thead = soup.new_tag('thead')
table.insert(0, thead)

tr = soup.new_tag('tr')
thead.insert(0, tr)

th = soup.new_tag('th')
th.string = "Suite Name"
tr.insert(0, th)

th = soup.new_tag('th')
th.string = "Test Case"
tr.insert(1, th)

th = soup.new_tag('th')
th.string = "Status"
tr.insert(2, th)

th = soup.new_tag('th')
th.string = "Time (s)"
tr.insert(3, th)

tbody = soup.new_tag('tbody')
table.insert(11, tbody)

### =============== GET TEST METRICS =============== ###

class TestCaseResults(ResultVisitor):

    def visit_test(self, test):

        table_tr = soup.new_tag('tr')
        tbody.insert(0, table_tr)

        table_td = soup.new_tag('td',style="word-wrap: break-word;max-width: 200px; white-space: normal")
        table_td.string = str(test.parent)
        table_tr.insert(0, table_td)

        table_td = soup.new_tag('td',style="word-wrap: break-word;max-width: 250px; white-space: normal;cursor: pointer; text-decoration: underline; color:blue")
        table_td.string = str(test)
        table_td['onclick']="openInNewTab('%s%s%s','%s%s')"%(log_name,'#',test.id,'#',test.id)
        table_td['data-toggle']="tooltip"
        table_td['title']="Click to view '%s' logs"% test
        table_tr.insert(1, table_td)

        table_td = soup.new_tag('td')
        table_td.string = str(test.status)
        table_tr.insert(2, table_td)

        table_td = soup.new_tag('td')
        table_td.string = str(test.elapsedtime/float(1000))
        table_tr.insert(3, table_td)

result.visit(TestCaseResults())

test_icon_txt="""
<div class="row">
<div class="col-md-12" style="height:25px;width:auto;">
</div>
</div>
"""
tm_div.append(BeautifulSoup(test_icon_txt, 'html.parser'))
### ============================ END OF TEST METRICS ============================================ ####
print("4 of 6: Capturing keyword metrics...")
### ============================ START OF KEYWORD METRICS ======================================= ####

# Keywords div
km_div = soup.new_tag('div')
km_div["id"] = "keywordMetrics"
km_div["class"] = "tabcontent"
page_content_div.insert(150, km_div)

keyword_icon_txt="""
<h4><b><i class="fa fa-table"></i> Keyword Metrics</b></h4>
  <hr></hr>
"""
km_div.append(BeautifulSoup(keyword_icon_txt, 'html.parser'))

# Create table tag
# <table id="myTable">
table = soup.new_tag('table')
table["id"] = "km"
table["class"] = "table table-striped table-bordered"
km_div.insert(10, table)

thead = soup.new_tag('thead')
table.insert(0, thead)

tr = soup.new_tag('tr')
thead.insert(0, tr)

th = soup.new_tag('th')
th.string = "Test Case"
tr.insert(1, th)

th = soup.new_tag('th')
th.string = "Keyword"
tr.insert(1, th)

th = soup.new_tag('th')
th.string = "Status"
tr.insert(2, th)

th = soup.new_tag('th')
th.string = "Time (s)"
tr.insert(3, th)

tbody = soup.new_tag('tbody')
table.insert(1, tbody)

class KeywordResults(ResultVisitor):

    def __init__(self):
        self.test = None

    def start_test(self, test):
        self.test = test

    def end_test(self, test):
        self.test = None

    def start_keyword(self,kw):
        # Get test case name (Credits: Robotframework author - Pekke)
        test_name = self.test.name if self.test is not None else ''

         # Ignore library keywords
        keyword_library = kw.libname

        if any (library in keyword_library for library in ignore_library):
            pass
        else:
            keyword_type = kw.type            
            if any (library in keyword_type for library in ignore_type):
                pass
            else:
                table_tr = soup.new_tag('tr')
                tbody.insert(1, table_tr)

                table_td = soup.new_tag('td',style="word-wrap: break-word;max-width: 250px; white-space: normal")
                
                if keyword_type != "kw":
                    table_td.string = str(kw.parent)
                else:
                    table_td.string = str(test_name)
                table_tr.insert(0, table_td)

                table_td = soup.new_tag('td',style="word-wrap: break-word;max-width: 250px; white-space: normal")
                table_td.string = str(kw.kwname)
                table_tr.insert(1, table_td)

                table_td = soup.new_tag('td')
                table_td.string = str(kw.status)
                table_tr.insert(2, table_td)

                table_td = soup.new_tag('td')
                table_td.string =str(kw.elapsedtime/float(1000))
                table_tr.insert(3, table_td)

result.visit(KeywordResults())
test_icon_txt="""
<div class="row">
<div class="col-md-12" style="height:25px;width:auto;">
</div>
</div>
"""
km_div.append(BeautifulSoup(test_icon_txt, 'html.parser'))
### ============================ END OF KEYWORD METRICS ======================================= ####

### ============================ START OF LOGS ====================================== ###

# Logs div
log_div = soup.new_tag('div')
log_div["id"] = "log"
log_div["class"] = "tabcontent"
page_content_div.insert(200, log_div)

test_icon_txt="""
    <p style="text-align:right">** <b>Report.html</b> and <b>Log.html</b> need to be in current folder in order to display here</p>
  <div class="embed-responsive embed-responsive-4by3">
    <iframe class="embed-responsive-item" src=%s></iframe>
  </div>
"""%(log_name)
log_div.append(BeautifulSoup(test_icon_txt, 'html.parser'))

### ============================ END OF LOGS ======================================= ####

### ============================ EMAIL STATISTICS ================================== ###
# Statistics div
statisitcs_div = soup.new_tag('div')
statisitcs_div["id"] = "statistics"
statisitcs_div["class"] = "tabcontent"
page_content_div.insert(300, statisitcs_div)

emailStatistics="""
<h4><b><i class="fa fa-envelope-o"></i> Email Statistics</b></h4>
<hr></hr>
<button id="create" class="btn btn-primary active inner" role="button" onclick="updateTextArea();this.style.visibility= 'hidden';"><i class="fa fa-cogs"></i> Generate Statistics Email</button>
<a download="message.eml" class="btn btn-primary active inner" role="button" id="downloadlink" style="display: none; width: 300px;"><i class="fa fa-download"></i> Click Here To Download Email</a>
<script>
function updateTextArea() {
    var suite = "<b>Top 10 Suite Performance:</b><br><br>" + $("#suiteBarID table")[0].outerHTML;
    var test = "<b>Top 10 Test Performance:</b><br><br>" + $("#testsBarID table")[0].outerHTML;
    var keyword ="<b>Top 10 Keyword Performance:</b><br><br>" + $("#keywordsBarID table")[0].outerHTML;
    var saluation="<pre><br>Please refer RF Metrics Report for detailed statistics.<br><br>Regards,<br>QA Team</pre></body></html>";
    document.getElementById("textbox").value += "<br>" + suite + "<br>" + test + "<br>" + keyword + saluation;
    $("#create").click(function(){
    $(this).remove();
    });
}
</script>

<textarea id="textbox" class="col-md-12" style="height: 400px; padding:1em;">
To: myemail1234@email.com
Subject: Automation Execution Status
X-Unsent: 1
Content-Type: text/html


<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>Test Email Sample</title>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<meta http-equiv="X-UA-Compatible" content="IE=edge" />
<meta name="viewport" content="width=device-width, initial-scale=1.0 " />
      <style>
         body {
			 background-color:#F2F2F2; 
         }
         body, html, table,pre,b {
			 font-family: Calibri, Arial, sans-serif;
			 font-size: 1em; 
         }
         .pastdue { color: crimson; }
         table {
			 border: 1px solid silver;
			 padding: 6px;
			 margin-left: 30px;
			 width: 600px;
         }
         thead {
			 text-align: center;
			 font-size: 1.1em;        
			 background-color: #B0C4DE;
			 font-weight: bold;
			 color: #2D2C2C;
         }
         tbody {
			text-align: center;
         }
         th {
            width: 25%%;
            word-wrap:break-word;
         }
      </style>
   </head>
   <body><pre>Hi Team,
Following are the last build execution statistics.

<b>Metrics:<b>

</pre>
      <table>
         <thead>
            <th style="width: 25%%;">Statistics</th>
            <th style="width: 25%%;">Total</th>
            <th style="width: 25%%;">Pass</th>
            <th style="width: 25%%;">Fail</th>
         </thead>
         <tbody>
            <tr>
               <td style="text-align: left;font-weight: bold;"> SUITE </td>
               <td style="background-color: #F5DEB3;text-align: center;">%s</td>
               <td style="background-color: #90EE90;text-align: center;">%s</td>
               <td style="background-color: #F08080;text-align: center;">%s</td>
            </tr>
            <tr>
               <td style="text-align: left;font-weight: bold;"> TESTS </td>
               <td style="background-color: #F5DEB3;text-align: center;">%s</td>
               <td style="background-color: #90EE90;text-align: center;">%s</td>
               <td style="background-color: #F08080;text-align: center;">%s</td>
            </tr>
            <tr>
               <td style="text-align: left;font-weight: bold;"> KEYWORDS </td>
               <td style="background-color: #F5DEB3;text-align: center;">%s</td>
               <td style="background-color: #90EE90;text-align: center;">%s</td>
               <td style="background-color: #F08080;text-align: center;">%s</td>
            </tr>
         </tbody>
      </table>


</textarea>

""" % (total_suite,passed_suite,failed_suite,total,passed,failed,total_keywords,passed_keywords,failed_keywords)
statisitcs_div.append(BeautifulSoup(emailStatistics, 'html.parser'))



### ============================ END OF EMAIL STATISTICS ================================== ###



script_text="""

    <script>
        (function () {
        var textFile = null,
          makeTextFile = function (text) {
            var data = new Blob([text], {type: 'text/plain'});
            if (textFile !== null) {
              window.URL.revokeObjectURL(textFile);
            }
            textFile = window.URL.createObjectURL(data);
            return textFile;
          };
        
          var create = document.getElementById('create'),
            textbox = document.getElementById('textbox');
          create.addEventListener('click', function () {
            var link = document.getElementById('downloadlink');
            link.href = makeTextFile(textbox.value);
            link.style.display = 'block';
          }, false);
        })();
    </script>
	<script>
        function createPieChart(passed_count,failed_count,ChartID,ChartName){
        var status = [];
        status.push(['Status', 'Percentage']);
        status.push(['PASS',parseInt(passed_count)],['FAIL',parseInt(failed_count)]);
        var data = google.visualization.arrayToDataTable(status);

        var options = {
        pieHole: 0.6,
        legend: 'none',
        chartArea: {width: "95%",height: "90%"},
        colors: ['green', 'red'],
        };

        var chart = new google.visualization.PieChart(document.getElementById(ChartID));
        chart.draw(data, options);
    }
    </script>
    <script>
       function createBarGraph(tableID,keyword_column,time_column,limit,ChartID,Label,type){
		var status = [];
		css_selector_locator = tableID + ' tbody >tr'
		var rows = $(css_selector_locator);
		var columns;
		var myColors = [
			'#4F81BC',
            '#C0504E',
            '#9BBB58',
            '#24BEAA',
            '#8064A1',
            '#4AACC5',
            '#F79647',
            '#815E86',
            '#76A032',
            '#34558B'
		];
		status.push([type, Label,{ role: 'annotation'}, {role: 'style'}]);
		for (var i = 0; i < rows.length; i++) {
			if (i == Number(limit)){
				break;
			}
			//status = [];
			name_value = $(rows[i]).find('td'); 
		  
			time=($(name_value[Number(time_column)]).html()).trim();
			keyword=($(name_value[Number(keyword_column)]).html()).trim();
			status.push([keyword,parseFloat(time),parseFloat(time),myColors[i]]);
		  }
		  var data = google.visualization.arrayToDataTable(status);

		  var options = {
            legend: 'none',
            chartArea: {width: "92%",height: "75%"},
            bar: {
                groupWidth: '90%'
            },
			annotations: {
				alwaysOutside: true,
                textStyle: {
                fontName: 'Comic Sans MS',
                fontSize: 13,
                bold: true,
                italic: true,
                color: "black",     // The color of the text.
                },
			},
            hAxis: {
                textStyle: {
                    fontName: 'Arial',
                    fontSize: 10,
                }
            },
            vAxis: {
                gridlines: { count: 10 },
                textStyle: {                    
                    fontName: 'Comic Sans MS',
                    fontSize: 10,
                }
            },
		  };  

            // Instantiate and draw the chart.
            var chart = new google.visualization.ColumnChart(document.getElementById(ChartID));
            chart.draw(data, options);
         }

    </script>

 <script>
  function executeDataTable(tabname,sortCol) {
    var fileTitle;
    switch(tabname) {
        case "#sm":
            fileTitle = "SuiteMetrics";
            break;
        case "#tm":
            fileTitle =  "TestMetrics";
            break;
        case "#km":
            fileTitle =  "KeywordMetrics";
            break;
        default:
            fileTitle =  "metrics";
    }

    $(tabname).DataTable(
        {
            retrieve: true,
            "order": [[ Number(sortCol), "desc" ]],
            dom: 'l<".margin" B>frtip',
            buttons: [
                'copy',
                {
                    extend: 'csv',
                    filename: function() {
                        return fileTitle + '-' + new Date().toLocaleString();
                    },
                    title : '',
                },
                {
                    extend: 'excel',
                    filename: function() {
                        return fileTitle + '-' + new Date().toLocaleString();
                    },
                    title : '',
                },
                {
                    extend: 'pdf',
                    filename: function() {
                        return fileTitle + '-' + new Date().toLocaleString();
                    },
                    title : '',
                },
                {
                    extend: 'print',
                    title : '',
                },
            ],
        } 
    );
}
 </script>
 <script>
  function openPage(pageName,elmnt,color) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablink");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].style.backgroundColor = "";
    }
    document.getElementById(pageName).style.display = "block";
    elmnt.style.backgroundColor = color;

}
// Get the element with id="defaultOpen" and click on it
document.getElementById("defaultOpen").click();
 </script>
 <script>
 // Get the element with id="defaultOpen" and click on it
document.getElementById("defaultOpen").click();
 </script>
 <script>
$(window).on('load',function(){$('.loader').fadeOut();});
</script>
"""

body.append(BeautifulSoup(script_text, 'html.parser'))

### ====== WRITE TO RF_METRICS_REPORT.HTML ===== ###

# Write output as html file
with open(result_file, 'w') as outfile:
    outfile.write(soup.prettify())

# Wait for 2 seconds - File is generated
time.sleep(2)

# ====== EMAIL CONTENT ========== #

email_content = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>Robotframework Metrics</title>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<meta http-equiv="X-UA-Compatible" content="IE=edge" />
<meta name="viewport" content="width=device-width, initial-scale=1.0 " />
      <style>
         body {
			 background-color:#F2F2F2; 
         }
         body, html, table,span,b {
			 font-family: Calibri, Arial, sans-serif;
			 font-size: 1em; 
         }
         .pastdue { color: crimson; }
         table {
			 border: 1px solid silver;
			 padding: 6px;
			 margin-left: 30px;
			 width: 600px;
         }
         thead {
			 text-align: center;
			 font-size: 1.1em;        
			 background-color: #B0C4DE;
			 font-weight: bold;
			 color: #2D2C2C;
         }
         tbody {
			text-align: center;
         }
         th {
            word-wrap:break-word;
         }
		 td {
            height: 25px;
         }
        .dt-buttons {
            margin-left: 30px;
        }
      </style>
   </head>
   <body>
   <span>Hi Team,<br>Following are the last build execution status.<br><br><b>Metrics:<b><br><br></span>
      <table>
         <thead>
            <th style="width: 25vh;"> Stats </th>
            <th style="width: 20vh;"> Total </th>
            <th style="width: 20vh;"> Pass </th>
            <th style="width: 20vh;"> Fail </th>
			      <th style="width: 15vh;"> Perc (%%)</th>
         </thead>
         <tbody>
            <tr>
               <td style="text-align: left;font-weight: bold;"> SUITE </td>
               <td style="text-align: center;">%s</td>
               <td style="text-align: center;">%s</td>
               <td style="text-align: center;">%s</td>
			         <td style="text-align: center;">%s</td>
            </tr>
            <tr>
               <td style="text-align: left;font-weight: bold;"> TESTS </td>
               <td style="text-align: center;">%s</td>
               <td style="text-align: center;">%s</td>
               <td style="text-align: center;">%s</td>
			         <td style="text-align: center;">%s</td>
            </tr>
            <tr>
               <td style="text-align: left;font-weight: bold;"> KEYWORDS </td>
               <td style="text-align: center;">%s</td>
               <td style="text-align: center;">%s</td>
               <td style="text-align: center;">%s</td>
			         <td style="text-align: center;">%s</td>
            </tr>
         </tbody>
      </table>

<span><br><b>Info:<b><br><br></span>
 <table>
         <tbody>
            <tr>
               <td style="text-align: left;font-weight: normal;width: 30vh;"> Execution Time </td>
               <td style="text-align: center;font-weight: normal;">%s h</td>
            </tr>
            <tr>
               <td style="text-align: left;font-weight: normal;width: 50vh;"> Generated By </td>
               <td style="text-align: center;font-weight: normal;">%s</td>
            </tr>
         </tbody>
      </table>

<span style="text-align: left;font-weight: normal;"><br>Please refer robotframework-metrics report for detailed info.<br><br>Regards,<br>QA Team</span>

</body></html> 
"""%(total_suite,passed_suite,failed_suite,suitepp,total,passed,failed,testpp,total_keywords,passed_keywords,failed_keywords,kwpp,elapsedtime,generator)

#msg.set_payload(email_content)
msg.attach(MIMEText(email_content, 'html'))

# Attach robotframework file
rfmetrics = MIMEBase('application', "octet-stream")
rfmetrics.set_payload(open(result_file, "rb").read())
encoders.encode_base64(rfmetrics)
attachmentName = 'attachment; filename=%s'%(result_file_name)
rfmetrics.add_header('Content-Disposition',attachmentName)
msg.attach(rfmetrics)

if send_email in ['true', '1', 't', 'y', 'yes']:
    # Start server
    server.starttls()
    print("5 of 6: Sending email with robotmetrics.html...")
    # Login Credentials for sending the mail
    server.login(msg['From'], password)
    
    server.sendmail(sender, recipients, msg.as_string())
    print("6 of 6: Email sent successfully!")
else:
    print("6 of 6: Skipping step 5 (send email) !")

print("robotframework-metrics.html is created successfully")
# ==== END OF EMAIL CONTENT ====== #