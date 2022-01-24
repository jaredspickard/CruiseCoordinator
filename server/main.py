import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_heroku import Heroku
# from flask_cors import CORS


app = Flask(__name__)
app.debug = True

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'skadoooooooosh-and-a-lil-kerpluuuuuuunk'
    GOOGLE_CLIENT_ID = '301139010020-rm1mnr8dlnd3656lt8j5f1gv6o001uv6.apps.googleusercontent.com'
    # SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/jaredspickard'
    PRAETORIAN_ROLES_DISABLED = True

app.config.from_object(Config)

heroku = Heroku(app)
db = SQLAlchemy(app)
login = LoginManager(app)
# guard = Praetorian()
# cors = CORS()

from api import routes, models

# db.init_app(app)
# guard.init_app(app, models.Cruiser)
# cors.init_app(app)

# Add users for the example
# with app.app_context():
#     db.create_all()
#     db.session.commit()
#     if db.session.query(models.User).filter_by(username='Yasoob').count() < 1:
#         db.session.add(User(
#           username='Yasoob',
#           password=guard.hash_password('strongpassword'),
#           roles='admin'
#             ))
    # db.session.commit()

if __name__ == '__main__':
    app.run()
