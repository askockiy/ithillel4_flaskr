from flask import Blueprint, render_template
from flaskr.db import get_db

bp = Blueprint('tracks', __name__, url_prefix="/tracks")

@bp.route('/')
def index():
    tracks = get_db().execute(
        'SELECT COUNT(id) FROM tracks'
    ).fetchone()[0]
    return render_template('tracks.html', tracks=tracks)

@bp.route('/<genre>')
def tgenre(genre):
    count = get_db().execute(
        'SELECT COUNT(*) FROM tracks WHERE genre = ?', (genre,)
    ).fetchone()[0]
    return render_template('tracks.html', genre=genre, count=count )