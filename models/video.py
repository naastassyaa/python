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
    video_target_audience = set()

    def __iter__(self):
        """Return an iterator object that can iterate over the video's target audience.
                Returns:
                    iterator: An iterator object for the video's target audience."""
        return iter(self.video_target_audience)

    def get_attributes_by_type(self, data_type):
        """Get a dictionary of attributes from the video by the specified data type.
                Args:
                    data_type (type): The data type to filter the attributes.
                Returns:
                    dict: A dictionary containing the attribute names
                    and values of the specified data type."""
        return {key: value for key, value in self.__dict__.items() if isinstance(value, data_type)}

    def __init__(self, title="", director="", year=0):
        """Initialize a new Video instance with the given title, director, and year.
                Args:
                    title (str): The title of the video. Default is an empty string.
                    director (str): The director of the video. Default is an empty string.
                    year (int): The year when the video was created. Default is 0."""
        self.title = title
        self.director = director
        self.year = year

    @abstractmethod
    def get_current_rating(self):
        """Abstract method to get the current rating of the video.
           This method needs to be implemented by subclasses."""
