from bs4 import BeautifulSoup
import datetime
import time
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

# Get report result - OS independent
current_path = os.getcwd()
# output.xml file location
text_file = os.path.join(os.path.curdir, 'output.xml')
# performance report result file location
result_file = os.path.join(os.path.curdir, 'rf_metrics_result.html')

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
        <script src="https://canvasjs.com/assets/script/canvasjs.min.js"></script>
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
    padding: 15px;
    height: 100%;
}

#container {
  text-align: center;
  max-width: 48%;
  //height: 100%
  margin: 0 auto;
}
.block {
  width: 48%;
  height: 350px;
  margin: 10px;
  display: inline-block;
  background: #f1f1f1;
}

#dashboard {background-color: white;}
#testMetrics {background-color: white;}
#keywordMetrics {background-color: white;}


</style>
</head>
</html>
"""

soup = BeautifulSoup(head_content,"html.parser")

body = soup.new_tag('body',style="padding: 5px")
soup.insert(0, body)

# Create header tag and title
h1 = soup.new_tag('h1',style="font-size: 2em;")
h1.string = "Robot Framework Metrics Report"
body.insert(0, h1)

br = soup.new_tag('br')
body.insert(1, br)

# Buttons
button = soup.new_tag('button')
button["class"] = "tablink"
button["onclick"] = "openPage('dashboard', this, 'orange');"
button["id"] = "defaultOpen"
button.string = "Dashboard"
body.insert(2, button)

button = soup.new_tag('button')
button["class"] = "tablink"
button["onclick"] = "openPage('testMetrics', this, 'orange');executeDataTable('#tm',4)"
button.string = "Test Metrics"
body.insert(3, button)

button = soup.new_tag('button')
button["class"] = "tablink"
button["onclick"] = "openPage('keywordMetrics', this, 'orange');executeDataTable('#km',5)"
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

container_div = soup.new_tag('div')
container_div["id"]="containers"
db_div.insert(1, container_div)

div_block_1 = soup.new_tag('div')
div_block_1["class"]="block"
container_div.insert(0, div_block_1)

div_block_2 = soup.new_tag('div')
div_block_2["class"]="block"
container_div.insert(1, div_block_2)

div_block_3 = soup.new_tag('div')
div_block_3["class"]="block"
container_div.insert(2, div_block_3)

div_block_4 = soup.new_tag('div')
div_block_4["class"]="block"
container_div.insert(3, div_block_4)

div = soup.new_tag('div',style="height: 350px; width: 100%;")
div["id"] = "testChartID"
div_block_1.insert(1, div)

div = soup.new_tag('div',style="height: 350px; width: 100%;")
div["id"] = "testsBarID"
div_block_2.insert(1, div)

div = soup.new_tag('div',style="height: 350px; width: 100%;")
div["id"] = "keywordChartID"
div_block_3.insert(1, div)

div = soup.new_tag('div',style="height: 350px; width: 100%;")
div["id"] = "keywordsBarID"
div_block_4.insert(1, div)

# Show graphs on load
show_graphs_on_load = """
window.onload = function(){
    executeDataTable('#tm',4);
    executeDataTable('#km',5);
    createPieChart('#tm',1,'testChartID','Tests Status:');		
    createBarGraph('#tm',0,4,10,'testsBarID','Top 10 Tests Performance:');
    createPieChart('#km',2,'keywordChartID','Keywords Status:');		
    createBarGraph('#km',1,5,10,'keywordsBarID','Top 10 Keywords Performance:')
	};
"""

script = soup.new_tag('script')
script.string = show_graphs_on_load
container_div.insert(5, script)


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

    table_td = soup.new_tag('td',style="word-wrap: break-word;max-width: 200px; white-space: normal")
    table_td.string = tests['name']
    table_tr.insert(0, table_td)

    for status in tests.find_all("status"):
        # Get duration took by keyword
        start_time = datetime.datetime.strptime(status['starttime'], "%Y%m%d %H:%M:%S.%f")        
        end_time = datetime.datetime.strptime(status['endtime'], "%Y%m%d %H:%M:%S.%f")
        test_status = status['status']

    dispay_start_time = start_time.strftime('%Y%m%d %H:%M:%S.%f')[:-3]
    display_end_time = end_time.strftime('%Y%m%d %H:%M:%S.%f')[:-3]

    table_td = soup.new_tag('td')
    table_td.string = str(test_status)
    table_tr.insert(1, table_td)

    table_td = soup.new_tag('td')
    table_td.string = str(dispay_start_time)
    table_tr.insert(2, table_td)

    table_td = soup.new_tag('td')
    table_td.string = str(display_end_time)
    table_tr.insert(3, table_td)

    total_time= end_time - start_time                
    try:
        total_time = datetime.datetime.strptime(str(total_time),'%H:%M:%S.%f')
        total_time = total_time.strftime('%H:%M:%S.%f')[:-3]
    except ValueError:
        total_time = datetime.datetime.strptime(str(total_time),'%H:%M:%S')
        total_time = total_time.strftime('%H:%M:%S')
        #total_time = total_time+".000"

    table_td = soup.new_tag('td')
    table_td.string = str(total_time)
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

                table_td = soup.new_tag('td',style="word-wrap: break-word;max-width: 200px; white-space: normal")
                table_td.string = tests['name']
                table_tr.insert(0, table_td)

                table_td = soup.new_tag('td',style="word-wrap: break-word;max-width: 200px; white-space: normal")
                table_td.string = keywords['name']
                table_tr.insert(1, table_td)

                for status in keywords.find_all("status"):
                    # Get duration took by keyword
                    start_time = datetime.datetime.strptime(status['starttime'], "%Y%m%d %H:%M:%S.%f")
                    end_time = datetime.datetime.strptime(status['endtime'], "%Y%m%d %H:%M:%S.%f")
                    test_status = status['status']

                dispay_start_time = start_time.strftime('%Y%m%d %H:%M:%S.%f')[:-3]
                display_end_time = end_time.strftime('%Y%m%d %H:%M:%S.%f')[:-3]

                table_td = soup.new_tag('td')
                table_td.string = test_status
                table_tr.insert(2, table_td)

                table_td = soup.new_tag('td')
                table_td.string = str(dispay_start_time)
                table_tr.insert(3, table_td)

                table_td = soup.new_tag('td')
                table_td.string = str(display_end_time)
                table_tr.insert(4, table_td)

                total_time= end_time - start_time

                try:
                    total_time = datetime.datetime.strptime(str(total_time),'%H:%M:%S.%f')
                    total_time = total_time.strftime('%H:%M:%S.%f')[:-3]
                except ValueError:
                    total_time = datetime.datetime.strptime(str(total_time),'%H:%M:%S')
                    total_time = total_time.strftime('%H:%M:%S')
                    #total_time= total_time+".000"
                
                table_td = soup.new_tag('td')
                table_td.string = str(total_time)
                table_tr.insert(5, table_td)

### ============================ END OF KEYWORD METRICS ======================================= ####

canvas_pie_script = """
function createPieChart(tableID,status_column,ChartID,ChartName){

var chart = new CanvasJS.Chart(ChartID,{  
    exportFileName: ChartName,
	exportEnabled: true,	
    animationEnabled: true,
	title: {
    text: ChartName,
    fontFamily: "Comic Sans MS",
    fontSize: 15,
	horizontalAlign: "left",
    fontWeight: "bold"
    
  },
  data: []
  
});

var rows = $(tableID).dataTable().fnGetNodes();
var columns;
var isPass = 0;
var isFail = 0;

for (var i = 0; i < rows.length; i++) {
  columns = $(rows[i]).find('td');  
  
    if (columns[Number(status_column)].innerHTML.trim() == "PASS") {
      isPass = isPass + 1;      
    } else {
      isFail = isFail + 1;      
    }
  }  
var status = [{label:'PASS',y:parseInt(isPass),color:"Green"},{label:'FAIL',y:parseInt(isFail),color:"Red"}];
  chart.options.data.push({
    //type: "pie",
    type: "doughnut",
    startAngle: 60,
    //innerRadius: 60,
    indexLabelFontSize: 15,
    indexLabel: "{label} - #percent%",
    toolTipContent: "<b>{label}:</b> {y} (#percent%)",

    //name: ($(columns[0]).html()), 
    //showInLegend: true,
    //legendText: ($(columns[0]).html()),
    dataPoints: status
  });
  chart.render();
}
"""
script = soup.new_tag('script')
script.string=canvas_pie_script
body.insert(7,script)

bar_graph_script = """
function createBarGraph(tableID,keyword_column,time_column,limit,ChartID,ChartName){
      var chart = new CanvasJS.Chart(ChartID, {
       exportFileName: ChartName,
        exportEnabled: true,	
        animationEnabled: true,
    title: {
        text: ChartName,
        fontFamily: "Comic Sans MS",
        fontSize: 15,
        textAlign: "centre",
        dockInsidePlotArea: true,
        fontWeight: "bold"
    },
      axisX:{
        //title:"Axis X title",
        labelAngle: 0,
        labelFontSize: 10,
        labelFontFamily:"Comic Sans MS",
        
      },
      axisY:{
        title:"Seconds (s)",
      },
      data: []
    });

var status = [];
css_selector_locator = tableID + ' tbody >tr'
var rows = $(css_selector_locator);
var columns;

for (var i = 0; i < rows.length; i++) {
    if (i == Number(limit)){
        break;
    }
	//status = [];
  name_value = $(rows[i]).find('td'); 
  
  time=($(name_value[Number(time_column)]).html()).trim();
    try {
	    mfree=time.split(".")    
        if (mfree.length > 1){
            tt=mfree[0].split(":");
            sec=tt[0]*3600+tt[1]*60+tt[2]*1+(mfree[1]/1000)*1;
        } else {
            tt=mfree[0].split(":");
            sec=tt[0]*3600+tt[1]*60+tt[2]*1;
        }
	    
    }
        catch (e) {
	    tt=time.split(":");
	    sec=tt[0]*3600+tt[1]*60+tt[2]*1;
    }
	
	status.push({label:$(name_value[Number(keyword_column)]).html(),y:sec});
  }  
	chart.options.data.push({
    type: "column",
    //name: ($(rows[0]).find('th')), 
    //showInLegend: true,
    //legendText: ($(rows[0]).find('th')),
	//yValueFormatString: "HH-mm-ss.fff",
    indexLabel: "{y} s",
    toolTipContent: "<b>{label}:</b> {y} s",
    dataPoints: status
  });
  
    chart.render();
	}
  </script>
"""

script = soup.new_tag('script')
script.string=bar_graph_script
body.insert(8,script)

### data table script ###
data_table_script = """
function executeDataTable(tabname,sortCol) {
    $(tabname).DataTable(
        {
        retrieve: true,
        "order": [[ Number(sortCol), "desc" ]]
        } 
    );
}
"""
# Create script tag - badges
script = soup.new_tag('script')
script.string=data_table_script
body.insert(9,script)

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
body.insert(10,script)


### ====== WRITE TO RF_METRICS_REPORT.HTML ===== ###

# Write output as html file
with open(result_file, 'w') as outfile:
    outfile.write(soup.prettify())