from bs4 import BeautifulSoup
import datetime
import sys
import os

# Ignores following library keywords in metrics report
ignore_library = [
    'BuiltIn',
    'SeleniumLibrary',
    'String',
    'Collections',
    'DateTime',
    ]

head_content = """

<!DOCTYPE html>
<html>
<head>
	<meta name="viewport" content="width=device-width, initial-scale=1">
		<title>Robot Framework Metrics Report</title>
		<meta charset="utf-8"/>
		<link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet" type="text/css"/>
		<link href="https://cdn.datatables.net/1.10.19/css/dataTables.bootstrap.min.css" rel="stylesheet" type="text/css"/>
		<script src="https://code.jquery.com/jquery-3.3.1.js" type="text/javascript"></script>
		<script src="https://cdn.datatables.net/1.10.19/js/jquery.dataTables.min.js" type="text/javascript"></script>
		<script src="https://cdn.datatables.net/1.10.19/js/dataTables.bootstrap.min.js" type="text/javascript"></script>
		<style>
* {box-sizing: border-box}

/* Set height of body and the document to 100% */
body, html {
    height: 100%;
    margin: 0;
    font-family:  Comic Sans MS;
}

/* Style tab links */
.tablink {
    background-color: #555;
    color: white;
    float: left;
    border: none;
    outline: none;
    cursor: pointer;
    padding: 14px 16px;
    font-size: 14px;
    width: 33.3%;
}

.tablink:hover {
    background-color: #777;
}

/* Style the tab content (and add height:100% for full page content) */
.tabcontent {
    color: black;
    display: none;
    padding: 20px;
    height: 100%;
}

#dashboard {background-color: white;}
#testMetrics {background-color: white;}
#keywordMetrics {background-color: white;}

</style>
</head>
</html>
"""

soup = BeautifulSoup(head_content,"html.parser")

# datatable script js
script_text = """ $(document).ready(function() {
    $('#example').DataTable();
} );"""
script = soup.new_tag('script')
script.attrs["type"] = "text/javascript"
script.string = script_text
soup.head.append(script)

body = soup.new_tag('body',style="padding: 5px")
soup.insert(0, body)

# Create header tag and title
h1 = soup.new_tag('h1',style="font-size: 2em;")
h1.string = "Robot Framework Metrics Report"
body.insert(0, h1)

br = soup.new_tag('br')
body.insert(1, br)

# Get report result - OS independent
current_path = os.getcwd()
# output.xml file location
text_file = os.path.join(os.path.curdir, 'output.xml')
# performance report result file location
result_file = os.path.join(os.path.curdir, 'rf_metrics_result.html')

# Buttons
button = soup.new_tag('button')
button["class"] = "tablink"
button["onclick"] = "openPage('dashboard', this, 'orange');executeDataTable('#db')"
button["id"] = "defaultOpen"
button.string = "Dashboard"
body.insert(2, button)

button = soup.new_tag('button')
button["class"] = "tablink"
button["onclick"] = "openPage('testMetrics', this, 'orange');executeDataTable('#tm')"
button.string = "Test Metrics"
body.insert(3, button)

button = soup.new_tag('button')
button["class"] = "tablink"
button["onclick"] = "openPage('keywordMetrics', this, 'orange');executeDataTable('#km')"
button.string = "Keyword Metrics"
body.insert(4, button)

# Dashboard div
db_div = soup.new_tag('div')
db_div["id"] = "dashboard"
db_div["class"] = "tabcontent"
body.insert(5, db_div)

# Tests div
tm_div = soup.new_tag('div')
tm_div["id"] = "testMetrics"
tm_div["class"] = "tabcontent"
body.insert(6, tm_div)

# Keywords div
km_div = soup.new_tag('div')
km_div["id"] = "keywordMetrics"
km_div["class"] = "tabcontent"
body.insert(5, km_div)

### ====== READ OUTPUT.XML ===== ###

with open('output.xml') as raw_resuls:
    results = BeautifulSoup(raw_resuls, 'lxml')

### ============================ START OF DASHBOARD ======================================= ####

br = soup.new_tag('br')
db_div.insert(0, br)
br = soup.new_tag('br')
db_div.insert(1, br)

h3 = soup.new_tag('h3',style="align: center")
h3.string= "<<<< Comming Soon >>>>"
db_div.insert(2, h3)


### ============================ END OF DASHBOARD ============================================ ####


### ============================ START OF TEST METRICS ======================================= ####

br = soup.new_tag('br')
tm_div.insert(0, br)
br = soup.new_tag('br')
tm_div.insert(1, br)

# Create table tag
table = soup.new_tag('table',style="padding: 5px;font-size: 13px;")
table["id"] = "tm"
table["class"] = "table table-striped table-bordered"
tm_div.insert(2, table)

thead = soup.new_tag('thead')
table.insert(0, thead)

tr = soup.new_tag('tr')
thead.insert(0, tr)

th = soup.new_tag('th')
th.string = "Test Case"
tr.insert(0, th)

th = soup.new_tag('th')
th.string = "Status"
tr.insert(1, th)

th = soup.new_tag('th')
th.string = "Start Time"
tr.insert(2, th)

th = soup.new_tag('th')
th.string = "End time"
tr.insert(3, th)

th = soup.new_tag('th')
th.string = "Elapsed Time"
tr.insert(4, th)

tbody = soup.new_tag('tbody')
table.insert(1, tbody)

### =============== GET TEST METRICS =============== ###

# List for test cases
for tests in results.find_all("test"):    

    table_tr = soup.new_tag('tr')
    tbody.insert(0, table_tr)

    table_td = soup.new_tag('td')
    table_td.string = tests['name']
    table_tr.insert(0, table_td)

    for status in tests.find_all("status"):
        # Get duration took by keyword
        start_time = datetime.datetime.strptime(status['starttime'], "%Y%m%d %H:%M:%S.%f")
        end_time = datetime.datetime.strptime(status['endtime'], "%Y%m%d %H:%M:%S.%f")
        test_status = status['status']

    table_td = soup.new_tag('td')
    table_td.string = str(test_status)
    table_tr.insert(1, table_td)

    table_td = soup.new_tag('td')
    table_td.string = str(start_time)
    table_tr.insert(2, table_td)

    table_td = soup.new_tag('td')
    table_td.string = str(end_time)
    table_tr.insert(3, table_td)

    duration = end_time - start_time

    table_td = soup.new_tag('td')
    table_td.string = str(duration)
    table_tr.insert(4, table_td)


### ============================ END OF TEST METRICS ============================================ ####

### ============================ START OF KEYWORD METRICS ======================================= ####

br = soup.new_tag('br')
km_div.insert(0, br)
br = soup.new_tag('br')
km_div.insert(1, br)

# Create table tag
# <table id="myTable">
table = soup.new_tag('table',style="padding: 5px;font-size: 13px;")
table["id"] = "km"
table["class"] = "table table-striped table-bordered"
km_div.insert(2, table)

thead = soup.new_tag('thead')
table.insert(0, thead)

tr = soup.new_tag('tr')
thead.insert(0, tr)

th = soup.new_tag('th')
th.string = "Test Case"
tr.insert(0, th)

th = soup.new_tag('th')
th.string = "Keyword"
tr.insert(1, th)

th = soup.new_tag('th')
th.string = "Status"
tr.insert(2, th)

th = soup.new_tag('th')
th.string = "Start Time"
tr.insert(3, th)

th = soup.new_tag('th')
th.string = "End time"
tr.insert(4, th)

th = soup.new_tag('th')
th.string = "Elapsed Time"
tr.insert(5, th)

tbody = soup.new_tag('tbody')
table.insert(1, tbody)

# List for test cases
for tests in results.find_all("test"):    

    # List for keywords
    for keywords in tests.find_all("kw"):

        try:
            keyword_type = keywords['type']
            if  str(keyword_type) == "for" or str(keyword_type) == "foritem":
                continue

        except Exception :

            try:
                # Ignore library keywords
                keyword_library = keywords['library']

                if any (library in keyword_library for library in ignore_library):
                    continue

                else:
                    # Keywords which are not ignored
                    valid_keyword = True

            except Exception :
                # In output.xml library attribute will not be included for Local keywords
                local_keyword = True

            if valid_keyword or local_keyword:

                table_tr = soup.new_tag('tr')
                tbody.insert(1, table_tr)

                table_td = soup.new_tag('td')
                table_td.string = tests['name']
                table_tr.insert(0, table_td)

                table_td = soup.new_tag('td')
                table_td.string = keywords['name']
                table_tr.insert(1, table_td)

                for status in keywords.find_all("status"):
                    # Get duration took by keyword
                    start_time = datetime.datetime.strptime(status['starttime'], "%Y%m%d %H:%M:%S.%f")
                    end_time = datetime.datetime.strptime(status['endtime'], "%Y%m%d %H:%M:%S.%f")
                    test_status = status['status']

                table_td = soup.new_tag('td')
                table_td.string = test_status
                table_tr.insert(2, table_td)

                table_td = soup.new_tag('td')
                table_td.string = str(start_time)
                table_tr.insert(3, table_td)

                table_td = soup.new_tag('td')
                table_td.string = str(end_time)
                table_tr.insert(4, table_td)

                duration = end_time - start_time

                table_td = soup.new_tag('td')
                table_td.string = str(duration)
                table_tr.insert(5, table_td)

### ============================ END OF KEYWORD METRICS ======================================= ####

### data table script ###
data_table_script = """
function executeDataTable(tabname) {
   $(document).ready(function() {
    $(tabname).DataTable();
} );}
"""
# Create script tag - badges
script = soup.new_tag('script')
script.string=data_table_script
body.insert(7,script)

### tab script ###
tab_script = """
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
"""
# Create script tag - badges
script = soup.new_tag('script')
script.string=tab_script
body.insert(8,script)


### ====== WRITE TO RF_METRICS_REPORT.HTML ===== ###

# Write output as html file
with open(result_file, 'w') as outfile:
    outfile.write(soup.prettify())