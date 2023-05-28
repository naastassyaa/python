"""Cartoon Model Module
This module provides the Cartoon class, which represents
a cartoon and extends the Video class."""
from models.video import Video  # pylint: disable=import-error


class Cartoon(Video):
    """Cartoon Class
        This class represents a cartoon and extends the Video class.
        Attributes:
            title (str): The title of the cartoon.
            director (str): The director of the cartoon.
            year (int): The year when the cartoon was released.
            genre (str): The genre of the cartoon.
            number_of_characters (int): The number of characters in the cartoon.
            rating (float): The overall rating of the cartoon.
            marks (int): The number of ratings given to the cartoon."""
    video_target_audience = {"children", "teenagers"}

    def __init__(  # pylint: disable=too-many-arguments
            self, title="", director="", year=0, genre="", number_of_characters=0,
            rating=0, marks=0):
        """Initialize a new Cartoon instance with the given title, director,
           year, genre, number of characters,rating, and marks.
            Args:
                title (str): The title of the Cartoon. Default is an empty string.
                director (str): The director of the Cartoon. Default is an empty string.
                year (int): The year when the Cartoon was created. Default is 0.
                genre (str): The genre of the Cartoon. Default is an empty string.
                number_of_characters (int): The number of characters in the Cartoon. Default is 0.
                rating (int): The rating of the Cartoon. Default is 0.
                marks (int): The number of marks received by the Cartoon. Default is 0."""
        super().__init__(title, director, year)
        self.genre = genre
        self.number_of_characters = number_of_characters
        self.rating = rating
        self.marks = marks

    def __str__(self):
        """Return a string representation of the Cartoon.
            Returns:
                str: A string representation of the Cartoon instance."""
        return f"Cartoon({self.title}, {self.director}, {self.year}, {self.genre}, " \
               f"{self.number_of_characters}, {self.rating}, {self.marks})"

    def __repr__(self):
        """Return a string representation of the Cartoon for debugging purposes.
            Returns:
                str: A string representation of the Cartoon instance."""
        return f"Cartoon({self.title}, {self.director}, {self.year}, {self.genre}, " \
               f"{self.number_of_characters}, {self.rating}, {self.marks})"

    def get_current_rating(self):
        """Calculate and return the current rating of the cartoon.
           Returns:
           float: The current rating of the cartoon."""
        return self.rating / self.marks
