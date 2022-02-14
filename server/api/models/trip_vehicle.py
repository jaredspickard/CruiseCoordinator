from app import db


class TripVehicle(db.Model):
    """ Class representing a vehicle that's available on this trip. """
    __tablename__ = 'trip_vehicles'
    id = db.Column(db.Integer, primary_key=True)
    cruiser_id = db.Column(db.Integer, db.ForeignKey('cruisers.id'))
    trip_id = db.Column(db.Integer, db.ForeignKey('trips.id'))
    vehicle_name = db.Column(db.Text)
    # TODO: add vehicle info (make/model/color, number of seats, etc.)
