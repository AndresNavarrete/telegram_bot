import requests
import json


def get_meme_url():
    url = "https://meme-api.herokuapp.com/gimme"
    response = requests.get(url).text
    data = json.loads(response)
    meme_url = data.get('url')
    return meme_url



