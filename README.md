Weather Monitoring System
Overview
The Weather Monitoring System is a real-time application designed to fetch and process weather data for various cities in India using the OpenWeatherMap API. It provides users with summarized insights, including daily temperature averages, maximum and minimum temperatures, and dominant weather conditions. The system also includes an alerting mechanism to notify users when specific weather thresholds are exceeded.

Features
Real-time Data Fetching: Continuously retrieves weather data from the OpenWeatherMap API at configurable intervals.
Data Processing: Aggregates daily weather statistics, including average, maximum, and minimum temperatures, along with the dominant weather condition.
Alerting System: User-configurable thresholds for temperature and weather conditions with alert notifications.
Data Visualization: A web dashboard that displays current weather conditions and daily summaries.
Technologies Used
Python
Flask
SQLAlchemy
SQLite
OpenWeatherMap API
Getting Started
Prerequisites
Python 3.x
pip (Python package installer)
Installation
Clone the repository:


git clone <repository_url>
cd weather_monitoring_system
Set up a virtual environment (optional but recommended):


python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the required packages:
pip install -r requirements.txt
Set your OpenWeatherMap API key in api_client.py.

Running the Application
To start the application, run:
python app.py
Open your browser and navigate to http://127.0.0.1:5000 to view the dashboard.

Testing
To run tests, you can create a separate test file using a testing framework like unittest or pytest.

License
This project is licensed under the MIT License.
