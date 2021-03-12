import os
import math
import smtplib
import time
import logging
from bs4 import BeautifulSoup
from datetime import datetime
from datetime import timedelta
from robot.api import ExecutionResult
from .test_stats import TestStats
from .keyword_stats import KeywordStats
from .suite_results import SuiteResults
from .test_results import TestResults
from .keyword_results import KeywordResults

try:
    from gevent.pool import Group

    FAILED_IMPORT = False

except ImportError:
    FAILED_IMPORT = True

IGNORE_TYPES = ['foritem', 'for']


def generate_report(opts):
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
    group = Group() if not FAILED_IMPORT else ''

    # START OF CUSTOMIZE REPORT
    # URL or filepath of your company logo
    logo = opts.logo

    # Ignores following type keywords in metrics report
    ignore_type = IGNORE_TYPES
    if opts.ignoretype:
        ignore_type.extend(opts.ignoretype)

    # END OF CUSTOMIZE REPORT
    # Report to support file location as arguments
    # Source Code Contributed By : Ruud Prijs
    # input directory
    path = os.path.abspath(os.path.expanduser(opts.path))

    # output.xml files
    output_names = []
    # support "*.xml" of output files
    if ( opts.output == "*.xml" ):
        for item in os.listdir(path): 
            if os.path.isfile(item) and item.endswith('.xml'):
                output_names.append(item)
    else:
        for curr_name in opts.output.split(","):
            curr_path = os.path.join(path, curr_name)
            output_names.append(curr_path)
    
    # log.html file
    log_name = opts.log_name

    # copy the list of output_names onto the one of required_files; the latter may (in the future) 
    # contain files that should not be processed as output_names
    required_files = list(output_names)
    missing_files = [filename for filename in required_files if not os.path.exists(filename)]
    if missing_files:
        # We have files missing.
        exit("output.xml file is missing: {}".format(", ".join(missing_files)))

    mt_time = datetime.now().strftime('%Y%m%d-%H%M%S')

    # Output result file location
    if opts.metrics_report_name:
        result_file_name = opts.metrics_report_name
    else:
        result_file_name = 'metrics-' + mt_time + '.html'
    result_file = os.path.join(path, result_file_name)

    # Read output.xml file
    result = ExecutionResult(*output_names)
    result.configure(stat_config={'suite_stat_level': 2,
                                  'tag_stat_combine': 'tagANDanother'})

    logging.info("Converting .xml to .html file. This may take few minutes...")

    head_content = """
    <!DOCTYPE doctype html>
    <html lang="en">

    <head>
        <link href="https://png.icons8.com/windows/50/000000/bot.png" rel="shortcut icon" type="image/x-icon" />
        <title>RF Metrics</title>
        <meta charset="utf-8" />
        <meta content="width=device-width, initial-scale=1" name="viewport" />
        <link href="https://cdn.datatables.net/1.10.19/css/jquery.dataTables.min.css" rel="stylesheet" />
        <link href="https://cdn.datatables.net/buttons/1.5.2/css/buttons.dataTables.min.css" rel="stylesheet" />
        <link href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.1.3/css/bootstrap.min.css" rel="stylesheet" />
        <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet" />
        <script src="https://code.jquery.com/jquery-3.3.1.js" type="text/javascript"/>
        <!-- Bootstrap core Googleccharts -->
        <script src="https://www.gstatic.com/charts/loader.js" type="text/javascript"/>
        <script type="text/javascript">
            google.charts.load('current', {
                packages: ['corechart']
            });
        </script>
        <!-- Bootstrap core Datatable-->
        <script src="https://cdn.datatables.net/1.10.19/js/jquery.dataTables.min.js" type="text/javascript"></script>
        <script src="https://cdn.datatables.net/buttons/1.5.2/js/dataTables.buttons.min.js" type="text/javascript"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/jszip/3.1.3/jszip.min.js" type="text/javascript"></script>
        <script src="https://cdn.datatables.net/buttons/1.5.2/js/buttons.html5.min.js" type="text/javascript"></script>
        <script src="https://cdn.datatables.net/buttons/1.5.2/js/buttons.print.min.js" type="text/javascript"></script>
        <script src="https://cdn.datatables.net/buttons/1.6.1/js/buttons.colVis.min.js" type="text/javascript"></script>

        <style>
            body {
                font-family: -apple-system, sans-serif;
                background-color: #eeeeee;
            }

            .sidenav {
                height: 100%;
                width: 220px;
                position: fixed;
                z-index: 1;
                top: 0;
                left: 0;
                background-color: white;
                overflow-x: hidden;
            }

            .sidenav a {
                padding: 12px 10px 8px 12px;
                text-decoration: none;
                font-size: 18px;
                color: Black;
                display: block;
            }

            .main {
                padding-top: 10px;
            }

            @media screen and (max-height: 450px) {
                .sidenav {
                    padding-top: 15px;
                }
                .sidenav a {
                    font-size: 18px;
                }
            }

            .wrimagecard {
                margin-top: 0;
                margin-bottom: 0.6rem;
                border-radius: 10px;
                transition: all 0.3s ease;
                background-color: #f8f9fa;
            }

            .rowcard {
                padding-top: 10px;
                box-shadow: 12px 15px 20px 0px rgba(46, 61, 73, 0.15);
                border-radius: 15px;
                transition: all 0.3s ease;
                background-color: white;
            }

            .tablecard {
                background-color: white;
                font-size: 14px;
            }

            tr {
                height: 40px;
            }

            .dt-buttons {
                margin-left: 5px;
            }

            th, td, tr {
                text-align:center;
                vertical-align: middle;
            }

            .loader {
                position: fixed;
                left: 0px;
                top: 0px;
                width: 100%;
                height: 100%;
                z-index: 9999;
                background: url('https://i.ibb.co/cXnKsNR/Cube-1s-200px.gif') 50% 50% no-repeat rgb(249, 249, 249);
            }
        </style>
    </head>
    """
    if opts.ignorekeywords == "True":
        hide_keyword = "hidden"
    else:
        hide_keyword = ""
    
    if opts.ignorelogs == "True":
        hide_logs = "hidden"
    else:
        hide_logs = ""

    soup = BeautifulSoup(head_content, "html.parser")
    body = soup.new_tag('body')
    soup.insert(20, body)
    icons_txt = """
    <div class="loader"></div>
    <div class="sidenav">
        <a> <img class="wrimagecard" src="%s" style="height:20vh;max-width:98%%;"/> </a>
        <a class="tablink" href="#" id="defaultOpen" onclick="openPage('dashboard', this, '#fc6666')"><i class="fa fa-dashboard" style="color:CORNFLOWERBLUE"></i> Dashboard</a>
        <a class="tablink" href="#" onclick="openPage('suiteMetrics', this, '#fc6666'); executeDataTable('#sm',5)"><i class="fa fa-th-large" style="color:CADETBLUE"></i> Suite Metrics</a>
        <a class="tablink" href="#" onclick="openPage('testMetrics', this, '#fc6666'); executeDataTable('#tm',3)"><i class="fa fa-list-alt" style="color:PALEVIOLETRED"></i> Test Metrics</a>
        <a %s class="tablink" href="#" onclick="openPage('keywordMetrics', this, '#fc6666'); executeDataTable('#km',3)"><i class="fa fa-table" style="color:STEELBLUE"></i> Keyword Metrics</a>
        <a %s class="tablink" href="#" onclick="openPage('log', this, '#fc6666');"><i class="fa fa-wpforms" style="color:CHOCOLATE"></i> Logs</a>
    </div>
    """ % (logo, hide_keyword, hide_logs)

    body.append(BeautifulSoup(icons_txt, 'html.parser'))

    page_content_div = soup.new_tag('div')
    page_content_div["class"] = "main col-md-9 ml-sm-auto col-lg-10 px-4"
    body.insert(50, page_content_div)

    logging.info("1 of 4: Capturing dashboard content...")
    test_stats = TestStats()
    result.visit(test_stats)

    try:
        test_stats_obj = test_stats.all
    except:
        test_stats_obj = test_stats
    total_suite = test_stats_obj.total_suite
    passed_suite = test_stats_obj.passed_suite
    failed_suite = test_stats_obj.failed_suite
    try:
        skipped_suite = test_stats_obj.skipped_suite
    except:
        skipped_suite = 0

    #suitepp = round(passed_suite * 100.0 / total_suite, 1)
    #suitefp = round(failed_suite * 100.0 / total_suite, 1)
    elapsedtime = datetime(1970, 1, 1) + timedelta(milliseconds=result.suite.elapsedtime)
    elapsedtime = elapsedtime.strftime("%X")
    my_results = result.generated_by_robot

    if my_results:
        generator = "Robot"
    else:
        generator = "Rebot"

    stats = result.statistics
    try:
        stats_obj = stats.total.all
    except:
        stats_obj = stats.total
    total = stats_obj.total
    passed = stats_obj.passed
    failed = stats_obj.failed
    try:
        skipped = stats_obj.skipped
    except:
        skipped = 0

    #testpp = round(passed * 100.0 / total, 1)
    #testfp = round(failed * 100.0 / total, 1)

    kw_stats = KeywordStats(ignore_type)
    result.visit(kw_stats)

    total_keywords = kw_stats.total_keywords
    passed_keywords = kw_stats.passed_keywords
    failed_keywords = kw_stats.failed_keywords
    try:
        skipped_keywords = kw_stats.skipped_keywords
    except:
        skipped_keywords = 0

    # Handling ZeroDivisionError exception when no keywords are found
    # if total_keywords > 0:
    #     kwpp = round(passed_keywords * 100.0 / total_keywords, 1)
    #     kwfp = round(failed_keywords * 100.0 / total_keywords, 1)
    # else:
    #     kwpp = 0
    #     kwfp = 0

    dashboard_content = """
    <div class="tabcontent" id="dashboard">
        <div id="stats_screenshot_area">
        <div class="d-flex flex-column flex-md-row align-items-center p-1 mb-3 bg-light border-bottom shadow-sm rowcard">
            <h5 class="my-0 mr-md-auto font-weight-normal"><i class="fa fa-dashboard"></i> Dashboard</h5>
            <nav class="my-2 my-md-0 mr-md-3" style="color:#fc6666">
            <a class="p-2"><b style="color:black;">Execution Time: </b>__TIME__ h</a>
            <a class="p-2"><b style="color:black;cursor: pointer;" data-toggle="tooltip" title=".xml file is created by">Generated By: </b>__GENERATED-BY__</a>
            </nav>
        </div>

        <div class="row rowcard">

            <div class="col-md-4 border-right" onclick="openPage('suiteMetrics', this, '')" data-toggle="tooltip" 
                title="Click to view Suite metrics" style="cursor: pointer;">
                <span style="font-weight:bold; padding-left:5px;color:gray">Suite Statistics:</span>
                <table style="width:100%;height:200px;text-align: center;">
                    <tbody>
                        <tr style="height:60%">
                            <td>
                                <table style="width:100%">
                                    <tbody>
                                        <tr style="height:100%">
                                            <td style="font-size:60px; color:#2ecc71">__SPASS__</td>
                                        </tr>
                                        <tr>
                                            <td><span style="color: #999999;font-size:12px">Pass</span></td>
                                        </tr>
                                    </tbody>
                                </table>
                            </td>
                        </tr>

                        <tr style="height:25%">
                            <td>
                                <table style="width:100%">
                                    <tbody>
                                        <tr style="height:70%;font-size:25px" align="center" valign="middle">
                                            <td style="width: 33%; color:brown">__STOTAL__</td>
                                            <td style="width: 33%; color:orange">__SSKIP__</td>
                                            <td style="width: 33%; color:#fc6666">__SFAIL__</td>
                                        </tr>
                                        <tr style="height:30%" align="center" valign="top">
                                            <td style="width: 33%"><span style="color: #999999;font-size:10px">Total</span></td>
                                            <td style="width: 33%"><span style="color: #999999;font-size:10px">Skip</span></td>
                                            <td style="width: 33%"><span style="color: #999999;font-size:10px">Fail</span></td>
                                        </tr>
                                    </tbody>
                                </table>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <div class="col-md-4 borders" onclick="openPage('testMetrics', this, '')" data-toggle="tooltip" 
                            title="Click to view Test metrics" style="cursor: pointer;">
                <span style="font-weight:bold; padding-left:5px;color:gray">Test Statistics:</span>
                <table style="width:100%;height:200px;text-align: center;">
                    <tbody>
                        <tr style="height:60%">
                            <td>
                                <table style="width:100%">
                                    <tbody>
                                        <tr style="height:100%">
                                            <td style="font-size:60px; color:#2ecc71">__TPASS__</td>
                                        </tr>
                                        <tr>
                                            <td><span style="color: #999999;font-size:12px">Pass</span></td>
                                        </tr>
                                    </tbody>
                                </table>
                            </td>
                        </tr>

                        <tr style="height:25%">
                            <td>
                                <table style="width:100%">
                                    <tbody>
                                        <tr style="height:70%;font-size:25px" align="center" valign="middle">
                                            <td style="width: 33%; color:brown">__TTOTAL__</td>
                                            <td style="width: 33%; color:orange">__TSKIP__</td>
                                            <td style="width: 33%; color:#fc6666">__TFAIL__</td>
                                        </tr>
                                        <tr style="height:30%" align="center" valign="top">
                                            <td style="width: 33%"><span style="color: #999999;font-size:10px">Total</span></td>
                                            <td style="width: 33%"><span style="color: #999999;font-size:10px">Skip</span></td>
                                            <td style="width: 33%"><span style="color: #999999;font-size:10px">Fail</span></td>
                                        </tr>
                                    </tbody>
                                </table>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <div class="col-md-4 border-left" onclick="openPage('keywordMetrics', this, '')" data-toggle="tooltip" 
                            title="Click to view Keyword metrics" style="cursor: pointer;">
                <span style="font-weight:bold; padding-left:5px;color:gray">Keyword Statistics:</span>
                <table style="width:100%;height:200px;text-align: center;">
                    <tbody>
                        <tr style="height:60%">
                            <td>
                                <table style="width:100%">
                                    <tbody>
                                        <tr style="height:100%">
                                            <td style="font-size:60px; color:#2ecc71">__KPASS__</td>
                                        </tr>
                                        <tr>
                                            <td><span style="color: #999999;font-size:12px">Pass</span></td>
                                        </tr>
                                    </tbody>
                                </table>
                            </td>
                        </tr>

                        <tr style="height:25%">
                            <td>
                                <table style="width:100%">
                                    <tbody>
                                        <tr style="height:70%;font-size:25px" align="center" valign="middle">
                                            <td style="width: 33%; color:brown">__KTOTAL__</td>
                                            <td style="width: 33%; color:orange">__KSKIP__</td>
                                            <td style="width: 33%; color:#fc6666">__KFAIL__</td>
                                        </tr>
                                        <tr style="height:30%" align="center" valign="top">
                                            <td style="width: 33%"><span style="color: #999999;font-size:10px">Total</span></td>
                                            <td style="width: 33%"><span style="color: #999999;font-size:10px">Skip</span></td>
                                            <td style="width: 33%"><span style="color: #999999;font-size:10px">Fail</span></td>
                                        </tr>
                                    </tbody>
                                </table>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>

        </div>
        <hr/>
        <div class="row rowcard">
            <div class="col-md-4" style="height:280px;width:auto;">
                <span style="font-weight:bold;color:gray">Suite Status:</span>
                <div id="suiteChartID" style="height:250px;width:auto;"></div>
            </div>
            <div class="col-md-4" style="height:280px;width:auto;">
                <span style="font-weight:bold;color:gray">Test Status:</span>
                <div id="testChartID" style="height:250px;width:auto;"></div>
            </div>
            <div class="col-md-4" style="height:280px;width:auto;">
                <span style="font-weight:bold;color:gray">Keyword Status:</span>
                <div id="keywordChartID" style="height:250px;width:auto;"></div>
            </div>
        </div>
        <hr/>
        <div class="row rowcard">
            <div class="col-md-12" style="height:450px;width:auto;">
                <span style="font-weight:bold;color:gray">Top 10 Suite Performance(sec):</span>
                <div id="suiteBarID" style="height:400px;width:auto;"></div>
            </div>
        </div>
        <hr/>
        <div class="row rowcard">
            <div class="col-md-12" style="height:450px;width:auto;">
                <span style="font-weight:bold;color:gray">Top 10 Test Performance(sec):</span>
                <div id="testsBarID" style="height:400px;width:auto;"> </div>
            </div>
        </div>
        <hr/>
        <div class="row rowcard" __KHIDE__>
            <div class="col-md-12" style="height:450px;width:auto;">
                <span style="font-weight:bold;color:gray">Top 10 Keywords Performance(sec):</span>
                <div id="keywordsBarID" style="height:400px;width:auto;"></div>
            </div>
        </div>
        <div class="row">
            <div class="col-md-12" style="height:25px;width:auto;">
                <p class="text-muted" style="text-align:center;font-size:9px">
                    <a href="https://github.com/adiralashiva8/robotframework-metrics" target="_blank" style="color:gray">robotframework-metrics</a>
                </p>
            </div>
        </div>

       <script>
            window.onload = function(){
                executeDataTable('#sm',6);
                executeDataTable('#tm',3);
                executeDataTable('#km',3);
                createPieChart(__SPASS__,__SFAIL__,__SSKIP__,'suiteChartID','Suite Status:');
                createBarGraph('#sm',0,6,10,'suiteBarID','Elapsed Time (s) ','Suite');
                createPieChart(__TPASS__,__TFAIL__,__TSKIP__,'testChartID','Tests Status:');
                createBarGraph('#tm',1,3,10,'testsBarID','Elapsed Time (s) ','Test');
                createPieChart(__KPASS__,__KFAIL__,__KSKIP__,'keywordChartID','Keywords Status:');
                createBarGraph('#km',1,3,10,'keywordsBarID','Elapsed Time (s) ','Keyword');
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
    """

    dashboard_content = dashboard_content.replace("__TIME__", str(elapsedtime))
    dashboard_content = dashboard_content.replace("__GENERATED-BY__", str(generator))
    dashboard_content = dashboard_content.replace("__STOTAL__", str(total_suite))
    dashboard_content = dashboard_content.replace("__SPASS__", str(passed_suite))
    dashboard_content = dashboard_content.replace("__SFAIL__", str(failed_suite))
    dashboard_content = dashboard_content.replace("__SSKIP__", str(skipped_suite))
    dashboard_content = dashboard_content.replace("__TTOTAL__", str(total))
    dashboard_content = dashboard_content.replace("__TPASS__", str(passed))
    dashboard_content = dashboard_content.replace("__TFAIL__", str(failed))
    dashboard_content = dashboard_content.replace("__TSKIP__", str(skipped))
    dashboard_content = dashboard_content.replace("__KTOTAL__", str(total_keywords))
    dashboard_content = dashboard_content.replace("__KPASS__", str(passed_keywords))
    dashboard_content = dashboard_content.replace("__KFAIL__", str(failed_keywords))
    dashboard_content = dashboard_content.replace("__KSKIP__", str(skipped_keywords))
    dashboard_content = dashboard_content.replace("__KHIDE__", str(hide_keyword))

    page_content_div.append(BeautifulSoup(dashboard_content, 'html.parser'))

    ### ============================ END OF DASHBOARD ============================================ ####
    logging.info("2 of 4: Capturing suite metrics...")
    ### ============================ START OF SUITE METRICS ======================================= ####

    # Tests div
    suite_div = soup.new_tag('div')
    suite_div["id"] = "suiteMetrics"
    suite_div["class"] = "tabcontent"
    page_content_div.insert(50, suite_div)

    test_icon_txt = """
                    <h4><b><i class="fa fa-table"></i> Suite Metrics</b></h4>
                    <hr></hr>
                    """
    suite_div.append(BeautifulSoup(test_icon_txt, 'html.parser'))

    # Create table tag
    table = soup.new_tag('table')
    table["id"] = "sm"
    table["class"] = "table row-border tablecard"
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
    th.string = "Fail"
    tr.insert(5, th)

    th = soup.new_tag('th')
    th.string = "Time (s)"
    tr.insert(6, th)

    suite_tbody = soup.new_tag('tbody')
    table.insert(11, suite_tbody)

    result.visit(SuiteResults(soup, suite_tbody, log_name, opts.fullsuitename))

    test_icon_txt = """
    <div class="row">
        <div class="col-md-12" style="height:25px;width:auto;"></div>
    </div>
    """
    suite_div.append(BeautifulSoup(test_icon_txt, 'html.parser'))

    ### ============================ END OF SUITE METRICS ============================================ ####
    logging.info("3 of 4: Capturing test metrics...")
    ### ============================ START OF TEST METRICS ======================================= ####

    # Tests div
    tm_div = soup.new_tag('div')
    tm_div["id"] = "testMetrics"
    tm_div["class"] = "tabcontent"
    page_content_div.insert(100, tm_div)

    test_icon_txt = """
    <h4><b><i class="fa fa-table"></i> Test Metrics</b></h4>
    <hr></hr>
    """
    tm_div.append(BeautifulSoup(test_icon_txt, 'html.parser'))

    # Create table tag
    table = soup.new_tag('table')
    table["id"] = "tm"
    table["class"] = "table row-border tablecard"
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

    th = soup.new_tag('th')
    th.string = "Error Message"
    tr.insert(4, th)

    if opts.showtags == "True":
        th = soup.new_tag('th')
        th.string = "Tags"
        tr.insert(5, th)

    test_tbody = soup.new_tag('tbody')
    table.insert(11, test_tbody)

    # GET TEST METRICS
    result.visit(TestResults(soup, test_tbody, log_name, opts.fullsuitename, opts.showtags))

    test_icon_txt = """
    <div class="row">
        <div class="col-md-12" style="height:25px;width:auto;"></div>
    </div>
    """
    tm_div.append(BeautifulSoup(test_icon_txt, 'html.parser'))
    
    ### ============================ END OF TEST METRICS ============================================ ####
    logging.info("4 of 4: Capturing keyword metrics...")
    ### ============================ START OF KEYWORD METRICS ======================================= ####

    # Keywords div
    km_div = soup.new_tag('div')
    km_div["id"] = "keywordMetrics"
    km_div["class"] = "tabcontent"
    page_content_div.insert(150, km_div)

    keyword_icon_txt = """
    <h4><b><i class="fa fa-table"></i> Keyword Metrics</b></h4>
      <hr></hr>
    """
    km_div.append(BeautifulSoup(keyword_icon_txt, 'html.parser'))

    # Create table tag
    # <table id="myTable">
    table = soup.new_tag('table')
    table["id"] = "km"
    table["class"] = "table row-border tablecard"
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

    kw_tbody = soup.new_tag('tbody')
    table.insert(1, kw_tbody)

    if opts.ignorekeywords == "True":
        pass
    else:
        if group:
            group.spawn(result.visit, KeywordResults(soup, kw_tbody, ignore_type))
            group.join()
        else:
            result.visit(KeywordResults(soup, kw_tbody, ignore_type))

    test_icon_txt = """
    <div class="row">
        <div class="col-md-12" style="height:25px;width:auto;"></div>
    </div>
    """
    km_div.append(BeautifulSoup(test_icon_txt, 'html.parser'))
    # END OF KEYWORD METRICS

    # START OF LOGS

    # Logs div
    if opts.ignorelogs == "True":
        pass
    else:
        log_div = soup.new_tag('div')
        log_div["id"] = "log"
        log_div["class"] = "tabcontent"
        page_content_div.insert(200, log_div)

        test_icon_txt = """
            <p style="text-align:right">** <b>Report.html</b> and <b>Log.html</b> need to be in current folder in 
            order to display here</p>
        <div class="embed-responsive embed-responsive-4by3">
            <iframe class="embed-responsive-item" src=%s></iframe>
        </div>
        """ % log_name
        log_div.append(BeautifulSoup(test_icon_txt, 'html.parser'))

    # END OF LOGS
    script_text = """
        <script>
            function createPieChart(passed_count, failed_count, skipped_count, ChartID, ChartName){
            var status = [];
            status.push(['Status', 'Percentage']);
            status.push(['PASS',parseInt(passed_count)],['FAIL',parseInt(failed_count)],['SKIP',parseInt(skipped_count)]);
            var data = google.visualization.arrayToDataTable(status);

            var options = {
            pieHole: 0.6,
            legend: 'none',
            chartArea: {width: "95%",height: "90%"},
            colors: ['#2ecc71', '#fc6666', '#ffa500'],
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
                    fontSize: 12,
                    //bold: true,
                    italic: true,
                    color: "black",     // The color of the text.
                    },
                },
                hAxis: {
                    textStyle: {
                        //fontName: 'Arial',
                        fontName: 'Comic Sans MS',
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
                "aoColumnDefs": [ {
                    "aTargets": [ -1, -2 ],
                    "mRender": function ( data, type, full ) {
                        return $("<div/>").html(data).text(); 
                    }
                } ],
                buttons: [
                    {
                        extend:    'copyHtml5',
                        text:      '<i class="fa fa-files-o"></i>',
                        filename: function() {
                            return fileTitle + '-' + new Date().toLocaleString();
                        },
                        titleAttr: 'Copy',
                        exportOptions: {
                            columns: ':visible'
                        }
					},

                    {
                        extend:    'csvHtml5',
                        text:      '<i class="fa fa-file-text-o"></i>',
                        titleAttr: 'CSV',
                        filename: function() {
                            return fileTitle + '-' + new Date().toLocaleString();
                        },
                        exportOptions: {
                            columns: ':visible'
                        }
                    },

                    {
                        extend:    'excelHtml5',
                        text:      '<i class="fa fa-file-excel-o"></i>',
                        titleAttr: 'Excel',
                        filename: function() {
                            return fileTitle + '-' + new Date().toLocaleString();
                        },
                        exportOptions: {
                            columns: ':visible'
                        }
                    },
                    {
                        extend:    'print',
                        text:      '<i class="fa fa-print"></i>',
                        titleAttr: 'Print',
                        exportOptions: {
                            columns: ':visible',
                            alignment: 'left',
                        }
                    },
                    {
                        extend:    'colvis',
                        collectionLayout: 'fixed two-column',
                        text:      '<i class="fa fa-low-vision"></i>',
                        titleAttr: 'Hide Column',
                        exportOptions: {
                            columns: ':visible'
                        },
                        postfixButtons: [ 'colvisRestore' ]
                    },
                ],
                columnDefs: [ {
                    visible: false,
                } ]
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
            tablinks[i].style.color = "";
        }
        document.getElementById(pageName).style.display = "block";
        elmnt.style.color = color;

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

    # WRITE TO RF_METRICS_REPORT.HTML

    # Write output as html file
    with open(result_file, 'w') as outfile:
        outfile.write(soup.prettify())

    logging.info("Results file created successfully and can be found at {}".format(result_file))