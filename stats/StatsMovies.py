from persistence.MongoPersistence import MongoPersistence


class StatsMovies:

    @staticmethod
    def probability_director_female(mongo_persistence: MongoPersistence):
        total_directors = mongo_persistence.get_total()
        female_directors = mongo_persistence.find({"director_genre": "F"}).count()
        return StatsMovies.calc_probability(female_directors, total_directors)

    @staticmethod
    def mean_duration_movies(mongo_persistence: MongoPersistence):
        duration_mean = mongo_persistence.aggregate([{'$group': {'_id': 'null', 'mean_duration': {'$avg': '$duration'}}}])
        return list(duration_mean).pop(0)['mean_duration']

    @staticmethod
    def probability_higher_than_eight_by_genre(mongo_persistence: MongoPersistence):
        query_total = [{"$unwind": "$genre"},
                       {"$group": {"_id": "$genre", "count": {"$sum": 1}}}
                       ]
        query_high_eight = [{"$unwind": "$genre"},
                            {'$match': {'ratting': {'$gt': 8.0}}},
                            {"$group": {"_id": "$genre", "count": {"$sum": 1}}}
                            ]

        total_genres = list(mongo_persistence.aggregate(query_total))
        high_eight_by_genre = list(mongo_persistence.aggregate(query_high_eight))
        prob_high_eight_genre = []
        for total_genre in total_genres:
            same_genre = next((v for v in high_eight_by_genre if v['_id'] == total_genre['_id']), None)
            if same_genre is not None:
                prob_by_genre = {"gênero": total_genre['_id'],
                                 'probabilidade': StatsMovies.calc_probability(same_genre['count'], total_genre['count'])
                                 }
            else:
                prob_by_genre = {"gênero": total_genre['_id'], 'probabilidade': 0}
            prob_high_eight_genre.append(prob_by_genre)

        return prob_high_eight_genre

    @staticmethod
    def probab_higher_than_eight_director_non_american(mongo_persistence: MongoPersistence):
        query_total = [{'$match': {'director_country': {'$ne': 'USA'}}},
                       {"$group": {"_id": "null", "count": {"$sum": 1}}}
                       ]

        query_director_high_eight = [{'$match': {'$and': [{'director_country': {'$ne': 'USA'}}, {'ratting': {'$gt': 8.0}}]}},
                                     {"$group": {"_id": "null", "count": {"$sum": 1}}},
                                     ]

        total_director_non_american = next(iter(mongo_persistence.aggregate(query_total)), {'count': 0})
        director_high_eight_non_american = next(iter(mongo_persistence.aggregate(query_director_high_eight)), {'count': 0})

        return StatsMovies.calc_probability(director_high_eight_non_american['count'], total_director_non_american['count'])

    @staticmethod
    def get_top_directors(mongo_persistence: MongoPersistence, top: int):
        ascending = -1
        directors_prefered = mongo_persistence.find({}, {"director_name": 1, '_id': 0})\
            .sort('director_position', ascending).limit(top)

        directors = []
        for director in directors_prefered:
            directors.append(director['director_name'])

        return directors

    @staticmethod
    def calc_probability(sample, total):
        if total == 0:
            return 0

        return (sample/total) * 100
