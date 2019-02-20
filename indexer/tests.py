from converters.JSONEncoder import JSONEncoder
from model.Director import Director
from persistence.MongoPersistence import MongoPersistence
from model.Movie import Movie
from stats.StatsMovies import StatsMovies


def test_persist_movies():
    mongo_persistence = MongoPersistence("mongodb://movie_imdb:movieisc0l@ds237955.mlab.com:37955/movie_imdb")
    director = Director("ramon", "USA", 2, "M")
    movie = Movie(name="salvando de uma cilada", duration=130, ratting=8.5, genres=["comedia"], director=director)
    movie_json = JSONEncoder(movie).to_json()
    mongo_persistence.persist(movie_json)


def test_probability_director_female():
    mongo_persistence = MongoPersistence("mongodb://movie_imdb:movieisc0l@ds237955.mlab.com:37955/movie_imdb")
    print(StatsMovies.probability_director_female(mongo_persistence))

def test_avg_duration_movies():
    mongo_persistence = MongoPersistence("mongodb://movie_imdb:movieisc0l@ds237955.mlab.com:37955/movie_imdb")
    print(StatsMovies.mean_duration_movies(mongo_persistence))


def test_ratting_high_than_eight():
    mongo_persistence = MongoPersistence("mongodb://movie_imdb:movieisc0l@ds237955.mlab.com:37955/movie_imdb")
    print(StatsMovies.probability_higher_than_eight(mongo_persistence))

def test_ratting_high_than_eight_by_genre():
    mongo_persistence = MongoPersistence("mongodb://movie_imdb:movieisc0l@ds237955.mlab.com:37955/movie_imdb")
    print(StatsMovies.probability_higher_than_eight_by_genre(mongo_persistence))

def test_probab_higher_than_eight_director_non_american():
    mongo_persistence = MongoPersistence("mongodb://movie_imdb:movieisc0l@ds237955.mlab.com:37955/movie_imdb")
    print(StatsMovies.probab_higher_than_eight_director_non_american(mongo_persistence))

def test_top10_directtors():
    mongo_persistence = MongoPersistence("mongodb://movie_imdb:movieisc0l@ds237955.mlab.com:37955/movie_imdb")
    print(StatsMovies.getTopDirectors(mongo_persistence, 15))


if __name__ == '__main__':
    #test_probability_director_female()
    #$test_avg_duration_movies()
    #test_ratting_high_than_eight()
    #test_ratting_high_than_eight_by_genre()
    test_probab_higher_than_eight_director_non_american()
    #test_persist_movies()
    #test_top10_directtors()

