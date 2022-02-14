from app import db


# define relationship between cruisers, trip_legs, and leg_vehicles
LegParticipant = db.Table(
    'leg_participants',
    db.Column('leg_id', db.Integer, db.ForeignKey('trip_legs.id'), primary_key=True),
    db.Column('cruiser_id', db.Integer, db.ForeignKey('cruisers.id'), primary_key=True),
    db.Column('vehicle_id', db.Integer, db.ForeignKey('trip_leg_vehicles.id'))
)
