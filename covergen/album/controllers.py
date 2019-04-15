"""Controllers for the album functionality."""

from flask import Blueprint, render_template

from .helpers import generate_random_album


album = Blueprint('album', __name__, url_prefix='/album')


@album.route('/random')
def show_random_album() -> str:
    """Show a random album cover."""
    album = generate_random_album()

    return render_template('base.html', album=album)
