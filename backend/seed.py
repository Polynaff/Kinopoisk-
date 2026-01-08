from app import create_app, db
from app.models import Movie

MOVIES = [
    {
        "title": "Начало",
        "year": 2010,
        "genre": "Sci-Fi",
        "description": "Сны внутри снов.",
        "poster": "inception.jpg",
        "watch_url":"https://www.kinopoisk.ru/film/447301/"
    },
    {
        "title": "Интерстеллар",
        "year": 2014,
        "genre": "Sci-Fi",
        "description": "Полет сквозь червоточину.",
        "poster": "interstellar.jpg",
        "watch_url": "https://www.kinopoisk.ru/film/258687/"
    },
    {
        "title": "Побег из Шоушенка",
        "year": 1994,
        "genre": "Drama",
        "description": "Надежда сильнее стен.",
        "poster": "shawshank.jpg",
        "watch_url": "https://www.kinopoisk.ru/film/326/"
    },
    {
        "title": "Во все тяжкие",
        "year": 2008,
        "genre": "Crime",
        "description": "Учитель химии меняет жизнь.",
        "poster": "breaking_bad.jpg",
        "watch_url": "https://www.kinopoisk.ru/series/404900/?utm_referrer=www.google.com"
    },
    {
        "title": "Mopsolend",
        "year": 2025,
        "genre": "Sci-Fi",
        "description": "Мопсики.",
        "poster": "mops.jpg",
        "watch_url": "https://www.youtube.com/watch?v=OmX1V6_gukY"
    },
]

app = create_app()

with app.app_context():
    for m in MOVIES:
        exists = Movie.query.filter_by(title=m["title"], year=m["year"]).first()
        if not exists:
            db.session.add(Movie(**m))
    db.session.commit()
    print("Seed done")
