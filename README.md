# Badly Written Flask Speedway

A poorly written Flask app that hosts a simple SQLLite DB of Bluetooth tags and does some basic DB manipulation.

The app code is based off code from the [Digital Ocean Flask/SQLite tutorial](https://www.digitalocean.com/community/tutorials/how-to-use-an-sqlite-database-in-a-flask-application) which is really quite a good introduction to Flask/SQLite.

Most of the CSS/HTML is from [W3Schools How To](https://www.w3schools.com/howto/default.asp) because I was too lazy to put a lot of effort into this. 

Maybe I'll revisit this at some point maybe I won't.

<img src="https://media.giphy.com/media/104vPBH8buV9vy/giphy.gif" width="480" height="303" frameBorder="0" class="giphy-embed" allowFullScreen></img><p><a href="https://giphy.com/gifs/tim-and-eric-idk-shrug-104vPBH8buV9vy">via GIPHY</a></p>


## Using this

1. `git clone https://github.com/roscoejp/flask-speedway.git`
1. `cd flask-speedway`
1. `pip install -r ./requirements.txt`
1. `python ./init_db.py`
1. `flask run`
1. Navigate to the URL provided in the output


## Configuration

- [.env](./.env) can contain any other env variables:
    - `SECRET_KEY`
    - `PORT`
    - `HOST`
    - `FLASK_APP`
    - `FLASK_ENV`

## Other files

- `sample_data.json` contains a sample body for a POST request from a Speedway Connect RFID antenna
- `test-publis-endpoint.ps1` is a script to make testing the publish endpoint easier. This emulates a Speedway Connect antenna posting every 5 seconds
- `.venv.ps1` is a script to make virtual envs easier to use in Windows
