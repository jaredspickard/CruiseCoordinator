from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_heroku import Heroku
from server.config import Config


app = Flask(__name__, static_url_path='', static_folder='client/build')
app.debug = True
app.config.from_object(Config)

heroku = Heroku(app)
db = SQLAlchemy(app)
login = LoginManager(app)

# import the routes
from server.api.routes.cruiser import *
from server.api.routes.trip import *
# import the models
from server.api.models.cruiser import *
from server.api.models.trip import *

# TODO: comment out the below route when running locally
@app.route("/", defaults={'path':''})
def serve(path):
    return send_from_directory(app.static_folder,'index.html')

if __name__ == '__main__':
    app.run()
