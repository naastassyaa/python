from models.Video import Video


class Film(Video):
    __instance = None

    def __init__(self, title="", director="", year=0, rating=0, marks=0):
        super().__init__(title, director, year)
        self.rating = rating
        self.marks = marks

    def __str__(self):
        return f"Film({self.title}, {self.director}, {self.year}, {self.rating}, {self.marks})"

    def rate(self, rating):
        if rating > 10:
            rating = 10
        elif rating < 1:
            rating = 1
        self.rating += rating
        self.marks += 1

    def get_current_rating(self):
        return self.rating / self.marks

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = Film()
        return cls.__instance
