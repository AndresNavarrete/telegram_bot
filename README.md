# telegram_bot

## Requirements and use
The requirements.txt file should list all Python libraries that are mandatory for running this bot. To install them you can use:
```sh
pipenv shell
```

A `.env` file is needed to run the bot. Environment must have the following variables:

```sh
TOKEN=''     # telegram bot token
MOVIE_KEY='' # omdb-api token (used for fetching movie plots and posters)
```

Movie listings are loaded from local JSON files in the `data/` directory. Plot and poster details are fetched from [Open Movie Database].

To run the bot you just need to execute the following line:

```sh
python3 main.py
```

[Open Movie Database]: <https://www.omdbapi.com/>
