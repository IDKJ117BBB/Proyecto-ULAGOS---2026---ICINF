import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#configuración de la app

app = Flask(__name__)

dbdir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(dbdir, 'database.db')#Configuracion de los motores

db = SQLAlchemy(app)
