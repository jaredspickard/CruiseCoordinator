from app import db


class Location(db.Model):
    """ Class to store locations (addresses). """
    __tablename__ = 'locations'
    id = db.Column(db.Integer, primary_key=True)
    street_address = db.Column(db.Text)
    city = db.Column(db.Text)
    state = db.Column(db.Text)
    zip_code = db.Column(db.Text)
