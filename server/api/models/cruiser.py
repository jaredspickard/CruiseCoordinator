from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db


class Cruiser(UserMixin, db.Model):
    __tablename__ = 'cruisers'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Text, index=True, unique=True)
    username = db.Column(db.Text, index=True, unique=True)
    password_hash = db.Column(db.Text)
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)

    def set_password(self, password):
        """ Hash the given password and save it as the cruiser's password_hash. """
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """ Verify that the hash of the given password matches the stored password hash. """
        return check_password_hash(self.password_hash, password)

    def serialize(self):
        """ Returns object in dict format. """
        return {
            'id': self.id,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name
        }
