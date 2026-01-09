"""
Точка входа в приложение.
Запуск: python run.py
"""

from app import create_app

# Создаём Flask-приложение через фабрику
flask_app = create_app()

if __name__ == "__main__":
    flask_app.run(debug=True)
