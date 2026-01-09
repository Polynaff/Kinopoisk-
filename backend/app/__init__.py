from flask import Flask
from flask_sqlalchemy import SQLAlchemy

"""
Инициализация приложения (Application Factory).
Здесь создаётся Flask app и подключаются расширения/роуты.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Расширение SQLAlchemy создаём глобально, привязываем позже в create_app()
db = SQLAlchemy()


def create_app() -> Flask:
    """
    Фабрика приложения.
    Возвращает готовый экземпляр Flask с подключённой БД и роутами.
    """
    flask_app = Flask(__name__)

    # SQLite база
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(flask_app)

    # Подключаем blueprint с маршрутами
    from app.routes import bp as main_blueprint
    flask_app.register_blueprint(main_blueprint)

    # Создаём таблицы при первом запуске
    with flask_app.app_context():
        from app.models import Movie  # noqa: F401 (нужно для регистрации модели)
        db.create_all()

    return flask_app
