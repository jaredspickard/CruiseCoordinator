from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from api import db, login


class Cruiser(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Text, index=True, unique=True)
    password_hash = db.Column(db.Text)
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)

    def set_password(self, password):
        """ Hash the given password and save it as the cruiser's password_hash. """
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """ Verify that the hash of the given password matches the stored password hash. """
        return check_password_hash(self.password_hash, password)

    @classmethod
    def get_by_google_id(cls, user_id):
        return cls.query.filter_by(google_user_id=user_id).first()


@login.user_loader
def load_user(id):
    return Cruiser.query.get(int(id))


class ExternalAccount(db.Model):
    """ Class to store external_account information for cruisers. """
    __tablename__ = 'external_accounts'
    id = db.Column(db.Integer, primary_key=True)
    cruiser_id = db.Column(db.Integer, db.ForeignKey('cruiser.id'))
    external_id = db.Column(db.Text, index=True)
    external_type = db.Column(db.Text, index=True)
    __table_args__ = (
        db.UniqueConstraint('external_id', 'external_type', name='_unique_external_account'),
        db.UniqueConstraint('cruiser_id', 'external_type', name='_unique')
    )


class Trip(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    trip_name = db.Column(db.Text)
    coordinator_id = db.Column(db.Integer, db.ForeignKey('cruiser.id'))
