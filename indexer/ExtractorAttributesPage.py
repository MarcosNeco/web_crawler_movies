import re as regex

import requests
from bs4 import BeautifulSoup

from model.Director import Director
from converters.JSONEncoder import JSONEncoder
from model.Movie import Movie


class ExtractorAttributesPage:

    def __init__(self, url_movie, url_base):
        self.url_movie = url_movie
        self.url_base = url_base

    def extract(self):
        print("extracting attributes from url:" + self.url_movie)
        page_movie = requests.get(self.url_movie).content
        soup = BeautifulSoup(page_movie, 'html.parser')
        title_wrapper = soup.find('div', {'class': 'title_wrapper'})
        ratting_wrapper = soup.find('span', {'itemprop': 'ratingValue'})

        if title_wrapper is None:
            return None

        title_movie = title_wrapper.h1.text.strip()

        tag_duration = title_wrapper.find('div', {'class': 'subtext'}).time
        if tag_duration is None:
            duration_minutes = None
        else:
            duration_minutes = int(regex.sub("[^0-9]", "", tag_duration.get('datetime')))

        if ratting_wrapper is None:
            ratting = None
        else:
            ratting = float(ratting_wrapper.text)

        genres = []
        for genre in title_wrapper.find('div', {'class': 'subtext'}).find('a', attrs={'href': regex.compile(r'genres*')}):
            genres.append(genre)

        director_name, director_country, position_director = self.extract_director_properties(page_movie)
        director = Director(director_name, director_country, position_director, 'F')
        movie = Movie(title_movie, duration_minutes, ratting, genres, director)

        return movie

    def extract_director_properties(self, page_movie):
        soup = BeautifulSoup(page_movie, 'html.parser')
        for person in soup.find_all('div', attrs={'class': 'credit_summary_item'}):
            if 'Director' in person.h4.text:
                director_href = person.a.get('href')
                page_director = requests.get(self.url_base + director_href).content
                soup = BeautifulSoup(page_director, 'html.parser')
                header_information = soup.find('h1', {'class': 'header'})
                director_name = header_information.find('span', {'class': 'itemprop'}).text.strip()

                tag_born = soup.find('div', {'id': 'name-born-info'})
                if tag_born is None:
                    country = None
                else:
                    country = soup.find('div', {'id': 'name-born-info'}).find('a', attrs={
                        'href': regex.compile('birth_place*')}).text.split(',')[-1].strip()

                tag_position_director = regex.sub("[^0-9]", "", soup.find('span', {'id': 'meterChange'}).text)
                position_director = int(tag_position_director)

                return director_name, country, position_director

        return None, None, None


if __name__ == '__main__':
    extractor = ExtractorAttributesPage("https://www.imdb.com//?ref_=nv_home/title/tt0095765/?ref_=nv_mv_dflt_1", "https://www.imdb.com/")
    movie = extractor.extract()
    #movie_in_json = JSONEncoder(movie).to_json()
 #   print(movie_in_json)

