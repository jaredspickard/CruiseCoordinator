from api import db


class Cruiser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    google_user_id = db.Column(db.Integer, index=True, unique=True)

    @classmethod
    def lookup(cls, username):
        # TODO
        return None

    @classmethod
    def identify(cls, id):
        return cls.query.get(id)

    @property
    def rolenames(self):
        return []

    @property
    def password(self):
        return ''

    @property
    def identity(self):
        return self.id

    @classmethod
    def get_by_google_id(cls, user_id):
        return cls.query.filter_by(google_user_id=user_id).first()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, unique=True)
    password = db.Column(db.Text)
    roles = db.Column(db.Text)
    is_active = db.Column(db.Boolean, default=True, server_default='true')

    @property
    def rolenames(self):
        try:
            return self.roles.split(',')
        except Exception:
            return []

    @classmethod
    def lookup(cls, username):
        return cls.query.filter_by(username=username).one_or_none()

    @classmethod
    def identify(cls, id):
        return cls.query.get(id)

    @property
    def identity(self):
        return self.id

    def is_valid(self):
        return self.is_active