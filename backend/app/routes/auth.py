from flask import Blueprint, jsonify, request
from app.models import User

auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    confirm_password = data.get('confirmPassword')
    user_type = data.get('userType')

    # Realize as validações necessárias e a lógica de registro aqui
    # (Verifique se o usuário já existe, valide os dados, registre o usuário, etc.)

    # Exemplo: Registro fictício de usuário
    new_user = User(name=name, email=email, password=password, user_type=user_type)
    new_user.save()

    return jsonify({'message': 'Usuário registrado com sucesso'}), 201
