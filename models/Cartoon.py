from models.Video import Video


class Cartoon(Video):
    def __init__(self, title="", director="", year=0, genre="", number_of_characters=0, rating=0, marks=0):
        super().__init__(title, director, year)
        self.genre = genre
        self.number_of_characters = number_of_characters
        self.rating = rating
        self.marks = marks

    def __str__(self):
        return f"Cartoon({self.title}, {self.director}, {self.year}, {self.genre}, " \
               f"{self.number_of_characters}, {self.rating}, {self.marks})"

    def get_current_rating(self):
        return self.rating / self.marks
