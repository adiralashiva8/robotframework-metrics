# Keywords Performance Metrics Report in Robot Framework

Aim of this project is to create HTML report based on robot framework output.xml (To analyze time took by each keyword in entire suite|test execution)

*How it Works:*

1. Read output.xml file (which will be created after script execution)
2. Get Test Case Name (test tag) , Keyword Name (kw tag) , Start Time, End Time (status tag) values from output.xml file
3. Convert data to html report using Beautifulsoap (Tabular format with sorting | pagination | search entire table | sort in search result)

*How to use in project:*

1. Checkout the project
2. Copy __keyword_performance_metrics_report_creator.py__ and __keyword_performance_metrics_executer.bat__ files to project (where output.xml file is available)
3. Install beautifulsoap: __pip install beautifulsoup4__  (to create html report)
4. Install lxml: __pip install lxml__ (to read data from xml file)
5. Execute keyword_performance_metrics_executer.bat file
6. "Keywords Performance Metrics Report" will be opened in new chrome tab
 
 Sample Report:(Tabular format with sorting | pagination | search entire table | sort in search result )
 
 ![Screenshot](Keywords_Performance_Metrics.PNG)

*How to Ignore Library Keywords in metrics*
 - In __keyword_performance_metrics_report_creator.py__ file add library to ignore for tuple:'ignore_library'
 - In this report keywords with type value 'for' and 'foritem' are ignored
 - Following library keywords are ignored in metrics
    ```
    ignore_library = [
     'BuiltIn',
     'SeleniumLibrary',
     'String',
     'Collections',
     'DateTime',
    ] 
    ```

Intention of project is to help the guys who are monitoring there keywords performance

 - Checkout the project.
 - Try within your project.
 - Suggest your feedback/queries
 - Let us improve this report together

** I want to check this report with larger automation suites (50 + test cases). To verify how the report behaves? and How table sorting works?
