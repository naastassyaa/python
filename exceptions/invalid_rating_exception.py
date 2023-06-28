"""
This module defines custom exception classes related to ratings.
"""


class InvalidRatingException(Exception):
    """Exception raised when an invalid rating is encountered.
        Attributes:
            message (str): The error message describing the invalid rating."""
    message = "Rating should be from 1 to 10!"

    def __init__(self):
        super().__init__(self.message)
