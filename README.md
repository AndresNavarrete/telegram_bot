# telegram_bot

## Requirements and use
The requirements.txt file should list all Python libraries that are mandatory for running this bot. To install them you can use:
```sh
pipenv shell
```

A `.env` file is needed to run the bot. Enviroment must have the following variables:

```sh

TOKEN=''     # telegram bot token
MOVIE_KEY='' # omdb-api token
IMDB_KEY=''  # imdb-api token

```

All movies data is streamed from [Open Movie Database] and [IMDb Api]

To run the bot you just need to execute the following line:

```sh
python3 main.py
```



[Open Movie Database]: <https://www.omdbapi.com/>
[IMDb Api]:  <https://imdb-api.com/> 
