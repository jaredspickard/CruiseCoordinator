from app import db


# create a table to store relationships between Cruisers
# ensure first_cruiser_id < second_cruiser_id
CruiserRelationship = db.Table(
    'cruiser_relationships',
    db.Column('first_cruiser_id', db.Integer, db.ForeignKey('cruisers.id'), primary_key=True),
    db.Column('second_cruiser_id', db.Integer, db.ForeignKey('cruisers.id'), primary_key=True),
    db.Column('type', db.Text)
)
