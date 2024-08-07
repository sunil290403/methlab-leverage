Methlab QA Assessment

Overview

This README provides instructions for the Methlab QA assessment. The task involves automating the testcases for leverage feature. The assessment includes UI automation using Selenium and performance testing with Locust.

Prerequisites
Ensure you have the following tools and dependencies installed:

* Python 3.7 or higher
* Selenium
* Locust
* Browser driver (e.g., ChromeDriver for Google Chrome)

Setup
1. Clone the Repository
```bash
   git clone <repository-url>
   cd methlab-leverage
```
2. Install Dependencies
   Create a virtual environment and install the required packages:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install <package-name>
```

To run the Selenium UI tests, use:

```bash
pytest --html=reports/test_report.html tests/test.py
```
Access the test_report from the reports folder to analyse

Performance Testing with Locust

To start performance testing, run:

```bash
locust -f locust/methlab_leverage.py
```
Access http://localhost:8089 in your browser to start and monitor the tests.

Performance Scenarios

Scenario : Measure performance of leverage page under load

Troubleshooting

Dependencies : Ensure all the dependencies are installed.
Driver Compatibility: Ensure that the browser driver version matches the browser version.