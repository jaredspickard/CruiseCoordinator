import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'skadoooooooosh-and-a-lil-kerpluuuuuuunk'
    GOOGLE_CLIENT_ID = '301139010020-rm1mnr8dlnd3656lt8j5f1gv6o001uv6.apps.googleusercontent.com'
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(os.getcwd(), 'database.db')}"
    PRAETORIAN_ROLES_DISABLED = True
