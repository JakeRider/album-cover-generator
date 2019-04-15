"""The main entry point of the application."""

from flask import Flask, render_template


def create_app() -> Flask:
    """Create an instance of the covergen app."""
    app = Flask(__name__)

    @app.route('/')
    def say_hello() -> str:
        return render_template('base.html')

    return app
