from app import db


class TripLeg(db.Model):
    """ Class representing a single leg of a trip. """
    __tablename__ = 'trip_legs'
    id = db.Column(db.Integer, primary_key=True)
    trip_id = db.Column(db.Integer, db.ForeignKey('trips.id'))
    starting_point = db.Column(db.Integer, db.ForeignKey('locations.id'))
    destination = db.Column(db.Integer, db.ForeignKey('locations.id'))
    # TODO: add more details (such as dates)
