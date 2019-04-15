"""Helpers for the album functionality."""

from random import choice

from .models import Album
from .wordlists import animals, colors, cottons, weathers


def generate_random_album() -> Album:
    """Generate a random album."""
    title = f'{choice(weathers)} {choice(cottons)}'.title()
    artist = f'by {choice(colors)} {choice(animals)}'.title()

    return Album(title, artist)
