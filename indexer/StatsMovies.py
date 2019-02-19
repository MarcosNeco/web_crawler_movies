from indexer.MongoPersistence import MongoPersistence


class StatsMovies:

    @staticmethod
    def probability_director_female(mongo_persistence):
        total_directors = mongo_persistence.find({}).count()
        female_directors = mongo_persistence.find({"director_genre": "F"}).count()
        return total_directors / female_directors

    @staticmethod
    def mean_duration_movies(mongo_persistence: MongoPersistence):
        duration_mean = mongo_persistence.aggregate([{'$group': {'_id': 'null', 'mean_duration': {'$avg': '$duration'}}}])
        return list(duration_mean).pop(0)['mean_duration']

