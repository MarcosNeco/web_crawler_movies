from bs4 import BeautifulSoup
import re as regex
import requests


class WebCrawler:

    @staticmethod
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
                if href is not None and href:
                    if '/title/tt' in href:
                        href_cleaned = regex.sub('.+?(?=/title)', '', href)
                        href_to_index = initial_url + href_cleaned
                        url_movies.append(href_to_index)
                        print("indexed url:" + href_to_index + "|total:" + str(len(url_movies)))
                    elif href[0] == "/":
                        to_crawl.append(current_url + href)

        return []


if __name__ == '__main__':
    url = WebCrawler.index_url_movies("https://www.imdb.com/", 1000)
    print(*url, sep='\n')