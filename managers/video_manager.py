"""Video Manager Module
This module provides a VideoManager class
that manages a list of videos."""


class VideoManager:
    """Video Manager Class
        This class represents a video manager that allows adding videos, finding videos
        based on certain criteria, and printing the added videos.
        Attributes:
            videos (list): A list of videos managed by the video manager."""
    def __init__(self):
        self.videos = []

    def add_video(self, video):
        """Add a video to the list of videos.
           Args:
           video: An instance of a video object to be added."""
        self.videos.append(video)

    def find_all_with_year_more_than(self, year):
        """Find all videos with a year greater than the specified year.
           Args:
           year: An integer representing the year.
           Returns:
           A list of videos with a year greater than the specified year."""
        return [video for video in self.videos if video.year > year]

    def find_all_with_same_director(self, director):
        """Find all videos with the same director.
           Args:
           director: A string representing the director's name.
           Returns:
           A list of videos with the same director."""
        return [video for video in self.videos if video.director == director]
