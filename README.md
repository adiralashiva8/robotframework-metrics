# Robot Framework Metrics Report

Creates HTML Metrics report based on robotframework output.xml.

[![PyPI version](https://badge.fury.io/py/robotframework-metrics.svg)](https://badge.fury.io/py/robotframework-metrics)
[![Downloads](https://pepy.tech/badge/robotframework-metrics)](https://pepy.tech/project/robotframework-metrics)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
[![Open Source Love png1](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://github.com/ellerbrock/open-source-badges/)

---
 - __Sample Report__ [link](https://robotmetrics.netlify.com/)
 - What's new in __v3.1.2_ [link](https://github.com/adiralashiva8/robotframework-metrics/releases/tag/v3.1.2)
 - Source Code used to parse output.xml in metrics report [link](https://adiralashivaprasad.blogspot.com/2019/01/how-to-get-suite-test-and-keyword.html)

---

#### How it Works:

1. Read output.xml file using robotframework API
2. Get Suite, Test Case , Keyword , Status and Elapsed time values
3. Convert data to html report using Beautifulsoup

---

#### How to use in project:

1. Install robotmetrics 

    > Case 1: Using pip
    ```
    pip install robotframework-metrics==3.1.2
    ```
    > Case 2: Using setup.py (clone project and run command within root)
    ```
    python setup.py install
    ```
    > Case 3: For latest changes use following command (pre-release or changes in master)
    ```
    pip install git+https://github.com/adiralashiva8/robotframework-metrics
    ```

2. Execute robotmetrics command to generate report

    > Case 1: No change in output.xml, log.html file name's and user is in same folder
    ```
    robotmetrics
    ```
    > Case 2: Change in output.xml, log.html file name's And .xml and .html files are under 'Result' folder
    ```
    robotmetrics --inputpath ./Result/ --output "output1.xml" --log "log1.html"
    ```
    robotframework-metrics can parse multiple xmls at a time. Following is the command
    ```
    robotmetrics --inputpath ./Result/ --output "output1.xml,output2.xml" --log "log1.html"
    ```
    
    > For more info on command line options use:

    ```
    robotmetrics --help
    ```
    
3. RobotFramework Metrics Report __metric-timestamp.html__ file will be created in current folder | `-inputpath` if specified

Note: From v3.1.4 users can specify __custom_report_name__ instead of __metrics-timestamp.html__ (changes in master)
```
robotmetrics -M regression_metrics.html
```

---

#### Customize Report

Specify Logo in Robotframework metrics: 

 - __Custom Logo__ : Customize your logo by using --logo command line option

     ```
     --logo "https://mycompany/logo.jpg"
     ```
---

#### How to Ignore Library Keywords in Metrics Report
 - Use command line options to ignore library keywords
    ``` 
    --ignore "Collections,Selenium2Library"
    ```
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

#### Generate robotframework-metrics after execution

Execute robotmetrics command after suite or test execution as follows:

 - Create .bat (or) .sh file with following snippet

    ```
    robot test.robot &&
    robotmetrics [:options]
    ```

    > && is used to execute multiple command's in .bat file

  - Modify robotmetrics command as required and execute .bat file
  
  - Robotframework metrics will be created after execution

---

*Performance Improvement (Beta) *

 - Do you feel robotmetrics command taking more time to capture metrics? Robotframework-metrics have ability to process metrics in parallel using gevent (which helps in saving time)
 > - Step 1: Install gevent
 > - Step 2: Execute robotmetrics command

---

Thanks for using robotframework-metrics!

 - What is your opinion of this report?
 - What’s the feature I should add?

If you have any questions / suggestions / comments on the report, please feel free to reach me at

 - Email: <a href="mailto:adiralashiva8@gmail.com?Subject=Robotframework%20Metrics" target="_blank">`adiralashiva8@gmail.com`</a> 
 - Slack: <a href="https://robotframework.slack.com/messages/robotframeworkmetrics" target="_blank">`robotframeworkmetrics`</a>
 - LinkedIn: <a href="https://www.linkedin.com/in/shivaprasadadirala/" target="_blank">`shivaprasadadirala`</a>
 - Twitter: <a href="https://twitter.com/ShivaAdirala" target="_blank">`@ShivaAdirala`</a>

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

> Note: Robotframework-metrics uses above open source libraries for generating report.

---

*Special Thanks To:*

*Contributors:*

1. [Pekka Klarck](https://www.linkedin.com/in/pekkaklarck/) [Author of robotframework]
    > - Contributed source to get 'Test Case' name from keyword 
    > - Suggested to use robotframework api to parse output.xml content 

2. [Ruud Prijs](https://www.linkedin.com/in/ruudprijs/)
    > - Contributed source to use command line options for report

3. [Jesse Zacharias](https://www.linkedin.com/in/jesse-zacharias-7926ba50/)
    > - Made robotmetrics installable (pip)
    > - Contributed source to improve performance

4. [Bassam Khouri](https://www.linkedin.com/in/bassamkhouri/)
    > - Contributed source to use ArgParser
    > - Contributed source to provide a human readable error if output.xml does not exist

5. [Francesco Spegni](https://www.linkedin.com/in/francesco-spegni-34b39b61/)
    > - Contributed source to parse multiple xml's
    > - Fixed distorted image

6. [Sreelesh Kunnath](https://www.linkedin.com/in/kunnathsree/)
    > - Contributed source to specify custom metrics file name (changes will be from v3.1.4)


*Feedback:*

1. [Mantri Sri](https://www.linkedin.com/in/mantri-sri-4a0196133/)
2. [Prasad Ozarkar](https://www.linkedin.com/in/prasad-ozarkar-b4a61017/)
3. [Suresh Parimi](https://www.linkedin.com/in/sparimi/)
4. [Robotframework community users](https://groups.google.com/forum/#!forum/robotframework-users)

*Thank you for your guidance, support and Idea:*

 - Steve
 - [Goutham Duduka](https://www.linkedin.com/in/goutham-kumar-duduka-45154718/)

---
