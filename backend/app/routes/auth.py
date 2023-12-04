from flask import Blueprint, jsonify, request
from flask_login import current_user, logout_user
from functools import wraps
from app.models import User, db

auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')

def admin_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if current_user.is_authenticated and current_user.role == 'admin':
            return func(*args, **kwargs)
        else:
            return jsonify({'error': 'Apenas administradores podem acessar esta rota'}), 403
    return wrapper

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json

    # Validação de Dados
    if not all(key in data for key in ['name', 'email', 'password', 'confirmPassword', 'userType']):
        return jsonify({'error': 'Todos os campos são obrigatórios'}), 400

    # Confirmação de Senha
    password = data.get('password')
    confirm_password = data.get('confirmPassword')
    if password != confirm_password:
        return jsonify({'error': 'A senha e a confirmação de senha não correspondem'}), 400

    # Validação de Email Único
    email = data.get('email')
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({'error': 'Este email já está em uso'}), 400

    # Registro de Usuário
    new_user = User(name=data.get('name'), email=email, user_type=data.get('userType'), is_approved=False)
    new_user.set_password(password)
    new_user.save()

    return jsonify({'message': 'Registro bem-sucedido! Faça login para começar.'}), 201

@auth_bp.route('/approve_user/<int:user_id>', methods=['POST'])
@admin_required
def approve_user(user_id):
    user = User.query.get_or_404(user_id)

    # Verificar se o usuário está aguardando aprovação
    if user.is_approved:
        return jsonify({'error': 'Este usuário já foi aprovado'}), 400

    # Aprovar o usuário
    user.is_approved = True
    db.session.commit()

    return jsonify({'message': 'Usuário aprovado com sucesso'}), 200

@auth_bp.route('/reject_user/<int:user_id>', methods=['POST'])
@admin_required
def reject_user(user_id):
    user = User.query.get_or_404(user_id)

    if user.is_approved:
        # Se o usuário já estiver aprovado, não é possível rejeitar
        return jsonify({'error': 'Este usuário já foi aprovado e não pode ser rejeitado'}), 400

    # Rejeitar o usuário
    db.session.delete(user)
    db.session.commit()

    return jsonify({'message': 'Usuário rejeitado com sucesso'}), 200

@auth_bp.route('/pending_users', methods=['GET'])
@admin_required
def get_pending_users():
    pending_users = User.query.filter_by(is_approved=False).all()

    return jsonify({'pending_users': pending_users}), 200

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()

    if user and user.check_password(password):
        # Verificar se o usuário está aprovado
        if user.is_approved:
            # Implemente a lógica de login aqui
            return jsonify({'message': 'Login bem-sucedido'}), 200
        else:
            return jsonify({'error': 'Aguardando aprovação do administrador'}), 403
    else:
        return jsonify({'error': 'Credenciais inválidas'}), 401
    
@auth_bp.route('/logout', methods=['POST'])
def logout():
    logout_user()
    return jsonify({'message': 'Logout bem-sucedido'}), 200