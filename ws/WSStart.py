from flask import Flask

from persistence.MongoPersistence import MongoPersistence
from stats.StatsMovies import StatsMovies

app = Flask(__name__)


@app.route("/")
def get_movies():
    url_connection_db = "mongodb://movie_imdb:movieisc0l@ds237955.mlab.com:37955/movie_imdb"
    persistence = MongoPersistence(url_connection_db)
    prob_woman_director = StatsMovies.probability_director_female(persistence)
    mean_duration_movies = StatsMovies.mean_duration_movies(persistence)
    prob_higher_eight_by_genre = StatsMovies.probability_higher_than_eight_by_genre(persistence)
    prob_director_non_american = StatsMovies.probab_higher_than_eight_director_non_american(persistence)
    prefered_directors = StatsMovies.get_top_directors(persistence, 10)

    content = """<h1>Estatísticas dos filmes</h1>
              <ul>
                <li>Qual a probabilidade de uma mulher ser diretora do filme? {prob_woman_director}% </li>
                <li>Qual o tempo de duração médio dos filmes obtidos? {mean_duration_movies} minutos </li>
                <li>Qual a probabilidade de cada filme em seu gênero ter uma avaliação 
                   superior a 8? {prob_higher_eight_by_genre}</li>
                <li>Qual a probabilidade de um filme ter avaliação superior a 8, considerando que
                ele não possui um diretor americano? {prob_director_non_american}%</li>
                <li>quais são os diretores preferidos? {prefered_directors}</li>
              </ul>""".format(prob_woman_director=round(prob_woman_director, 2),
                              mean_duration_movies=round(mean_duration_movies, 2),
                              prob_higher_eight_by_genre=prob_higher_eight_by_genre,
                              prob_director_non_american=round(prob_director_non_american, 2),
                              prefered_directors=prefered_directors)

    return '<html><body>' + content + '</body></html>'


app.run(host='localhost', port=8080, debug=True, load_dotenv=False)




