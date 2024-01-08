from flask import Blueprint, jsonify, request, flash, redirect, url_for
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity, unset_jwt_cookies, verify_jwt_in_request
from flask_login import current_user, logout_user, login_required
from functools import wraps
from datetime import timedelta, datetime
from app.models import User, Notification, db
from .. import login_manager

auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')

def admin_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if current_user.is_authenticated and current_user.is_admin:
            return func(*args, **kwargs)
        else:
            return jsonify({'error': 'Apenas administradores podem acessar esta rota'}), 403
    return wrapper

@auth_bp.route('/home')
def home():
    if current_user.is_authenticated:
        return jsonify(isAuthenticated=True)
    else:
        return jsonify(isAuthenticated=False)

@auth_bp.route('/register', methods=['POST', 'OPTIONS'])
def register():
    if request.method == 'OPTIONS':
        # Responde à solicitação OPTIONS com os cabeçalhos CORS apropriados
        response = jsonify({'message': 'Preflight request received'})
        response.headers.add('Access-Control-Allow-Methods', 'POST')
        return response

    data = request.json

    # Validação de Dados
    if not all(key in data for key in ['name', 'email', 'password', 'confirmPassword']):
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
    new_user = User(name=data.get('name'), email=email, is_approved=False)
    new_user.set_password(password)
    new_user.save()

    # Crie uma notificação para todos os administradores
    admins = User.query.filter_by(is_admin=True).all()
    for admin in admins:
        notification = Notification(user_id=admin.id, text=f'Novo registro: {User(name=data.get('name'))}')
        db.session.add(notification)

    db.session.commit()

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

    # Promover a admin se solicitado
    if request.json.get('promote_to_admin'):
        user.is_admin = True

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

@auth_bp.route('/notifications', methods=['GET'])
@jwt_required()
def check_notifications():
    current_user = get_jwt_identity()
    user = User.query.filter_by(email=current_user).first()

    if not user:
        return jsonify({'error': 'Usuário não encontrado'}), 404

    notifications = [notification.to_dict() for notification in user.notifications]
    return jsonify({'notifications': notifications}), 200

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    remember_me = data.get('rememberMe', False)

    user = User.query.filter_by(email=email).first()

    if user and user.check_password(password):
        if user.is_approved:
            # Crie um token de acesso
            access_token = create_access_token(identity=email)
            # Crie um token de atualização com base na opção "Lembre-me"
            if remember_me:
                refresh_token = create_refresh_token(identity=email, expires_delta=timedelta(days=7))
            else:
                refresh_token = create_refresh_token(identity=email, expires_delta=timedelta(hours=1))

            # Registre o login do usuário
            user.last_login = datetime.utcnow()
            db.session.commit()

            return jsonify(access_token=access_token, refresh_token=refresh_token), 200
        else:
            return jsonify({'error': 'Aguardando aprovação do administrador'}), 403
    else:
        return jsonify({'error': 'Credenciais inválidas'}), 401
    
@auth_bp.route('/verify-token', methods=['GET', 'OPTIONS'])
def verify_token():
    if request.method != 'OPTIONS':
        verify_jwt_in_request()
        current_user = get_jwt_identity()
        return jsonify(logged_in_as=current_user), 200
    else:
        return jsonify({}), 200
    
@auth_bp.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    current_user = get_jwt_identity()
    access_token = create_access_token(identity=current_user)
    return jsonify(access_token=access_token), 200
    
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
    
@auth_bp.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    resp = jsonify({'message': 'Logout bem-sucedido'})
    unset_jwt_cookies(resp)
    return resp, 200
