"""Film Model Module
This module provides the Film class, which represents
a film and extends the Video class."""
from decorators.decorators import logged  # pylint: disable=import-error
from exceptions.invalid_rating_exception import InvalidRatingException  # pylint: disable=import-error
from models.video import Video  # pylint: disable=import-error


class Film(Video):
    """Film Class
       This class represents a film and extends the Video class.
       Attributes:
           title (str): The title of the film.
           director (str): The director of the film.
           year (int): The year when the film was released.
           rating (float): The overall rating of the film.
           marks (int): The number of ratings given to the film."""

    video_target_audience = {"children", "teenagers", "middle-aged", "older people"}

    def __init__(  # pylint: disable=too-many-arguments
            self, title="", director="", year=0, rating=0, marks=0):
        """Initialize a new Film instance with the given title, director, year, rating, and marks.
            Args:
                title (str): The title of the film. Default is an empty string.
                director (str): The director of the film. Default is an empty string.
                year (int): The year when the film was created. Default is 0.
                rating (int): The rating of the film. Default is 0.
                marks (int): The number of marks received by the film. Default is 0."""
        super().__init__(title, director, year)
        self.rating = rating
        self.marks = marks

    def __str__(self):
        """Return a string representation of the Film.
            Returns:
                str: A string representation of the Film instance."""
        return f"Film({self.title}, {self.director}, {self.year}, {self.rating}, {self.marks})"

    def __repr__(self):
        """Return a string representation of the Film for debugging purposes.
            Returns:
                str: A string representation of the Film instance."""
        return f"Film({self.title}, {self.director}, {self.year}, {self.rating}, {self.marks})"

    @logged(InvalidRatingException, "file")
    def rate(self, rating):
        """Rate the film and update the overall rating.
           Args:
           rating (float): The rating given to the film.
           Note:
           The rating is constrained between 1 and 10."""

        if rating > 10 or rating < 1:
            raise InvalidRatingException
        self.rating += rating
        self.marks += 1

    def get_current_rating(self):
        """Calculate and return the current rating of the film.
           Returns:
           float: The current rating of the film."""

        return self.rating / self.marks
