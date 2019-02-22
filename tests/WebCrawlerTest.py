import unittest

from indexer.WebCrawler import WebCrawler


class WebCrawlerTest(unittest.TestCase):

    def setUp(self):
        self.url_imdb = "https://www.imdb.com/"

    def test_index_urls_indexed(self):
        url = WebCrawler.index_url_movies(self.url_imdb, 100)
        self.assertEqual(100, len(url))

    def test_patter_movie_url(self):
        url = WebCrawler.index_url_movies(self.url_imdb, 5)
        self.assertTrue("/title/tt" in url[0])
        self.assertTrue("/title/tt" in url[1])
        self.assertTrue("/title/tt" in url[2])
        self.assertTrue("/title/tt" in url[3])
        self.assertTrue("/title/tt" in url[4])

    def test_if_not_exist_duplicates(self):
        urls_indexed = WebCrawler.index_url_movies(self.url_imdb, 100)
        self.assertTrue(len(urls_indexed) == len(set(urls_indexed)))