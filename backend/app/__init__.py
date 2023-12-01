from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class='config.Config'):
    app = Flask(__name__)

    # Configurações do seu aplicativo Flask
    app.config.from_object(config_class)

    # Configurações do SQLAlchemy
    db.init_app(app)

    # Habilita CORS para permitir solicitações do frontend
    CORS(app)

    # Registra as blueprints
    from app.routes.auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/api/auth')

    # Inicializa o Flask-Migrate após configurar o aplicativo
    migrate.init_app(app, db)

    return app
