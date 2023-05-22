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
    def __init__(  # pylint: disable=too-many-arguments
            self, title="", director="", year=0, genre="", number_of_characters=0,
            rating=0, marks=0):
        super().__init__(title, director, year)
        self.genre = genre
        self.number_of_characters = number_of_characters
        self.rating = rating
        self.marks = marks

    def __str__(self):
        return f"Cartoon({self.title}, {self.director}, {self.year}, {self.genre}, " \
               f"{self.number_of_characters}, {self.rating}, {self.marks})"

    def get_current_rating(self):
        """Calculate and return the current rating of the cartoon.
           Returns:
           float: The current rating of the cartoon."""
        return self.rating / self.marks
