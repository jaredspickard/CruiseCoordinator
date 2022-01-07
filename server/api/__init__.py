from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_praetorian import Praetorian
from flask_cors import CORS
from config import Config


app = Flask(__name__)
app.debug = True
app.config.from_object(Config)

db = SQLAlchemy()
# guard = Praetorian()
cors = CORS()

from api import routes, models

db.init_app(app)
# guard.init_app(app, models.User)
cors.init_app(app)

# Add users for the example
# with app.app_context():
#     db.create_all()
#     if db.session.query(models.User).filter_by(username='Yasoob').count() < 1:
#         db.session.add(User(
#           username='Yasoob',
#           password=guard.hash_password('strongpassword'),
#           roles='admin'
#             ))
#     db.session.commit()
