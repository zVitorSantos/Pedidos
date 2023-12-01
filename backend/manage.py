from app import create_app, db
from app.models import User, Client, Representative, Employee, Admin, Pedido
import os

# Obtenha o caminho absoluto para o diretório atual do script
base_dir = os.path.abspath(os.path.dirname(__file__))
db_dir = os.path.join(base_dir, 'data')
db_path = os.path.join(db_dir, 'database.db') 

# Crie o diretório se não existir
if not os.path.exists(db_dir):
    os.makedirs(db_dir)

# Crie o arquivo do banco de dados se não existir
if not os.path.exists(db_path):
    open(db_path, 'w').close()

# Crie a aplicação
app = create_app()

# Crie o contexto de aplicação
with app.app_context():
    # Configure o caminho do banco de dados
    app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///' + os.path.abspath(db_path)

    # Crie todas as tabelas
    db.create_all()
