from app import db


class Movie(db.Model):
    __tablename__ = "movies"

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(200), nullable=False)
    year = db.Column(db.Integer, nullable=True)
    genre = db.Column(db.String(100), nullable=True)
    description = db.Column(db.Text, nullable=True)

    poster = db.Column(db.String(255), nullable=True)     # имя файла из static/img
    watch_url = db.Column(db.String(500), nullable=True)  # ссылка где смотреть

    is_favorite = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<Movie {self.title}>"
