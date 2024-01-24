from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Enum
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship
from . import db

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    is_approved = db.Column(db.Boolean, default=False)
    is_admin = db.Column(db.Boolean, default=False)
    notifications = db.relationship('Notification', backref='user', lazy='dynamic')
    ads = db.relationship('Ad', backref='user', lazy='dynamic')

    def save(self):
        db.session.add(self)
        db.session.commit()

class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    referenced_user_id = db.Column(db.Integer)  
    type = db.Column(db.String(50))  
    text = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'text': self.get_notification_text(),
            'timestamp': self.timestamp
        }

    def get_notification_text(self):
        if self.type == 'accept_request':
            return 'Você tem uma nova solicitação de aceitação.'
        # Adicione outras condições para outros tipos de notificações
        else:
            return self.text

# Fretes

class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    cnpj = db.Column(db.String(18), unique=True)
    postal_code = db.Column(db.String(9))




# Parte de Vendas

class Platform(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    sales = db.relationship('Sale', backref='platform', lazy='dynamic')
    commission_fees = db.relationship('CommissionFee', backref='platform', lazy='dynamic')
    reputation_discounts = db.relationship('ReputationDiscount', backref='platform', lazy='dynamic')
    additional_fees = db.relationship('AdditionalFee', backref='platform', lazy='dynamic')

# Taxas

class CommissionFee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    platform_id = db.Column(db.Integer, db.ForeignKey('platform.id'))
    type = db.Column(db.String(50))
    range_start = db.Column(db.Float)
    range_end = db.Column(db.Float)
    commission_percentage = db.Column(db.Float)
    fixed_cost = db.Column(db.Float)

class ReputationDiscount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    platform_id = db.Column(db.Integer, db.ForeignKey('platform.id'))
    reputation = db.Column(db.String(50))
    discount_percentage = db.Column(db.Float)

class AdditionalFee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    platform_id = db.Column(db.Integer, db.ForeignKey('platform.id'))
    type = db.Column(db.String(50))
    fee_percentage = db.Column(db.Float)
    fixed_value = db.Column(db.Float)

# Fim das taxas

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    subcategories = db.relationship('SubCategory', backref='category', lazy='dynamic')

class SubCategory(db.Model):
    __tablename__ = 'sub_category'  
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    ads = db.relationship('Ad', backref='sub_category', lazy='dynamic')
    package_length = db.Column(db.Float) 
    package_width = db.Column(db.Float) 
    package_height = db.Column(db.Float) 
    unit_weight = db.Column(db.Float) 

ad_sale = db.Table('ad_sale',
    db.Column('ad_id', db.Integer, db.ForeignKey('ad.id'), primary_key=True),
    db.Column('sale_id', db.Integer, db.ForeignKey('sale.id'), primary_key=True)
)

class Ad(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(500))
    subcategory_id = db.Column(db.Integer, db.ForeignKey('sub_category.id', name='fk_ad_subcategory'))
    price = db.Column(db.Float)
    date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    code = db.Column(db.String(50), unique=True)
    platform_id = db.Column(db.Integer, db.ForeignKey('platform.id'))
    platform = db.relationship('Platform', backref='ads')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    sales = db.relationship('Sale', secondary=ad_sale, back_populates='ads')

class Sale(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    total_value = db.Column(db.Float)
    platform_id = db.Column(db.Integer, db.ForeignKey('platform.id'))
    code = db.Column(db.String(50))
    customer_name = db.Column(db.String(100))
    ads = db.relationship('Ad', secondary=ad_sale, back_populates='sales')
    def add_from_ad(self, ad):
        self.title = ad.title
        self.description = ad.description
        self.total_value = ad.price
        self.platform_id = ad.platform_id
        self.code = ad.code
        self.ads.append(ad)

    @property
    def categories(self):
        return [ad.category for ad in self.ads]

    @property
    def subcategories(self):
        return [ad.subcategory for ad in self.ads]