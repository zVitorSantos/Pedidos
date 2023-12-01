from app import db
from app.models import User, Client

# Crie um cliente
client = Client()  
db.session.add(client)
db.session.commit()

# Crie um usuário com o cliente associado
user = User(username='test', email='test@example.com', password='password', client_info=client)
db.session.add(user)
db.session.commit()
