from app import db


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
