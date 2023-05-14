class Film:
    __instance = None

    def __init__(self, title="", director="", year=0, rating=0, marks=0):
        self.__title = title
        self.__director = director
        self.__year = year
        self.__rating = rating
        self.__marks = marks

    @property
    def title(self):
        return self.__title

    @property
    def director(self):
        return self.__director

    @property
    def year(self):
        return self.__year

    @property
    def rating(self):
        return self.__rating

    @property
    def marks(self):
        return self.__marks

    @title.setter
    def title(self, title):
        self.__title = title

    @director.setter
    def director(self, director):
        self.__director = director

    @year.setter
    def year(self, year):
        self.__year = year

    @rating.setter
    def rating(self, rating):
        self.__rating = rating

    @marks.setter
    def marks(self, marks):
        self.__marks = marks

    def __str__(self):
        return f"Film({self.__title}, {self.__director}, {self.__year}, {self.__rating}, {self.__marks})"

    def rate(self, rating):
        if rating > 10:
            rating = 10
        elif rating < 1:
            rating = 1
        self.__rating += rating
        self.__marks += 1

    def get_current_rating(self):
        return self.__rating / self.__marks

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = Film()
        return cls.__instance


