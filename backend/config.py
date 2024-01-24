class Config:
    # Configurações existentes
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '1234'
    SQLALCHEMY_MIGRATE_REPO = 'migrations'
    JWT_SECRET_KEY = 'teste1234'

    # Configurações do Flask-Mail
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'seu_email@gmail.com'  # Substitua com seu email
    MAIL_PASSWORD = 'sua_senha'  # Substitua com sua senha