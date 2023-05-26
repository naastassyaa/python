"""Video Model Module
This module provides the Video class, which is an abstract base class for representing videos."""
from abc import ABC, abstractmethod  # pylint: disable=import-error


class Video(ABC):
    """Video Class
        This abstract base class represents a video.
        Attributes:
            title (str): The title of the video.
            director (str): The director of the video.
            year (int): The year when the video was created."""

    # pylint: disable=too-few-public-methods
    def __init__(self, title="", director="", year=0):
        self.title = title
        self.director = director
        self.year = year

    @abstractmethod
    def get_current_rating(self):
        """Abstract method to get the current rating of the video.
           This method needs to be implemented by subclasses."""
