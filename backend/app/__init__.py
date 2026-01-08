from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # SQLite база (файл появится в корне проекта)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    # подключаем роуты
    from app.routes import bp
    app.register_blueprint(bp)

    # создаём таблицы при первом запуске
    with app.app_context():
        from app.models import Movie
        db.create_all()

    return app
