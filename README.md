# Robot Framework Metrics Report

Creates HTML Metrics report based on robotframework output.xml.

[![HitCount](http://hits.dwyl.io/adiralashiva8/robotframework-metrics.svg)](http://hits.dwyl.io/adiralashiva8/robotframework-metrics)
![Github All Releases](https://img.shields.io/github/downloads/adiralashiva8/robotframework-metrics/total.svg)
![Github Releases (by Release)](https://img.shields.io/github/downloads/adiralashiva8/robotframework-metrics/v3.1.1/total.svg)
![GitHub release](https://img.shields.io/github/release/adiralashiva8/robotframework-metrics.svg)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/adiralashiva8/robotframework-metrics.svg)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
[![Open Source Love png1](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://github.com/ellerbrock/open-source-badges/)

---
 - __Sample Report__ [link](https://robotframework-metrics.netlify.com/)
 - What's new in __v3.1.1_ [link](https://github.com/adiralashiva8/robotframework-metrics/releases/tag/v3.1.1)

---

#### How it Works:

1. Read output.xml file using robotframework API
2. Get Suite, Test Case , Keyword , Status and Elapsed time values
3. Convert data to html report using Beautifulsoup

---

#### How to use in project:

1. Download __robotmetrics.py__ from here [link](https://github.com/adiralashiva8/robotframework-metrics/releases/download/v3.1.1/robotmetrics.py)

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
    
5. RobotFramework Metrics Report __metric-timestamp.html__ file will be created in current folder | `-inputpath` if specified

6. Email will be sent to mentioned recepient with __metric-timestamp.html__ file

---

#### Customize Report

Specify Logo and custom links in Robotframework metrics: 

 - __Custom Logo__ : Customize your logo by modifying __robotmetrics.py__ file at line no: 21

     ```
     logo = "https://cdn.pixabay.com/photo/2016/08/02/10/42/wifi-1563009_960_720.jpg"
     ```
 
 - __Custom Links__ : You can customize your links in report by modifying __robotmetrics.py__ file at line no: 309-320. Modify href and text

    ```
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
    ```
 
---
#### How to Specifiy EMAIL recepients
 - In __robotmetrics.py__ file add specific TO, FROM, SUBJECT, EMAIL server and etc., info (line no:98-113)

    ```
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
    ``` 

---
#### How to Disable EMAIL
 - By default email will be sent to mentioned recpients when .py file is executed. Using -email false (or) -email f can disable send email.

    ```
    python robotmetrics.py -email false
    ```

 - Email will be sent when following condition is met 
    ```
    -email true | 1 | t | y | yes
    ``` 
---

#### How to Ignore Library Keywords in Metrics Report
 - In __robotmetrics.py__ file add specific library keywords __ignore_library__
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

Execute .py file after suite or test execution as follows:

 - Create .bat (or) .sh file with following snippet

    ```
    robot test.robot &&
    python robotmetrics.py
    ```

    > && is used to execute multiple command's in .bat file

  - Modify robot command as required and execute .bat file
  
  - Robotframework metrics will be created after execution

---

Thanks for using robotframework-metrics!

 - What is your opinion of this report?
 - What’s the feature I should add?

If you have any questions / suggestions / comments on the report, please feel free to reach me on adiralashiva8@gmail.com  
 
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
