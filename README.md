# Robot Framework Metrics Report

Creates custom HTML report (dashboard view) by parsing robotframework output.xml file

[![PyPI version](https://badge.fury.io/py/robotframework-metrics.svg)](https://badge.fury.io/py/robotframework-metrics)
[![Downloads](https://pepy.tech/badge/robotframework-metrics)](https://pepy.tech/project/robotframework-metrics)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
[![Open Source Love png1](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://github.com/ellerbrock/open-source-badges/)

---
 - __Sample Report__ [link](https://rfmetrics.netlify.com/)

 - Whats new in __v3.3.1__ [link](https://github.com/adiralashiva8/robotframework-metrics/releases/tag/v3.3.1)

---

#### How it Works:

1. Read `output.xml` file using `robot.api - ResultVisitor, ExecutionResult` [API Link](https://robot-framework.readthedocs.io/en/stable/autodoc/robot.result.html)

2. Get Suite, Test Case , Keyword , Status and Elapsed time values

3. Convert data to html report

---

#### How to use in project:

__Step 1__ Install robotmetrics 

   > Case 1: Using pip
   ```
   pip install robotframework-metrics==3.3.1
   ```
   > Case 2: Using setup.py (clone project and run command within root)
   ```
   python setup.py install
   ```
   > Case 3: For latest changes use following command (pre-release or changes in master)
   ```
   pip install git+https://github.com/adiralashiva8/robotframework-metrics
   ```

__Step 2__ Execute robotmetrics command to generate report

   > Case 1: No change in output.xml file name (assumig user is in same folder)
   ```
   robotmetrics
   ```
   > Case 2: output.xml under 'Result' folder
   ```
   robotmetrics --inputpath ./Result/ --output output1.xml
   ```

   > For more info on command line options use:

   ```
   robotmetrics --help
   ```

---

#### Generate robotframework-metrics after execution

Execute robotmetrics command after suite or test execution as follows:

 - Create .bat (or) .sh file with following snippet

    ```
    robot test.robot &
    robotmetrics [:options]
    ```

    > & is used to execute multiple command's in .bat file

  - Modify robotmetrics command as required and execute .bat file

  - Robotframework metrics will be created after execution

---

If you have any questions / suggestions / comments on the report, please feel free to reach me at

 - Email: <a href="mailto:adiralashiva8@gmail.com?Subject=Robotframework%20Metrics" target="_blank">`adiralashiva8@gmail.com`</a> 

---

*Special Thanks To:*

*Idea, Guidance and Support:*

 - Steve Fisher
 - Goutham Duduka


*Contributors:*

1. [Pekka Klarck](https://www.linkedin.com/in/pekkaklarck/) [Author of robotframework]

2. [Ruud Prijs](https://www.linkedin.com/in/ruudprijs/)


3. [Jesse Zacharias](https://www.linkedin.com/in/jesse-zacharias-7926ba50/)

4. [Bassam Khouri](https://www.linkedin.com/in/bassamkhouri/)

5. [Francesco Spegni](https://www.linkedin.com/in/francesco-spegni-34b39b61/)

6. [Sreelesh Kunnath](https://www.linkedin.com/in/kunnathsree/)


*Feedback:*

1. [Mantri Sri](https://www.linkedin.com/in/mantri-sri-4a0196133/)
2. [Prasad Ozarkar](https://www.linkedin.com/in/prasad-ozarkar-b4a61017/)
3. [Suresh Parimi](https://www.linkedin.com/in/sparimi/)
4. [Robotframework community users](https://groups.google.com/forum/#!forum/robotframework-users)

---

:star: repo if you like it

---
