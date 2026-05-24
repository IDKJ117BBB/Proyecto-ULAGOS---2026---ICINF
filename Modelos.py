from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__) #__name__ hace referencia al archivo en el q estamos
app.config["SQLALCHEMY_DATABASE_URL"] = "sqlite:///Maindatabase.db"#Configuracion de los motores

#inicializar SQLalchemy
databaseCAFETERIA = SQLAlchemy()#Instanciar un objeto database
databaseCAFETERIA.init_app(app)

"""class base(DeclarativeBase):
    pass
"""
#Cada modelo es una tabla en la base de datos

#Clase para usuario y admin
class User(databaseCAFETERIA.Model):
    id= databaseCAFETERIA.Column(databaseCAFETERIA.Integer, primary_key=True)
    username = databaseCAFETERIA.Column(databaseCAFETERIA.String(60), nullable=False)
    password = databaseCAFETERIA.Column(databaseCAFETERIA.String(30), nullable=False)
    role = databaseCAFETERIA.Column(databaseCAFETERIA.Boolean, nullable=False, default=False)#rol, True=admin, False=cliente
    #Añadir métodos que usen los atributos de user
    #Tales como iniciar sesión, realizar reserva
    def user_verification(self, passwordIn): #PasswordIn es la contraseña que le pasaremos desde la ventana
        """Logica aqui"""
        return
    def agregar_usuario(self): #Se supone solo el admin debe tener acceso a esto
        if self.role==1:
            #Crea un usuario y lo agrega
            #Aqui va lo que puede hacer el admin (en este caso agregar user)
            return
    def makereservation(self, menuIds, comidaId):
        return
    
#Clase para almuerzo (item)
class Lunch(databaseCAFETERIA.Model):
    id = databaseCAFETERIA.Column(databaseCAFETERIA.Integer, primary_key=True)
    name = databaseCAFETERIA.Column(databaseCAFETERIA.String(80), nullable=False)
    quantity = databaseCAFETERIA.Column(databaseCAFETERIA.Integer)#Cantidad de esa comida en especifico
    #description = db.Column(db.Text)
    #Métodos para enlazarse con un Menu
    def addtomenu(self, menuID):#Relacionar con la tabla intermedia
        return
    #Métodos para borrar o editar alguna comida o agregar
    
#Clase para Menu (tiene varios almuerzos)
class Menu(databaseCAFETERIA.Model): #Falta crear tabla intermedia entre Food y Menu (N a N)
    id = databaseCAFETERIA.Column(databaseCAFETERIA.Integer, primary_key=True)
    day = databaseCAFETERIA.Column(databaseCAFETERIA.String(20), nullable=False)
    #time = db.Column(db.String(20), nullable=False)
    #enu = db.Column(db.Text, nullable=False)
    #foods = db.relationship('Food', backref='menu', lazy=True, cascade='all, delete-orphan')
    
#Clase para abarrotes
class groceries(databaseCAFETERIA.Model):
    id = databaseCAFETERIA.Column()

#######TABLAS RESERVAS###########
class Reservation_lunch(databaseCAFETERIA.Model): # N a 1 con User y 1 a 1 con menú
    id = databaseCAFETERIA.Column(databaseCAFETERIA.Integer, primary_key=True)
     
class Reservation_groceries(databaseCAFETERIA.Model):
    id=None
    
########TABLAS INTERMEDIAS########

#Un menu puede tener varios almuerzos y un almuerzo puede aparecer en multiples menus
class Lunch_Menu(databaseCAFETERIA.Model):
    id=None