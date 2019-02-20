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
    #prefered_directors = StatsMovies.getTopDirectors(persistence)

    content = '<h1>Estatísticas dos filmes</h1>'.join('<ul>')
    content = content.join('<li>Qual a probabilidade de uma mulher ser diretora do filme? '+str(prob_woman_director)+'</li>')
    content = content.join('<li>Qual o tempo de duração médio dos filmes obtidos? ' + str(mean_duration_movies) + '</li>')
    content = content.join('<li>Qual a probabilidade de cada filme em seu gênero ter uma avaliação ' +
                 'superior a 8? ').join(prob_higher_eight_by_genre).join('</li>')
    content = content.join('<li>Qual a probabilidade de um filme ter avaliação superior ' +
                 'a 8, considerando que ele não possui um diretor americano?' + str(prob_director_non_american)+'</li>')
    #content = content.join('<li>quais são os diretores preferidos?').join(prefered_directors).join('</li>')
    content = content.join('</ul>')
    return '<html><head>custom head stuff here</head><body>' + content + '</body></html>'


app.run(host='localhost', port=8080, debug=True, load_dotenv=False)




