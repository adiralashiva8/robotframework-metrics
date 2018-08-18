# Robot Framework Metrics Report

Aim of this project is to create HTML report based on robot framework output.xml (To analyze TESTS, KEYWORDS in entire suite | test execution)

---

*How it Works:*

1. Read output.xml file using robotframework api (robot.result.model)
2. Get Test Case Name , Keyword Name, Status, Start Time, End Time and Elapsed time values using api
3. Convert data to html report using Beautifulsoup (Tabular format with sorting | pagination | search entire table | sort in search result)

---

*How to use in project:*

1. Clone project
    ```
    git clone https://github.com/adiralashiva8/robotframework-metrics.git
    ```
2. Copy __rf_metrics_report_creator.py__ and __rf_metrics_executer.sh__ files to project (where output.xml file is available)
3. Install beautifulsoup: (to create html report - one time activity)
    ```
    pip install beautifulsoup4
    ```
4. Execute __rf_metrics_executer.sh__ file
5. __Robotframework Metrics Report__ will be launched in new chrome tab

---

 Sample Report:(Tabular format with sorting | pagination | search entire table | sort in search result )
 
 Dashboard: (Consist of Keywords, Tests status charts)

 __WEB__
 ![Screenshot](web_dashboard.JPG)

 __SMALL_SCREEN__
 ![Screenshot](mobile_dashboard.JPG)

 Test Metrics:  (Test Metrics - Sort by Elapsed time descending order)

  __WEB__
 ![Screenshot](Web_Test_Metrics.JPG)

 __SMALL_SCREEN__
 ![Screenshot](mobile_test_metrics.JPG)

 Keyword Metrics: (Keywords Metrics - Sort by Elapsed time descending order)

 __WEB__
 ![Screenshot](web_keyword_metrics.JPG)
 
 __SMALL_SCREEN__
 ![Screenshot](mobile_keyword_metrics.JPG)

---

*Credits:*

1. Robotframework
2. W3Schools
3. Stackoverflow
4. CanvasJs
5. DataTable
6. BeautifulSoup
7. Jquery | JavaScript
8. Bootstrap

---

> You are watching first HTML 'Metrics Report' in Robot framework :)

---