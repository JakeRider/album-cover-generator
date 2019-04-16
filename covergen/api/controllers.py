"""Controllers for the RESTful API."""

from flask import Blueprint, jsonify

from ..album.helpers import generate_random_album


api = Blueprint('api', __name__, url_prefix='/api/v1')


@api.route('/album/generate-random')
def generate_random_album_json() -> str:
    """Generate a JSON for a random album cover."""
    album = generate_random_album()
    json = {
        'title': album.title,
        'artist': album.artist,
    }

    return jsonify(json)
