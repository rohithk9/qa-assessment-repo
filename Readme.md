[![Build Status](https://app.travis-ci.com/rohithk9/qa-assessment-repo.svg?branch=master)](https://app.travis-ci.com/rohithk9/qa-assessment-repo)

# This Project is based on an assessment done for a Firmware QA Engineer position at a Company

# Project Tree
```.
.
├── Readme.md
├── __init__.py
├── battery_life_estimator.py
├── battery_life_estimator_results.log
├── conftest.py
├── data
│   └── sampleData.csv
├── pytest-report.xml
├── pytest.ini
├── requirements.txt
├── test_battery_life_estimator.log
└── test_battery_life_estimator.py
```
# Description
The assessment consists of a dataset of UTC timestamps and current in amperes drawn by a battery powered device at these timestamps.
The assessment asks to write a python script to calculate maximum and minimum currents draw by the device, total energy consumption and expected lifetime of the battery.

Note: The expected lifetime of the battery was calculated assuming that the battery capacity is 1000 mAh.

The project consists of the main script that calculated these parameters in battery_life_estimator.py.
test_battery_life_estimator.py consists of test cases used to test the main script.

Calculated parameters are written to battery_life_estimator_results.log file.
Test results are written to the battery_life_estimator.log file.

# Development Environmemt

The development was done using Sublime text as the text editor and built using Python 3.11.4

Testing is done using the pytest framework from Python.

# Requirements
Run the following commands before running the script:
pip install -r requirements.txt

To run the script:
python battery_life_estimator.py

To run the tests:
pytest
