import unittest

from indexer.ExtractorAttributesPage import ExtractorAttributesPage


class ExtractorAttributesPageTest(unittest.TestCase):

    def test_extract_properties_from_one_movie(self):
        url_base = "https://www.imdb.com"
        href_movie = "https://www.imdb.com/title/tt0111161/"
        movie = ExtractorAttributesPage(href_movie, url_base).extract()
        self.assertEqual("Um Sonho de Liberdade\xa0(1994)", movie.name)
        self.assertEqual(142, movie.duration)
        self.assertEqual(9.3, movie.ratting)
        self.assertEqual(['Drama'], movie.genres)
        self.assertEqual("Frank Darabont", movie.director.name)
        self.assertEqual("France", movie.director.country)
        self.assertEqual(164, movie.director.position)

    def test_movie_without_info_director(self):
        url_base = "https://www.imdb.com"
        href_movie = "https://www.imdb.com/title/tt0098800/?ref_=nv_sr_1"
        movie = ExtractorAttributesPage(href_movie, url_base).extract()
        self.assertEqual(None, movie.director.name)
        self.assertEqual(None, movie.director.position)
        self.assertEqual(None, movie.director.country)
