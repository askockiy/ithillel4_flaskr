from flask import Blueprint, render_template
from flaskr.db import get_db

bp = Blueprint('track-sec', __name__, url_prefix="/track-sec")

@bp.route('/')
def index():
    track_sec = get_db().execute(
        'SELECT title, length FROM tracks'
    ).fetchall()
    return render_template('track_sec.html', track_sec=track_sec)

@bp.route('/statistics/')
def statistics():
    total_length = get_db().execute('SELECT SUM(length) FROM tracks').fetchone()[0]
    count = get_db().execute('SELECT COUNT(*) FROM tracks').fetchone()[0]
    if count > 0:
        average_length = total_length / count
    else:
        average_length = 0
    return render_template('track_sec_statistics.html', average_length=average_length, total_length=total_length)