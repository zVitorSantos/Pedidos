from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship
from . import db

user_empresa = db.Table('user_empresa',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('empresa_id', db.Integer, db.ForeignKey('empresa.id'), primary_key=True)
)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
        
    role = db.Column(db.String(50))
    is_approved = db.Column(db.Boolean, default=False)
    is_complete = db.Column(db.Boolean, default=False)
    is_person = db.Column(db.Boolean)
    cpf = db.Column(db.String(14))  
    cnpj = db.Column(db.String(18))  
    state_registration = db.Column(db.String(50)) 
    state = db.Column(db.String(50))
    city = db.Column(db.String(100))
    postal_code = db.Column(db.String(9))
    address = db.Column(db.String(200))
    contact_email = db.Column(db.String(120))
    contact_phone = db.Column(db.String(20))
    empresas = db.relationship('Empresa', secondary=user_empresa, back_populates='users')

    # Relationships
    client = db.relationship('Client', backref='user', uselist=False)
    representative = db.relationship('Representative', backref='user', uselist=False)
    employee = db.relationship('Employee', backref='user', uselist=False)
    admin = db.relationship('Admin', backref='user', uselist=False)

    def save(self):
        db.session.add(self)
        db.session.commit()

class Empresa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    users = db.relationship('User', secondary=user_empresa, back_populates='empresas')

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    orders = db.relationship('Order', backref='client')

class Representative(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    clients = db.relationship('Client', secondary='representative_client_association', backref='representatives')

    representative_client_association = db.Table('representative_client_association',
    db.Column('representative_id', db.Integer, db.ForeignKey('representative.id')),
    db.Column('client_id', db.Integer, db.ForeignKey('client.id')))

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    orders = db.relationship('Order', backref='employee')

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(50), nullable=False)
    status_info = db.Column(db.String(200))
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'))