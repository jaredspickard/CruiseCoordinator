from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login


class Cruiser(UserMixin, db.Model):
    __tablename__ = 'cruisers'
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

    def serialize(self):
        """ Returns object in dict format. """
        return {
            'id': self.id,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name
        }


@login.user_loader
def load_user(id):
    return Cruiser.query.get(int(id))


class ExternalAccount(db.Model):
    """ Class to store external_account information for cruisers. """
    __tablename__ = 'external_accounts'
    id = db.Column(db.Integer, primary_key=True)
    cruiser_id = db.Column(db.Integer, db.ForeignKey('cruisers.id'))
    external_id = db.Column(db.Text, index=True)
    external_type = db.Column(db.Text, index=True)
    __table_args__ = (
        db.UniqueConstraint('external_id', 'external_type', name='_unique_external_account'),
        db.UniqueConstraint('cruiser_id', 'external_type', name='_unique_external_type_per_cruiser')
    )


class Trip(db.Model):
    """ Class representing an overall Trip. """
    __tablename__ = 'trips'
    id = db.Column(db.Integer, primary_key=True)
    trip_name = db.Column(db.Text)
    coordinator_id = db.Column(db.Integer, db.ForeignKey('cruisers.id'))

    def serialize(self):
        """ Returns object in dict format. """
        return {
            'id': self.id,
            'trip_name': self.trip_name,
            'coordinator_id': self.coordinator_id
        }


trip_attendees = db.Table(
    'trip_attendees',
    db.Column('trip_id', db.Integer, db.ForeignKey('trip.id'), primary_key=True),
    db.Column('cruiser_id', db.Integer, db.ForeignKey('cruisers.id'), primary_key=True),
    db.Column('pending', db.Boolean, default=True)
)


class TripLeg(db.Model):
    """ Class representing a single leg of a trip. """
    __tablename__ = 'trip_legs'
    id = db.Column(db.Integer, primary_key=True)
    trip_id = db.Column(db.Integer, db.ForeignKey('trip.id'))
    starting_point = db.Column(db.Integer, db.ForeignKey('location.id'))
    destination = db.Column(db.Integer, db.ForeignKey('location.id'))


class Location(db.Model):
    """ Class to store locations (addresses). """
    __tablename__ = 'locations'
    id = db.Column(db.Integer, primary_key=True)
    street_address = db.Column(db.Text)
    city = db.Column(db.Text)
    state = db.Column(db.Text)
    zip_code = db.Column(db.Text)
