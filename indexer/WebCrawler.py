from bs4 import BeautifulSoup
import requests


def index_url_movies(initial_url, max_movies):
    crawled, to_crawl, url_movies = [], [], []
    to_crawl.append(initial_url)

    while to_crawl:
        current_url = to_crawl.pop(0)
        response_url = requests.get(current_url)
        html_extractor = BeautifulSoup(response_url.content, 'html.parser')

        for link in html_extractor.findAll('a'):
            if len(url_movies) >= max_movies:
                return url_movies

            href = link.get('href')
            if href is not None:
                if '/title/tt' in href:
                    url_movies.append(current_url + href)
                elif href[0] == "/":
                    to_crawl.append(current_url + href)

    return []


if __name__ == '__main__':
    url = index_url_movies("https://www.imdb.com/", 100)
    print(*url, sep='\n')