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

from server.api import routes, models

@app.route("/", defaults={'path':''})
def serve(path):
    return send_from_directory(app.static_folder,'index.html')

if __name__ == '__main__':
    app.run()
