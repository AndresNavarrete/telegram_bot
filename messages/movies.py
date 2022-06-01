import random
import requests
import json


def get_movie():

    key = '7413c775'
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