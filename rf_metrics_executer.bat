:: Execute python file to generate html report
rem Please be patient metric converstion is in-process...
python rf_metrics_report_creator.py & 

:: Open chrome with result
start chrome "rf_metrics_result.html"