1. clone the project
2. install the dependencies - pip install -r .\requirements.txt
3. run the project using the commands
       1. sanity testcases -> pytest -m sanity --html=sanity_report.html (python -m pytest -m sanity --html=sanity_report.html - in case local system fails to find the root)
       2. funcational testcases->  pytest -m funcational --html=funcational_report.html
       3. regression testcases -> pytest -m regression --html=regression_report.htm

