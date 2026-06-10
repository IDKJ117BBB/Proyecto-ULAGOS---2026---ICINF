import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#configuración de la app

app = Flask(__name__, template_folder='templates')

dbdir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(dbdir, 'database.db')#Configuracion de los motores
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

