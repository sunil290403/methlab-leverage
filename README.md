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
   bash
   Copy code
   git clone <repository-url>
   cd methlab-qa-assessment

2. Install Dependencies
   Create a virtual environment and install the required packages:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt


UI Automation with Selenium
Configuration
Update the config.py file with:

URL of the application
Browser driver paths
Running Tests
To run the Selenium UI tests, use:

bash
Copy code
pytest tests/test.py

Performance Testing with Locust
Configuration
Update the locustfile.py with:

Endpoints for wallet interactions
Load parameters for performance testing
Running Locust
To start performance testing, run:

bash
Copy code
locust -f locustfile.py
Access http://localhost:8089 in your browser to start and monitor the tests.

Performance Scenarios
Scenario 1: Measure performance of leverage page under load

Troubleshooting
Dependencies : Ensure all the dependencies are installed.
Driver Compatibility: Ensure that the browser driver version matches the browser version.