from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class WeatherSummary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(10), unique=True)
    avg_temp = db.Column(db.Float)
    max_temp = db.Column(db.Float)
    min_temp = db.Column(db.Float)
    dominant_condition = db.Column(db.String(50))

def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()
