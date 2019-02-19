from indexer.Movie import Movie
import json


class JSONEncoder:

    def __init__(self, movie: Movie):
        self.movie = movie

    def to_json(self):
        movie_dict = {
            "name": self.movie.name,
            "duration": self.movie.duration,
            "ratting": self.movie.ratting,
            "genre": self.movie.genres,
            "director_name": self.movie.director.name,
            "director_country": self.movie.director.country,
            "director_genre": self.movie.director.genre}
        return movie_dict


