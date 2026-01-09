"""
Модели базы данных (SQLAlchemy).
"""

from app import db


class Movie(db.Model):
    """Фильм/сериал в каталоге."""

    __tablename__ = "movies"

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(200), nullable=False)
    year = db.Column(db.Integer, nullable=True)
    genre = db.Column(db.String(100), nullable=True)
    description = db.Column(db.Text, nullable=True)

    # имя файла картинки из static/img
    poster = db.Column(db.String(255), nullable=True)

    # ссылка "где смотреть"
    watch_url = db.Column(db.String(500), nullable=True)

    # признак "в избранном"
    is_favorite = db.Column(db.Boolean, default=False)

    def __repr__(self) -> str:
        return f"<Movie id={self.id} title={self.title!r}>"
