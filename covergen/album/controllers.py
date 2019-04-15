"""Controllers for the album functionality."""

from flask import Blueprint, render_template

from .models import Album


album = Blueprint('album', __name__, url_prefix='/album')


@album.route('/random')
def show_random_album() -> str:
    """Show a random album cover."""
    album = Album('Chronicles', 'Rush')

    return render_template('base.html', album=album)
