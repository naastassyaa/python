"""TikTok Model Module
This module provides the TikTok class, which
represents a TikTok video and extends the Video class."""
from models.video import Video  # pylint: disable=import-error


class TikTok(Video):
    """TikTok Class
        This class represents a TikTok video and extends the Video class.
        Attributes:
            title (str): The title of the TikTok video.
            director (str): The director of the TikTok video.
            year (int): The year when the TikTok video was created.
            name_of_song (str): The name of the song featured in the TikTok video.
            likes (int): The number of likes the TikTok video has received.
            views (int): The number of views the TikTok video has received.
            comments (int): The number of comments the TikTok video has received."""

    def __init__(  # pylint: disable=too-many-arguments
            self, title="", director="", year=0, name_of_song="", likes=0, views=0, comments=0):
        super().__init__(title, director, year)
        self.name_of_song = name_of_song
        self.likes = likes
        self.views = views
        self.comments = comments

    def __str__(self):
        return f"TikTok({self.title}, {self.director}, {self.year}, {self.name_of_song}, " \
               f"{self.likes}, {self.views}, {self.comments})"

    def get_current_rating(self):
        """Calculate and return the current rating of the TikTok video.
           Returns:
           float: The current rating of the TikTok video."""
        return (self.likes + self.comments) / self.views
