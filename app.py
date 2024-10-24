from flask import Flask, render_template
from database import init_db
from api_client import fetch_weather_data, CITIES
from data_processor import process_weather_data

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

init_db(app)

@app.route('/')
def index():
    weather_data = []
    for city in CITIES:
        data = fetch_weather_data(city)
        if data.get('main'):
            process_weather_data(data)
            weather_data.append(data)

    return render_template('index.html', weather_data=weather_data)

if __name__ == "__main__":
    app.run(debug=True)
