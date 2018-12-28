# Robot Framework Metrics Report

Creates HTML Metrics report based on robotframework output.xml.

[![HitCount](http://hits.dwyl.io/adiralashiva8/robotframework-metrics.svg)](http://hits.dwyl.io/adiralashiva8/robotframework-metrics)
![Github All Releases](https://img.shields.io/github/downloads/adiralashiva8/robotframework-metrics/total.svg)
![Github Releases (by Release)](https://img.shields.io/github/downloads/adiralashiva8/robotframework-metrics/v3.1.1/total.svg)
![GitHub release](https://img.shields.io/github/release/adiralashiva8/robotframework-metrics.svg)
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

1. Install robotmetrics 

    > Case 1: Using pip
    ```
    pip install robotmetrics
    ```
    > Case 2: Clone project
    ```
    python setup.py install
    ```

2. Execute robotmetrics command to generate report

    > Specifying all command options

    ```
    robotmetrics --inputpath ./Result/ --output "output1.xml" --log "log1.html" --report "report1.html" --email false 
    ```

    > For help:

    ```
    robotmetrics --help
    ```
    
3. RobotFramework Metrics Report __metric-timestamp.html__ file will be created in current folder | `-inputpath` if specified

4. Email will be sent to mentioned recepient with __metric-timestamp.html__ file

---

#### Customize Report

Specify Logo in Robotframework metrics: 

 - __Custom Logo__ : Customize your logo by using --logo command line option

     ```
     --logo "https://encrypted-tbn0.gstatic.com/images"
     ```
---
#### How to Specifiy EMAIL recepients
 - Default robotmetrics uses gmail server. From command line users have to specific FROM, PWD, TO and CC

    ```
    robotmetrics --email true --from "user1@gmail.com" --pwd "***********" --to "user2@gmail.com,user3@yahoo.com"
     --cc "user4@yahoo.com,user5@gmail.com" 
    
    ``` 

---
#### How to Disable EMAIL
 - By default email will be sent to mentioned recipients when robotmetrics command is executed. Using --email false can disable email

    ```
    robotmetrics --email false
    ```

 - Email will be sent when following condition is met 
    ```
    --email true | True
    ``` 
---

#### How to Ignore Library Keywords in Metrics Report
 - Use command line options to ignore library keywords
    ``` 
    --ignore Collections
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

*Special Thanks To:*

*Contributors:*

1. Pekka Klarck
    > - Contributed source to get 'Test Case' name from keyword 
    > - Suggested to use robotframework api for output.xml content 
2. Ruud Prijs
    > - Contributed source to use command line options for report
3. Jesse Zacharias
    > - Made robotmetrics installable
    > - Contributed source to improve performance

*Feedback:*

1. Mantri Sri
2. Prasad Ozarkar
3. And Others

---