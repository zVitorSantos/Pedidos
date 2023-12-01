from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from app import db

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    role = db.Column(db.String(20), nullable=False) 
    registration_date = db.Column(db.DateTime, default=datetime.utcnow)
    is_approved = db.Column(db.Boolean, default=False)
    employees = db.relationship('Employee', backref='admin', lazy=True)
    representatives = db.relationship('Representative', backref='employee', lazy=True)
    clients = db.relationship('Client', backref='representative', lazy=True)
    client_info = db.relationship('Client', backref='user', lazy=True, uselist=False)
    representative_info = db.relationship('Representative', backref='user', lazy=True, uselist=False)
    employee_info = db.relationship('Employee', backref='user', lazy=True, uselist=False)
    admin_info = db.relationship('Admin', backref='user', lazy=True, uselist=False)


class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    pedidos = db.relationship('Pedido', backref='cliente', lazy=True)

class Representative(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    clients_associated = db.relationship('Client', secondary='representative_client_association', lazy='subquery', backref=db.backref('representatives_associated', lazy=True))

representative_client_association = db.Table('representative_client_association',
    db.Column('representative_id', db.Integer, db.ForeignKey('representative.id')),
    db.Column('client_id', db.Integer, db.ForeignKey('client.id'))
)

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    pedidos = db.relationship('Pedido', backref='funcionario', lazy=True)

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class Pedido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Campos específicos do pedido
    status = db.Column(db.String(50), nullable=False)
    # Relacionamento com o usuário (cliente ou funcionário)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
