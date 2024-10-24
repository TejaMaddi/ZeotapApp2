from datetime import datetime
from database import WeatherSummary, db

def process_weather_data(data):
    temp = data['main']['temp']
    feels_like = data['main']['feels_like']
    condition = data['weather'][0]['main']
    timestamp = data['dt']
    date = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')

    summary = WeatherSummary.query.filter_by(date=date).first()

    if summary:
        summary.avg_temp = (summary.avg_temp + temp) / 2
        summary.max_temp = max(summary.max_temp, temp)
        summary.min_temp = min(summary.min_temp, temp)
    else:
        summary = WeatherSummary(
            date=date,
            avg_temp=temp,
            max_temp=temp,
            min_temp=temp,
            dominant_condition=condition
        )

    db.session.add(summary)
    db.session.commit()
