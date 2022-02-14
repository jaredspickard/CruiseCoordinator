from app import db


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
