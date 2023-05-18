from abc import ABC, abstractmethod


class Video(ABC):

    def __init__(self, title="", director="", year=0):
        self.title = title
        self.director = director
        self.year = year

    @abstractmethod
    def get_current_rating(self):
        pass
