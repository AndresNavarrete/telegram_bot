import random
import requests
import json

from dotenv import load_dotenv
import os

### http://www.omdbapi.com/ 
### https://imdb-api.com/api
def get_popular_movie():
    load_dotenv()
    key_imdb = os.environ.get('IMDB_KEY')
    
    url = "https://imdb-api.com/API/MostPopularMovies/{}".format(
        key_imdb
    )
    response = requests.get(url).text
    data = json.loads(response)
    ok = data.get('errorMessage') == ''

    if not ok:
        return False

    items = data.get('items')
    movie = random.choice(items)
    movie_id = movie.get('id')

    title = movie.get('fullTitle')
    plot, poster_url = get_movie_plot_and_poster(movie_id)
    str = title + "\n\n" + plot
    return (str, poster_url)

def get_movie_plot_and_poster(imdb_id: str):
    key = os.environ.get("MOVIE_KEY")
    url = "https://www.omdbapi.com/?i={}&apikey={}".format(
        imdb_id,
        key
    )
    response = requests.get(url).text
    data = json.loads(response)
    plot = data.get('Plot')
    poster = data.get('Poster')
    return plot, poster

def get_top_movie():
    with open('data/250_movies.json', 'r') as f:
        movies = json.load(f)
    movie = random.choice(movies["items"])
    movie_id = movie.get('id')

    title = movie.get('fullTitle')
    plot, poster_url = get_movie_plot_and_poster(movie_id)
    str = title + "\n\n" + plot
    return (str, poster_url)

def get_k_drama():
    k_drama_list = ["ls022410475",  "ls020438463"]
    imdb_list = random.choice(k_drama_list)
    key_imdb = os.environ.get('IMDB_KEY')
    
    url = "https://imdb-api.com/en/API/IMDbList/{}/{}".format(
        key_imdb,
        imdb_list
    )
    response = requests.get(url).text
    data = json.loads(response)
    ok = data.get('errorMessage') == ''
    if not ok:
        return False
    items = data.get('items')
    movie = random.choice(items)
    movie_id = movie.get('id')

    title = movie.get('fullTitle')
    plot, poster_url = get_movie_plot_and_poster(movie_id)
    str = title + "\n\n" + plot
    return (str, poster_url)







