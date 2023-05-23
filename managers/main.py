"""
main module
"""
from managers.video_manager import VideoManager  # pylint: disable=import-error
from models.cartoon import Cartoon  # pylint: disable=import-error
from models.clip import Clip  # pylint: disable=import-error
from models.film import Film  # pylint: disable=import-error
from models.tik_tok import TikTok  # pylint: disable=import-error

if __name__ == '__main__':
    list_videos = VideoManager()
    list_videos.add_video(Film("Титанік", "Джеймс Кемерон", 1997, 123, 16))
    list_videos.add_video(Film("До зустрічі з тобою", "Теа Шеррок", 2016, 166, 20))
    list_videos.add_video(
        Clip("The Hills of Aberfeldy", "Mia Barnes", 2023, "The Hills of Aberfeldy",
             "Ed Sheeran", 36000, 2500000))
    list_videos.add_video(Clip("NF - HAPPY", "Mia Barnes", 2023, "Happy", "NF", 305000, 12000000))
    list_videos.add_video(TikTok("Cooking", "SashaBo", 2022, "Mockingbird", 123, 506, 1098))
    list_videos.add_video(TikTok("My Style", "SashaBo", 2023, "Mockingbird",
                                 129, 409, 8048))
    list_videos.add_video(Cartoon("Мавка. Лісова пісня", "Олександра Рубан",
                                  2023, "Фентезі", 12, 145, 15))
    list_videos.add_video(Cartoon("Зоотрополіс", "Байрон Говард", 2016, "Комедія", 17, 178, 20))

    print("Всі додані відео:")
    for i in list_videos.videos:
        print(i)

    print("Відео з роком більшим ніж заданий:")
    print(*list_videos.find_all_with_year_more_than(2022), sep="\n")

    print("Відео з однаковим режисером:")
    print(*list_videos.find_all_with_same_director("SashaBo"), sep="\n")
