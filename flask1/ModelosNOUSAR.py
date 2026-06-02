"""from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# esto lo corregí por: SQLALCHEMY_DATABASE_URI (era URL básicamente)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Maindatabase.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy()
db.init_app(app)

# --- MODELOS B) --- edit 31/05, soy un genio, lo logré

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), nullable=False)
    password = db.Column(db.String(30), nullable=False)
    role = db.Column(db.Boolean, nullable=False, default=False)

class Lunch(db.Model):
    __tablename__ = 'lunch'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    quantity = db.Column(db.Integer)

class Menu(db.Model):
    __tablename__ = 'menu'
    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.String(20), nullable=False)

class Lunch_Menu(db.Model):
    __tablename__ = 'lunch_menu'
    id = db.Column(db.Integer, primary_key=True)
    lunch_id = db.Column(db.Integer, db.ForeignKey('lunch.id'), nullable=False)
    menu_id = db.Column(db.Integer, db.ForeignKey('menu.id'), nullable=False)

class Groceries(db.Model):
    __tablename__ = 'groceries'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    quantity = db.Column(db.Integer)

class Reservation_Lunch(db.Model):
    __tablename__ = 'reservation_lunch'
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    lunch_menu_id = db.Column(db.Integer, db.ForeignKey('lunch_menu.id'), nullable=False)
    description = db.Column(db.String(200), nullable=True)

class Reservation_Groceries(db.Model):
    __tablename__ = 'reservation_groceries'
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    groceries_id = db.Column(db.Integer, db.ForeignKey('groceries.id'), nullable=False)
    description = db.Column(db.String(200), nullable=True)

#01/06 samu goat goat goat"""
