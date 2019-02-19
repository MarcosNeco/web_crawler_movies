from pymongo import MongoClient

from indexer.Movie import Movie


class MongoPersistence:

    def __init__(self, url_connection):
        self.url_connection = url_connection

    def connect(self, database='movie_imdb', collection='movie'):
        mongo_client = MongoClient(self.url_connection)
        movie_db = mongo_client[database]
        return movie_db[collection]

    def persist(self, movie_to_store: Movie):
        movie_collection = self.connect()
        movie_saved = movie_collection.find_one({"name": movie_to_store['name']})
        if movie_saved is None:
            movie_collection.insert_one(movie_to_store)
        else:
            update_query = {"$set": movie_to_store}
            movie_collection.update_one({"_id": movie_saved['_id']}, update_query)

    def find(self, query):
        return self.connect().find(query)

    def find_one(self, query):
        return self.connect().find_one(query)

    def aggregate(self, query):
        return self.connect().aggregate(query)

