import requests
from bs4 import BeautifulSoup
import re as regex

from indexer.JSONEncoder import JSONEncoder
from indexer.Director import Director
from indexer.Movie import Movie
from indexer.MongoPersistence import MongoPersistence


class ExtractorAttributesPage:

    def __init__(self, url_movie, url_base):
        self.url_movie = url_movie
        self.url_base = url_base

    def extract(self):
        page_movie = requests.get(self.url_movie).content
        soup = BeautifulSoup(page_movie, 'html.parser')
        title_wrapper = soup.find('div', {'class': 'title_wrapper'})
        ratting_wrapper = soup.find('span', {'itemprop': 'ratingValue'})

        title_movie = title_wrapper.h1.text
        duration_minutes = int(regex.sub("[^0-9]", "", title_wrapper.div.time.get('datetime')))
        ratting = float(ratting_wrapper.text)

        genres = []
        for genre in title_wrapper.div.find('a', attrs={'href': regex.compile(r'genres*')}):
            genres.append(genre.text)

        director_name, director_country = self.extract_director_properties(page_movie)
        director = Director(director_name, director_country)
        movie = Movie(title_movie, duration_minutes, ratting, genres, director)

        return movie

    def extract_director_properties(self, page_movie):
        soup = BeautifulSoup(page_movie, 'html.parser')
        for person in soup.find_all('div', attrs={'class': 'credit_summary_item'}):
            if person.h4.text == 'Director:':
                director_href = person.a.get('href')
                page_director = requests.get(self.url_base + director_href).content
                soup = BeautifulSoup(page_director, 'html.parser')
                header_information = soup.find('h1', {'class': 'header'})
                director_name = header_information.find('span', {'class': 'itemprop'}).text
                country = soup.find('div', {'id': 'name-born-info'}).find('a', attrs={
                    'href': regex.compile('birth_place*')}).text.split(',')[2]
                return director_name, country



if __name__ == '__main__':
    extractor = ExtractorAttributesPage("https://www.imdb.com/title/tt1477834/?ref_=rvi_tt", "https://www.imdb.com/")
    movie = extractor.extract()
    movie_in_json = JSONEncoder(movie).to_json()
    mongo_store = MongoPersistence("mongodb://MarcosNeco:familia1993@ds237955.mlab.com:37955/movie_imdb")
    mongo_store.persist(movie_in_json)
    print(movie_in_json)
