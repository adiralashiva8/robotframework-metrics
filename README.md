# Robot Framework Metrics Report

Creates HTML Metrics report based on robotframework output.xml

---

*How it Works:*

1. Read output.xml file using robotframework API
2. Get Suite, Test Case , Keyword , Status, Start Time, End Time and Elapsed time values using api
3. Convert data to html report using Beautifulsoup

---

*How to use in project:*

1. Download __robotmetrics.py__ from here [link](https://github.com/adiralashiva8/robotframework-metrics/releases/download/v3.0/robotframework-metrics-master.zip)

    > Repo has some extra files (.html and .xml for testing) - I suggest to download from link

2. Copy __robotmetrics.py__ file to project

3. Install beautifulsoup: (to create html report - one time activity)

    ```
    pip install beautifulsoup4
    ```

4. Execute __robotmetrics.py__ file

    > Case 1: robotmetrics.py is copied where output.xml is available

    ```
    python robotmetrics.py
    ```

    > Case 2: Specify output.xml file path. (When .xml and .html file names are same)

    ```
    python robotmetrics.py -inputpath .\Result\
    ```
    
    > Case 3: Specify file name. (When .xml and .html file names are altered)

    ```
    python robotmetrics.py -inputpath .\Result\ -output voutput.xml -report vreport.html -log vlog.html
    ```
    
5. RobotFramework Metrics Report __metric-<timestamp>.html__ file will be created in current folder | `-inputpath` if specified

---

 Sample report [link](https://robotframework-metrics-report.netlify.com/#)

---

*How to Ignore Library Keywords in Metrics Report*
 - In __robotmetrics.py__ file add specific library keywords to tuple __ignore_library__ to ignore in report
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

1. Robotframework [link](https://robot-framework.readthedocs.io/en/v3.0.4/autodoc/robot.result.html)
2. Stackoverflow [link](http://stackoverflow.com)
3. Google charts [link](https://developers.google.com/chart/)
4. DataTable [link](https://datatables.net/examples/basic_init/table_sorting.html)
5. BeautifulSoup [link](http://beautiful-soup-4.readthedocs.io)
6. Jquery | JavaScript [link](https://www.jqueryscript.net)
7. Bootstrap [link](http://getbootstrap.com/docs/4.1/examples/dashboard/)
8. Icons8 [link](https://icons8.com/)
9. FontAwesome [link](https://fontawesome.com)

---