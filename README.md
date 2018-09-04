# Robot Framework Metrics Report

Creates HTML Metrics report based on robotframework output.xml

---

*How it Works:*

1. Read output.xml file using robotframework API (robot.result.model)
2. Get Suite, Test Case , Keyword , Status, Start Time, End Time and Elapsed time values using api
3. Convert data to html report using Beautifulsoup

---

*How to use in project:*

1. Clone project or download here [link](https://github.com/adiralashiva8/robotframework-metrics/archive/master.zip)

    ```
    git clone https://github.com/adiralashiva8/robotframework-metrics.git
    ```

2. Copy __rf_metrics_report_creator.py__ file to project (where output.xml file is available.)

    > Note: __output.xml__ file name having timestamp is recognized by Metrics Report

    > output.xml, report.html and log.html need to be within same folder.

3. Install beautifulsoup: (to create html report - one time activity)

    ```
    pip install beautifulsoup4
    ```

4. Execute __rf_metrics_report_creator.py__ file

    ```
    python rf_metrics_report_creator.py
    ```

5. RobotFramework Metrics Report __rf_metrics_result.html__ file will be created in current folder

---

 *Sample Report:*

 __DASHBOARD__

![Screenshot](Images/Dashboard_1.png)

![Screenshot](Images/Dashboard_2.png)

![Screenshot](Images/Dashboard_3.png)

__SUITE METRICS__

 ![Screenshot](Images/Suite_Metrics.png)
 
__TEST METRICS__

 ![Screenshot](Images/Test_Metrics.png)
 
__KEYWORD METRICS__

 ![Screenshot](Images/Keyword_Metrics.png)

__ROBOT LOG__

 ![Screenshot](Images/Robot_Logs.png)

 __EMAIL STATISTICS__


 ![Screenshot](Images/Email_Statistics.png)


 ![Screenshot](Images/Email_Statistics_Email.png)


---

*How to Ignore Library Keywords in Metrics Report*
 - In __rf_metrics_report_creator.py__ file add specific library keywords to tuple __ignore_library__ to ignore in report
 - In Metric report, keywords with type value 'for' and 'foritem' are ignored
 - Following library keywords are ignored in Metrics Report
    ```
    ignore_library = [
     'BuiltIn',
     'SeleniumLibrary',
     'String',
     'Collections',
     'DateTime',
    ] 
    ```

---

*Credits:*

1. Robotframework [link](http://robotframework.org)
2. W3Schools [link](http://www.w3schools.com)
3. Stackoverflow [link](http://stackoverflow.com)
4. Google charts [link](https://developers.google.com/chart/)
5. DataTable [link](https://datatables.net)
6. BeautifulSoup [link](http://beautiful-soup-4.readthedocs.io)
7. Jquery | JavaScript [link](https://www.jqueryscript.net)
8. Bootstrap [link](https://getbootstrap.com/)
9. Icons8 [link](https://icons8.com/)
10. FontAwesome [link](https://fontawesome.com)

---

> You are watching first HTML 'Metrics Report' in Robot framework.

---
