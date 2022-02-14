from app import db


class LegVehicle(db.Model):
    """ Class representing an instance of a TripVehicle for a single leg of the Trip. """
    __tablename__ = 'trip_leg_vehicles'
    id = db.Column(db.Integer, primary_key=True)
    leg_id = db.Column(db.Integer, db.ForeignKey('trip_legs.id'))
    vehicle_id = db.Column(db.Integer, db.ForeignKey('trip_vehicles.id'))
    # TODO: add leg-specific data
