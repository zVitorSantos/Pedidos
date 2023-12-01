from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    role = db.Column(db.String(20), nullable=False) 
    registration_date = db.Column(db.DateTime, default=datetime.utcnow)
    is_approved = db.Column(db.Boolean, default=False)

    # Relacionamentos
    employees = db.relationship('Employee', back_populates='user', overlaps="employees,user")
    representatives = db.relationship('Representative', back_populates='user', overlaps="representatives,user")
    clients = db.relationship('Client', back_populates='user', lazy=True)
    client_info = db.relationship('Client', back_populates='associated_user', overlaps="clients,user")
    representative_info = db.relationship('Representative', back_populates='representative_user_info', overlaps="representatives,user")
    employee_info = db.relationship('Employee', back_populates='employee_user_info', overlaps="employees,user")
    admin_info = db.relationship('Admin', back_populates='user_info', lazy=True, uselist=False)

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.relationship('User', back_populates='clients', overlaps="clients,user")
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user_info = db.relationship('User', back_populates='client_info', uselist=False, overlaps="clients,user")
    associated_user = db.relationship('User', back_populates='client_info', overlaps="associated_user,clients,user")
    pedidos = db.relationship('Pedido', backref='cliente', lazy=True)

class Representative(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user_info = db.relationship('User', back_populates='representative_user_info', uselist=False, overlaps="representatives,user")
    representative_user_info = db.relationship('User', back_populates='representative_info', overlaps="representatives,user")
    user = db.relationship('User', back_populates='representatives', overlaps="representatives,user")
    clients_associated = db.relationship('Client', secondary='representative_client_association', lazy='subquery', backref=db.backref('representatives_associated', lazy=True))

representative_client_association = db.Table('representative_client_association',
    db.Column('representative_id', db.Integer, db.ForeignKey('representative.id')),
    db.Column('client_id', db.Integer, db.ForeignKey('client.id'))
)

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', back_populates='employees', overlaps="employees,user")
    employee_user_info = db.relationship('User', back_populates='employee_info', overlaps="employees,user")
    pedidos = db.relationship('Pedido', backref='funcionario', lazy=True)

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user_info = db.relationship('User', back_populates='admin_info', uselist=False, overlaps="admin_info,user")

class Pedido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(50), nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
