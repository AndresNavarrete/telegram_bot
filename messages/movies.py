import random
import requests
import json

from dotenv import load_dotenv
import os

### http://www.omdbapi.com/ 
def get_movie():
    load_dotenv()
    key = os.environ.get("MOVIE_KEY")
    keywords = ["one", "star", "war", "love", "god", "earth", "family", "universe", "trial", "rise", "club", "lord", "teen", "europa"]
    keyword = random.choice(keywords)
    page = random.randint(1,2)
    url = "https://www.omdbapi.com/?s={}&apikey={}&type=movie&page={}".format(
        keyword,
        key,
        page
    )

    response = requests.get(url).text
    data = json.loads(response)
    ok = data.get('Response')

    if not ok:
        return False

    search = data.get('Search')
    movie = random.choice(search)

    str = "{} ({})".format(movie["Title"], movie["Year"])
    poster_url = movie["Poster"]

    return (str, poster_url)