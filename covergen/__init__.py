"""The main entry point of the application."""

from flask import Flask, redirect

from .album.controllers import album


def create_app() -> Flask:
    """Create an instance of the covergen app."""
    app = Flask(__name__)

    app.register_blueprint(album)

    @app.route('/')
    def index():
        """Redirect to the random album view."""
        return redirect('/album/random', 301)

    return app
