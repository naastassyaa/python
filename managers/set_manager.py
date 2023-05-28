"""
SetManager Module
This module provides a SetManager class that allows iteration
and indexing over videos in a video manager.
Module Contents:
- SetManager: A class that provides iteration and indexing
functionality over videos in a video manager.
"""


class SetManager:
    """SetManager Class
        This class represents a set manager that provides iteration and indexing functionality
        over the videos in the video manager.
        Attributes:
            video_manager (VideoManager): An instance of the
            VideoManager class containing the videos."""

    def __init__(self, video_manager):
        """Initialize the SetManager instance with a VideoManager object.
            Args:
              video_manager (VideoManager): An instance of the
              VideoManager class containing the videos."""
        self.video_manager = video_manager

    def __iter__(self):
        """Return an iterator object that can iterate over the videos in the video manager.
        Yields:
            Video: The next video in the video manager."""
        for i in self.video_manager:
            for j in i:
                yield j

    def __len__(self):
        """Return the number of videos in the SetManager.
            Returns:
             int: The number of videos in the SetManager."""
        return len(list(iter(self)))

    def __getitem__(self, index):
        """Get a video from the video manager based on the index.
        Args:
            index: An integer representing the index of the video to retrieve.
        Returns:
            The video at the specified index."""

        return list(iter(self))[index]
