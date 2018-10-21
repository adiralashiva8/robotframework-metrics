# Robot Framework Metrics Report 

Creates HTML Metrics report based on robotframework output.xml. Sample report [link](https://robotframework-metrics-v-3-1.netlify.com/#)

[![HitCount](http://hits.dwyl.io/adiralashiva8/robotframework-metrics.svg)](http://hits.dwyl.io/adiralashiva8/robotframework-metrics)
![Github All Releases](https://img.shields.io/github/downloads/adiralashiva8/robotframework-metrics/total.svg)
![GitHub release](https://img.shields.io/github/release/adiralashiva8/robotframework-metrics.svg)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/adiralashiva8/robotframework-metrics.svg)

---

*How it Works:*

1. Read output.xml file using robotframework API
2. Get Suite, Test Case , Keyword , Status, Start Time, End Time and Elapsed time values
3. Convert data to html report using Beautifulsoup

---

*How to use in project:*

1. Download __robotmetrics.py__ from here [link](https://github.com/adiralashiva8/robotframework-metrics/releases/download/v3-1/robotmetrics.py)

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

*Customize Report*

Specify Logo and custom links in Robotframework metrics: 

 - __Custom Logo__ : Customize your logo by modifying __robotmetrics.py__ file at line no: 37
 ```
 logo = "https://cdn.pixabay.com/photo/2016/08/02/10/42/wifi-1563009_960_720.jpg"
 ```
 
 - __Custom Links__ : You can customize your links in report by modifying __robotmetrics.py__ file at line no: 312-323. Modify href and text
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
*How to Specifiy EMAIL recepients*
 - In __robotmetrics.py__ file add specific TO, FROM, SUBJECT, EMAIL server and etc., info (line no:18-30)
    ```
    server = smtplib.SMTP('smtp.gmail.com:587')
    msg = email.message.Message()
    msg['Subject'] = 'Automation Status'

    sender = 'me@gmail.com'
    recipients = ['user1@gmail.com', 'user2@yahoo.com','user3@hotmail.com']

    msg['From'] = sender
    msg['To'] = ", ".join(recipients)
    password = "xxxxxxxxxxxxxxxxxx"
    ``` 
---

*How to Ignore Library Keywords in Metrics Report*
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

Thanks for using robotframework-metrics!

 - What is your opinion of this report?
 - What’s one the most important feature we should add?

If you have any questions/suggestions/comments on the report, please feel free to reach me on adiralashiva8@gmail.com  

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
