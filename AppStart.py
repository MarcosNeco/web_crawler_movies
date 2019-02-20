from converters.JSONEncoder import JSONEncoder
from indexer.ExtractorAttributesPage import ExtractorAttributesPage
from indexer.WebCrawler import WebCrawler
from persistence.MongoPersistence import MongoPersistence

if __name__ == '__main__':
    url_connection_db = "mongodb://movie_imdb:movieisc0l@ds237955.mlab.com:37955/movie_imdb"
    url_base = "https://www.imdb.com/"
    max_movies_to_index = 10000

    persistence = MongoPersistence(url_connection_db)
    total_movies_indexed = persistence.get_total()

    if total_movies_indexed <= total_movies_indexed:
        qtd_movies_to_index = max_movies_to_index - total_movies_indexed
        url_pages_movie_indexed = WebCrawler.index_url_movies(url_base, qtd_movies_to_index)

        print("total pages to index:"+qtd_movies_to_index+"||total pages indexed:" + qtd_movies_to_index)
        for url_page_movie in url_pages_movie_indexed:
            extractor = ExtractorAttributesPage(url_page_movie, url_base)
            movie = extractor.extract()
            json_encoder = JSONEncoder(movie)
            persistence.persist(json_encoder.to_json())


