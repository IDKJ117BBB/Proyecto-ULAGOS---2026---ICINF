from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
#from flask1 import Controladores

app=Flask(__name__) #__name__ hace referencia al archivo en el q estamos

dbdir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(dbdir, 'database.db')#Configuracion de los motores

#inicializar SQLalchemy
db = SQLAlchemy()#Instanciar un objeto database
db.init_app(app)

#Cada modelo es una tabla en la base de datos

#Clase para usuario y admin
class User(db.Model):
    __tablename__='user'
    rut = db.Column(db.Integer, primary_key=True, nullable=False)#numero sin puntos ni espacios ni dígito verificador, luego configurar esto
    username = db.Column(db.String(70), nullable=False)
    password = db.Column(db.String(30), nullable=False)
    role = db.Column(db.Boolean, nullable=False, default=False)#True=admin, False=cliente

    @classmethod
    def get(cls,rut,password):
       user = cls.query.filter_by(rut=rut).first() #Para obtener la fila donde al rut sea igual al ingresado
       if user==True and user.password==password: #comprobar si el rut existe y si la contraseña en la base datos es igual a la ingresada
           return user
       return None
       
    def makereservation(self, tiporeserva):
            #Funcion para crear un enlace con la id de este usuario
            return
         
    def agregar_usuario(self): #Se supone solo el admin debe tener acceso a esto
        if self.role==1:
            #Crea un usuario y lo agrega
            #Aqui va lo que puede hacer el admin (en este caso agregar user)
            return
        

    
#Clase para almuerzo (item)
class Lunch(db.Model):
    __tablename__='lunch'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    quantity = db.Column(db.Integer)#Cantidad de esa comida en especifico
    description = db.Column(db.String(200), nullable=True)
    #Métodos para enlazarse con un Menu
    def addtomenu(self, menuID):#Relacionar con la tabla intermedia
        return
    #Métodos para borrar o editar alguna comida o agregar
    
#Clase para Menu (tiene varios almuerzos)
class Menu(db.Model):
    __tablename__='menu'
    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.String(20), nullable=False)
    #time = db.Column(db.String(20), nullable=False)
    #enu = db.Column(db.Text, nullable=False)
    #foods = db.relationship('Food', backref='menu', lazy=True, cascade='all, delete-orphan')
    
#Clase para abarrotes
class groceries(db.Model):
    __tablename__='groceries'
    id = db.Column()
    name = db.Column()
    quantity = db.Column(db.Integer)#Cantidad de producto en específico
    description = db.Column(db.String(200), nullable=True)

#######TABLAS RESERVAS###########
class Reservation_lunch(db.Model): # N a 1 con User y 1 a 1 con menú
    __tablename__='reservation_lunch'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    lunch_menu_id = db.Column(db.Integer, db.ForeignKey())
     
class Reservation_groceries(db.Model):
    __tablename__='reservation_groceries'
    id=db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=True)


########TABLAS INTERMEDIAS########
#Un menu puede tener varios almuerzos y un almuerzo puede aparecer en multiples menus
class Lunch_Menu(db.Model):
    __tablename__='lunch_menu'
    id = db.Column(db.Integer, primary_key=True)
    lunch_id = db.Column(db.Integer, db.ForeignKey('lunch.id'), nullable=False)
    menu_id = db.Column(db.Integer, db.ForeignKey('menu.id'), nullable=False)

