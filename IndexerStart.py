from converters.JSONEncoder import JSONEncoder
from indexer.ExtractorAttributesPage import ExtractorAttributesPage
from indexer.WebCrawler import WebCrawler
from persistence.MongoPersistence import MongoPersistence
import sys

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] is not None:
        url_connection_db = sys.argv[1]
    else:
        url_connection_db = "mongodb://movie_imdb:movieisc0l@ds237955.mlab.com:37955/movie_imdb"

    url_base = "https://www.imdb.com/"
    max_movies_to_index = 1000

    persistence = MongoPersistence(url_connection_db)
    total_movies_indexed = persistence.get_total()

    if max_movies_to_index > total_movies_indexed:
        qtd_movies_to_index = max_movies_to_index - total_movies_indexed
        url_pages_movie_indexed = WebCrawler.index_url_movies(url_base, qtd_movies_to_index)

        print("total pages to index:"+str(qtd_movies_to_index)+"||total pages indexed:" + str(qtd_movies_to_index))
        count_persisted = 0
        for url_page_movie in url_pages_movie_indexed:
            extractor = ExtractorAttributesPage(url_page_movie, url_base)
            movie = extractor.extract()
            if movie is not None:
                json_encoder = JSONEncoder(movie)
                movie_json = json_encoder.to_json()
                persistence.persist(movie_json)
                count_persisted += 1
                print("object="+str(movie_json)+" persisted|total:" + str(count_persisted))



