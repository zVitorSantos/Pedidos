class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '1234'
    SQLALCHEMY_MIGRATE_REPO = 'migrations'