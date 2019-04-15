"""The main entry point of the application."""

from dataclasses import dataclass

from flask import Flask, render_template


@dataclass
class Album:
    """A dataclass representing an album."""

    title: str
    artist: str


def create_app() -> Flask:
    """Create an instance of the covergen app."""
    app = Flask(__name__)

    @app.route('/')
    def home() -> str:
        album = Album('Chronicles', 'Rush')

        return render_template('base.html', album=album)

    return app
