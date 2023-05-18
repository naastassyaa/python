from models.Video import Video


class Clip(Video):
    def __init__(self, title="", director="", year=0, name_of_song="", singer="", likes=0, views=0):
        super().__init__(title, director, year)
        self.name_of_song = name_of_song
        self.singer = singer
        self.likes = likes
        self.views = views

    def __str__(self):
        return f"Clip({self.title}, {self.director}, {self.year}, {self.name_of_song}, " \
               f"{self.singer}, {self.likes}, {self.views})"

    def get_current_rating(self):
        return self.likes / self.views
