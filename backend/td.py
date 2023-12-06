from app import create_app, db
from app.models import User, Empresa

app = create_app()

# Crie um contexto de aplicação
with app.app_context():
    # Obtenha o usuário
    user = User.query.filter_by(email='vendas03.gmg@gmail.com').first()

    # Nomes das empresas a serem criadas
    empresa_names = ['Brilha Natal', 'Verytel', 'Maggiore Modas', 'Maggiore Peças']

    # Crie empresas se elas não existirem
    for name in empresa_names:
        empresa = Empresa.query.filter_by(name=name).first()
        if not empresa:
            empresa = Empresa(name=name)
            db.session.add(empresa)
        
        # Associe a empresa ao usuário
        if empresa not in user.empresas:
            user.empresas.append(empresa)

    db.session.commit()