## Melopedia
App for music lovers.
Add all your artists, sort them and rate them.

See [screenshots](/screenshots) folder

## Why ?
Since I listen music via streaming, I discovered lot of new good stuff and I a bit forgot my local music.
Streaming apps does not have all music and the artists management is not enought mature for the moment, so I needed something where I can view all my music library, rate it, explore it and sort it.

## Requirements
- [Last.fm API key](http://www.last.fm/fr/api) to retrieve artists info (can be disable in source)
- Python 2.7 and later
- SQL database

## Deploying
- Create virtualenv and install dependencies with [pip](https://pip.pypa.io/en/stable/installing/)
```sh
$ pip install virtualenv
$ virtualenv /path/to/melopedia/venv
$ source /path/to/melopedia/venv/bin/activate
$ pip install -r requirements.txt
```
- Create SQL database and configure connexion in config.py file [doc](http://flask-sqlalchemy.pocoo.org/2.1/config/)
- Create database structure
```sh
$ ./db_create.py
```
- Start app. Exemple invocations :
```sh
$ ./run.py --host 0.0.0.0
$ ./run.py --host 127.0.1.1 --port 8000
$ ./run.py --debug
```

## Extras
You can use parse_zik.py script to add your local library.
To work well, directory tree must be Tags/artists/albums
Exemples :
```sh
$ ./parse_zik.py -r /path/to/music/Classical/ -g "classical"
```
Add multiple tags, separate by ':'
```sh
$ ./parse_zik.py -r /path/to/music/Metal/Progressive\ Metal/ -g "progressive metal:metal"
```
Pass the --help flag to get a help message.

## Enjoy !
