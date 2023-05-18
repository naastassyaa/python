from models.Video import Video


class TikTok(Video):
    def __init__(self, title="", director="", year=0, name_of_song="", likes=0, views=0, comments=0):
        super().__init__(title, director, year)
        self.name_of_song = name_of_song
        self.likes = likes
        self.views = views
        self.comments = comments

    def __str__(self):
        return f"TikTok({self.title}, {self.director}, {self.year}, {self.name_of_song}, " \
               f"{self.likes}, {self.views}, {self.comments})"

    def get_current_rating(self):
        return (self.likes + self.comments) / self.views
