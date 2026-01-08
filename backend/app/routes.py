from flask import Blueprint, render_template, request, redirect, url_for
from sqlalchemy import or_

from app import db
from app.models import Movie

bp = Blueprint("main", __name__)

# ----------------------------
# Главная страница + поиск
# ----------------------------
@bp.get("/")
def index():
    q = (request.args.get("q") or "").strip()

    query = Movie.query
    if q:
        like = f"%{q}%"
        query = query.filter(or_(
            Movie.title.ilike(like),
            Movie.genre.ilike(like),
            Movie.description.ilike(like),
        ))

    movies = query.order_by(Movie.title.asc()).all()
    return render_template("index.html", movies=movies, q=q)


# ----------------------------
# Страница одного фильма
# ----------------------------
@bp.get("/movies/<int:movie_id>")
def movie_detail(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    return render_template("movie_detail.html", movie=movie)


# ----------------------------
# Избранное
# ----------------------------
@bp.get("/favorites")
def favorites():
    movies = Movie.query.filter_by(is_favorite=True).order_by(Movie.title.asc()).all()
    return render_template("favorites.html", movies=movies)


# ----------------------------
# Добавить / убрать из избранного
# ----------------------------
@bp.post("/movies/<int:movie_id>/favorite")
def toggle_favorite(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    movie.is_favorite = not movie.is_favorite
    db.session.commit()
    return redirect(request.referrer or url_for("main.index"))
