class InvalidRatingException(Exception):
    message = "Rating should be from 1 to 10!"

    def __init__(self):
        super().__init__(self.message)
