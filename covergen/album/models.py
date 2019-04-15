"""Data models for the album functionality."""

from dataclasses import dataclass


@dataclass
class Album:
    """A dataclass representing an album."""

    title: str
    artist: str
