from app import db


# define relationship for cruisers and trips (manages invitations/requests as well)
TripAttendee = db.Table(
    'trip_attendees',
    db.Column('trip_id', db.Integer, db.ForeignKey('trips.id'), primary_key=True),
    db.Column('cruiser_id', db.Integer, db.ForeignKey('cruisers.id'), primary_key=True),
    db.Column('pending_coordinator_approval', db.Boolean, default=True),
    db.Column('pending_cruiser_acceptance', db.Boolean, default=True)
)
