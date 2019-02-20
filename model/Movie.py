from model import Director


class Movie(object):

    def __init__(self, name: str, duration: int, ratting: float, genres: [], director: Director):
        self.name = name
        self.duration = duration
        self.ratting = ratting
        self.genres = genres
        self.director = director
