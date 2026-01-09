"""
Заполнение базы начальными данными.

Запуск:
    python seed.py

Скрипт добавляет фильмы в БД, если их там ещё нет.
"""

from app import create_app, db
from app.models import Movie

SEED_MOVIES = [
    {
        "title": "Начало",
        "year": 2010,
        "genre": "Sci-Fi",
        "description": "Сны внутри снов.",
        "poster": "inception.jpg",
        "watch_url": "https://www.kinopoisk.ru/film/447301/",
    },
    {
        "title": "Интерстеллар",
        "year": 2014,
        "genre": "Sci-Fi",
        "description": "Полет сквозь червоточину.",
        "poster": "interstellar.jpg",
        "watch_url": "https://www.kinopoisk.ru/film/258687/",
    },
    {
        "title": "Побег из Шоушенка",
        "year": 1994,
        "genre": "Drama",
        "description": "Надежда сильнее стен.",
        "poster": "shawshank.jpg",
        "watch_url": "https://www.kinopoisk.ru/film/326/",
    },
    {
        "title": "Во все тяжкие",
        "year": 2008,
        "genre": "Crime",
        "description": "Учитель химии меняет жизнь.",
        "poster": "breaking_bad.jpg",
        "watch_url": "https://www.kinopoisk.ru/series/404900/?utm_referrer=www.google.com",
    },
    {
        "title": "Mopsolend",
        "year": 2025,
        "genre": "Sci-Fi",
        "description": "Мопсики.",
        "poster": "mops.jpg",
        "watch_url": "https://www.youtube.com/watch?v=OmX1V6_gukY",
    },
]


def seed_database() -> None:
    """Добавляет фильмы из SEED_MOVIES в базу данных."""
    flask_app = create_app()

    with flask_app.app_context():
        added_count = 0

        for movie_data in SEED_MOVIES:
            existing_movie = Movie.query.filter_by(
                title=movie_data["title"],
                year=movie_data["year"],
            ).first()

            if existing_movie is None:
                db.session.add(Movie(**movie_data))
                added_count += 1

        db.session.commit()
        print(f"Seed done. Added: {added_count}")


if __name__ == "__main__":
    seed_database()
