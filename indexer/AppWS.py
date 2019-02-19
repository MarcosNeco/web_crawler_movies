from flask import Flask
app = Flask(__name__)


@app.route("/")
def get_movies():
    return "movies"


app.run(host='localhost', port=8080, debug=True, load_dotenv=False)




