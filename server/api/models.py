from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login


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


@login.user_loader
def load_user(id):
    return Cruiser.query.get(int(id))


# create a table to store relationships between Cruisers
# ensure first_cruiser_id < second_cruiser_id
cruiser_relationships = db.Table(
    'cruiser_relationships',
    db.Column('first_cruiser_id', db.Integer, db.ForeignKey('cruisers.id'), primary_key=True),
    db.Column('second_cruiser_id', db.Integer, db.ForeignKey('cruisers.id'), primary_key=True),
    db.Column('type', db.Text)
)


# class ExternalAccount(db.Model):
#     """ Class to store external_account information for cruisers. """
#     __tablename__ = 'external_accounts'
#     id = db.Column(db.Integer, primary_key=True)
#     cruiser_id = db.Column(db.Integer, db.ForeignKey('cruisers.id'))
#     external_id = db.Column(db.Text, index=True)
#     external_type = db.Column(db.Text, index=True)
#     __table_args__ = (
#         db.UniqueConstraint('external_id', 'external_type', name='_unique_external_account'),
#         db.UniqueConstraint('cruiser_id', 'external_type', name='_unique_external_type_per_cruiser')
#     )


class Trip(db.Model):
    """ Class representing an overall Trip. """
    __tablename__ = 'trips'
    id = db.Column(db.Integer, primary_key=True)
    coordinator_id = db.Column(db.Integer, db.ForeignKey('cruisers.id'))
    name = db.Column(db.Text)
    description = db.Column(db.Text)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    # visible_to_friends = db.Column(db.Boolean, default=False)
    # TODO: add more details related to privacy and attendee accessability

    def serialize(self):
        """ Returns object in dict format. """
        return {
            'id': self.id,
            'coordinator_id': self.coordinator_id,
            'name': self.name,
            'description': self.description,
            'start_date': self.start_date,
            'end_date': self.end_date
        }


# define relationship for cruisers and trips (manages invitations/requests as well)
trip_attendees = db.Table(
    'trip_attendees',
    db.Column('trip_id', db.Integer, db.ForeignKey('trips.id'), primary_key=True),
    db.Column('cruiser_id', db.Integer, db.ForeignKey('cruisers.id'), primary_key=True),
    db.Column('pending_coordinator_approval', db.Boolean, default=True),
    db.Column('pending_cruiser_acceptance', db.Boolean, default=True)
)


class TripLeg(db.Model):
    """ Class representing a single leg of a trip. """
    __tablename__ = 'trip_legs'
    id = db.Column(db.Integer, primary_key=True)
    trip_id = db.Column(db.Integer, db.ForeignKey('trips.id'))
    starting_point = db.Column(db.Integer, db.ForeignKey('locations.id'))
    destination = db.Column(db.Integer, db.ForeignKey('locations.id'))
    # TODO: add more details (such as dates)


# TODO: consider creating a table to allow cruisers to save vehicle info (can prepopulate this model)
class TripVehicle(db.Model):
    """ Class representing a vehicle that's available on this trip. """
    __tablename__ = 'trip_vehicles'
    id = db.Column(db.Integer, primary_key=True)
    cruiser_id = db.Column(db.Integer, db.ForeignKey('cruisers.id'))
    trip_id = db.Column(db.Integer, db.ForeignKey('trips.id'))
    vehicle_name = db.Column(db.Text)
    # TODO: add vehicle info (make/model/color, number of seats, etc.)


class LegVehicle(db.Model):
    """ Class representing an instance of a TripVehicle for a single leg of the Trip. """
    __tablename__ = 'trip_leg_vehicles'
    id = db.Column(db.Integer, primary_key=True)
    leg_id = db.Column(db.Integer, db.ForeignKey('trip_legs.id'))
    vehicle_id = db.Column(db.Integer, db.ForeignKey('trip_vehicles.id'))
    # TODO: add leg-specific data


# define relationship between cruisers, trip_legs, and leg_vehicles
leg_participants = db.Table(
    'leg_participants',
    db.Column('leg_id', db.Integer, db.ForeignKey('trip_legs.id'), primary_key=True),
    db.Column('cruiser_id', db.Integer, db.ForeignKey('cruisers.id'), primary_key=True),
    db.Column('vehicle_id', db.Integer, db.ForeignKey('trip_leg_vehicles.id'))
)


class Location(db.Model):
    """ Class to store locations (addresses). """
    __tablename__ = 'locations'
    id = db.Column(db.Integer, primary_key=True)
    street_address = db.Column(db.Text)
    city = db.Column(db.Text)
    state = db.Column(db.Text)
    zip_code = db.Column(db.Text)
