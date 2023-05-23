"""Clip Model Module
This module provides the Clip class, which represents a video clip and extends the Video class."""
from models.video import Video  # pylint: disable=import-error


class Clip(Video):
    """Clip Class
        This class represents a video clip and extends the Video class.
        Attributes:
            title (str): The title of the clip.
            director (str): The director of the clip.
            year (int): The year when the clip was released.
            name_of_song (str): The name of the song featured in the clip.
            singer (str): The singer of the song featured in the clip.
            likes (int): The number of likes the clip has received.
            views (int): The number of views the clip has received."""

    def __init__(  # pylint: disable=too-many-arguments
            self, title="", director="", year=0, name_of_song="", singer="", likes=0, views=0):
        super().__init__(title, director, year)
        self.name_of_song = name_of_song
        self.singer = singer
        self.likes = likes
        self.views = views

    def __str__(self):
        return f"Clip({self.title}, {self.director}, {self.year}, {self.name_of_song}, " \
               f"{self.singer}, {self.likes}, {self.views})"

    def get_current_rating(self):
        """Calculate and return the current rating of the clip.
           Returns:
           float: The current rating of the clip."""
        return self.likes / self.views
