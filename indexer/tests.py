from indexer.JSONEncoder import JSONEncoder
from indexer.Director import Director
from indexer.MongoPersistence import MongoPersistence
from indexer.Movie import Movie
from indexer.StatsMovies import StatsMovies


def test_persist_movies():
    mongo_persistence = MongoPersistence("mongodb://movie_imdb:movieisc0l@ds237955.mlab.com:37955/movie_imdb")
    director = Director("director2", "eua", "M")
    movie = Movie(name="penetras bom de papo", duration=130, ratting=5.5, genres=["comedia"], director=director)
    movie_json = JSONEncoder(movie).to_json()
    mongo_persistence.persist(movie_json)


def test_avg_duration_movies():
    mongo_persistence = MongoPersistence("mongodb://movie_imdb:movieisc0l@ds237955.mlab.com:37955/movie_imdb")
    print(StatsMovies.mean_duration_movies(mongo_persistence))


if __name__ == '__main__':
    test_avg_duration_movies()
