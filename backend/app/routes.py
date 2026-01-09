"""
HTTP-маршруты приложения (Flask Blueprint).
"""

from flask import Blueprint, render_template, request, redirect, url_for
from sqlalchemy import or_

from app import db
from app.models import Movie

bp = Blueprint("main", __name__)


@bp.get("/")
def index():
    """
    Главная страница каталога + поиск.
    """
    search_text = (request.args.get("q") or "").strip()

    movies_query = Movie.query

    if search_text:
        like_pattern = f"%{search_text}%"
        movies_query = movies_query.filter(
            or_(
                Movie.title.ilike(like_pattern),
                Movie.genre.ilike(like_pattern),
                Movie.description.ilike(like_pattern),
            )
        )

    movies = movies_query.order_by(Movie.title.asc()).all()
    return render_template("index.html", movies=movies, q=search_text)


@bp.get("/movies/<int:movie_id>")
def movie_detail(movie_id: int):
    """Страница одного фильма."""
    movie = Movie.query.get_or_404(movie_id)
    return render_template("movie_detail.html", movie=movie)


@bp.get("/favorites")
def favorites():
    """Страница избранного."""
    favorite_movies = (
        Movie.query.filter_by(is_favorite=True)
        .order_by(Movie.title.asc())
        .all()
    )
    return render_template("favorites.html", movies=favorite_movies)


@bp.post("/movies/<int:movie_id>/favorite")
def toggle_favorite(movie_id: int):
    """
    Переключает статус избранного у фильма и возвращает пользователя назад.
    """
    movie = Movie.query.get_or_404(movie_id)
    movie.is_favorite = not movie.is_favorite
    db.session.commit()

    return redirect(request.referrer or url_for("main.index"))
