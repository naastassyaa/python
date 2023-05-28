"""Video Manager Module
This module provides a VideoManager class
that manages a list of videos."""

from decorators.decorators import history, validate_snake_case  # pylint: disable=import-error


class VideoManager:
    """Video Manager Class
        This class represents a video manager that allows adding videos, finding videos
        based on certain criteria, and printing the added videos.
        Attributes:
        videos (list): A list of videos managed by the video manager."""

    def __init__(self):
        """Initialize a new instance of the VideoManager class.
            This method sets up an empty list to store the videos managed by the video manager."""
        self.videos = []

    @history
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

    @validate_snake_case
    def find_all_with_same_director(self, director):
        """Find all videos with the same director.
           Args:
           director: A string representing the director's name.
           Returns:
           A list of videos with the same director."""

        return [video for video in self.videos if video.director == director]

    def result_of_rating_method(self):
        """Calculate and return the current rating for each video in the video manager.
            Returns:
                list: A list of the current ratings for each video in the video manager."""
        return [video.get_current_rating() for video in self.videos]

    def all_more_than_year(self, year):
        """Check if all or any of the videos in the video manager have a
        year greater than the specified year.
           Args:
               year (int): An integer representing the year to compare against.
           Returns:
               dict: A dictionary with two boolean values indicating if all or any videos
               have a year greater than the specified year.
                   - "any": True if any video has a year greater than
                   the specified year, False otherwise.
                   - "all": True if all videos have a year greater than
                   the specified year, False otherwise."""
        all_any = {"any": any(video.year > year for video in self.videos),
                   "all": all(video.year > year for video in self.videos)}
        return all_any

    def __len__(self):
        """Return the number of videos in the video manager."""

        return len(self.videos)

    def __getitem__(self, index):
        """Get a video from the video manager based on the index.
        Args:
            index: An integer representing the index of the video to retrieve.
        Returns:
            The video at the specified index."""

        return self.videos[index]

    def __iter__(self):
        """Return an iterator object that can iterate over the videos in the video manager."""

        return iter(self.videos)
