from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_jwt_extended import JWTManager
from sqlalchemy.orm import configure_mappers

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app(config_class='config.Config'):
    app = Flask(__name__)
    
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    # Configurações do seu aplicativo Flask
    app.config.from_object(config_class)

    # Configurações do SQLAlchemy
    db.init_app(app)

    # Inicialize o LoginManager
    login_manager.init_app(app)

    # Registra as blueprints
    from app.routes.auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/api/auth')

    migrate.init_app(app, db)

    with app.app_context():
        db.create_all()  

    jwt = JWTManager(app)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
        return response

    return app