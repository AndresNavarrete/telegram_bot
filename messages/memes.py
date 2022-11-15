import requests
import json
import random

### https://github.com/D3vd/Meme_Api
def get_meme_url():

    subreddits = ["memes", "dankmemes", "me_irl", "wholesomememes"]
    sub = random.choice(subreddits)
    url = "https://meme-api.herokuapp.com/gimme/" + sub
    response = requests.get(url).text
    data = json.loads(response)
    meme_url = data.get("url")
    return meme_url
