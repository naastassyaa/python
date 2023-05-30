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

    video_target_audience = {"teenagers", "middle-aged"}

    def __init__(  # pylint: disable=too-many-arguments
            self, title="", director="", year=0, name_of_song="", likes=0, views=0, comments=0):
        """Initialize a new TikTok instance with the given title, director, year,
        name of the song, likes, views, and comments.
            Args:
                title (str): The title of the TikTok. Default is an empty string.
                director (str): The director of the TikTok. Default is an empty string.
                year (int): The year when the TikTok was created. Default is 0.
                name_of_song (str): The name of the song used in the TikTok.
                Default is an empty string.
                likes (int): The number of likes received by the TikTok. Default is 0.
                views (int): The number of views received by the TikTok. Default is 0.
                comments (int): The number of comments received by the TikTok. Default is 0."""
        super().__init__(title, director, year)
        self.name_of_song = name_of_song
        self.likes = likes
        self.views = views
        self.comments = comments

    def __str__(self):
        """Return a string representation of the TikTok.
            Returns:
                str: A string representation of the TikTok instance."""
        return f"TikTok({self.title}, {self.director}, {self.year}, {self.name_of_song}, " \
               f"{self.likes}, {self.views}, {self.comments})"

    def __repr__(self):
        """Return a string representation of the TikTok for debugging purposes.
            Returns:
                str: A string representation of the TikTok instance."""
        return f"TikTok({self.title}, {self.director}, {self.year}, {self.name_of_song}, " \
               f"{self.likes}, {self.views}, {self.comments})"

    def get_current_rating(self):
        """Calculate and return the current rating of the TikTok video.
           Returns:
           float: The current rating of the TikTok video."""
        return (self.likes + self.comments) / self.views
