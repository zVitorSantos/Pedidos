from flask import Flask
from app.models import db, User

app = Flask(__name__)

# Configurações do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  
db.init_app(app)

with app.app_context():
    # Crie o banco de dados
    db.create_all()