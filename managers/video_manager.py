"""Video Manager Module
This module provides a VideoManager class
that manages a list of videos."""
from models.cartoon import Cartoon  # pylint: disable=import-error
from models.clip import Clip  # pylint: disable=import-error
from models.film import Film  # pylint: disable=import-error
from models.tik_tok import TikTok  # pylint: disable=import-error


class VideoManager:
    """Video Manager Class
        This class represents a video manager that allows adding videos, finding videos
        based on certain criteria, and printing the added videos.
        Attributes:
            videos (list): A list of videos managed by the video manager."""
    videos = []

    @classmethod
    def add_video(cls, video):
        """Add a video to the list of videos.
           Args:
           video: An instance of a video object to be added."""
        cls.videos.append(video)

    @classmethod
    def main(cls):
        """The main method that adds videos to the video manager,
        prints the added videos,
        finds videos with a year greater than a specified year,
        and finds videos with the same director."""
        cls.add_video(Film("Титанік", "Джеймс Кемерон", 1997, 123, 16))
        cls.add_video(Film("До зустрічі з тобою", "Теа Шеррок", 2016, 166, 20))
        cls.add_video(
            Clip("The Hills of Aberfeldy", "Mia Barnes", 2023, "The Hills of Aberfeldy",
                 "Ed Sheeran", 36000, 2500000))
        cls.add_video(Clip("NF - HAPPY", "Mia Barnes", 2023, "Happy", "NF", 305000, 12000000))
        cls.add_video(TikTok("Cooking", "SashaBo", 2022, "Mockingbird", 123, 506, 1098))
        cls.add_video(TikTok("My Style", "SashaBo", 2023, "Mockingbird",
                             129, 409, 8048))
        cls.add_video(Cartoon("Мавка. Лісова пісня", "Олександра Рубан",
                              2023, "Фентезі", 12, 145, 15))
        cls.add_video(Cartoon("Зоотрополіс", "Байрон Говард", 2016, "Комедія", 17, 178, 20))

        print("Всі додані відео:")
        for i in cls.videos:
            print(i)

        print("Відео з роком більшим ніж заданий:")
        print(*cls.find_all_with_year_more_than(2022), sep="\n")

        print("Відео з однаковим режисером:")
        print(*cls.find_all_with_same_director("SashaBo"), sep="\n")

    @classmethod
    def find_all_with_year_more_than(cls, year):
        """Find all videos with a year greater than the specified year.
           Args:
           year: An integer representing the year.
           Returns:
           A list of videos with a year greater than the specified year."""
        return [video for video in cls.videos if video.year > year]

    @classmethod
    def find_all_with_same_director(cls, director):
        """Find all videos with the same director.
           Args:
           director: A string representing the director's name.
           Returns:
           A list of videos with the same director."""
        return [video for video in cls.videos if video.director == director]


VideoManager.main()
