from flask import render_template, redirect, url_for, request

from .configr import app
from . import modelos

@app.route('/')
def index():
    # ventana principal o login
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    # prototipo de validación de datos
    #Ahora debe tener validación para aceptar la forma xxxxxxxx-x
    rut = request.form.get('rut')
    #La contraseña tambien tiene que tener restricciones, no carácteres especiales
    password = request.form.get('password')
    
    # aquí la verificacion, la lógica está en Modelos.py
    if modelos.User.get(rut, password):
        return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    # ventana de selección: almuerzos o snacks
    return render_template('index.html')

@app.route('/reservar_almuerzo', methods=['GET', 'POST'])
def reservar_almuerzo():
    if request.method == 'POST':
        # prototipo para guardar reserva de almuerzo... escribiendo prototipo, me acordé del prototype 2, juegazo.
        # model.Reservation_Lunch.add(...)
        return redirect(url_for('dashboard'))
    return render_template('reservar_almuerzo.html')

@app.route('/comprar_abarrotes', methods=['GET', 'POST'])
def comprar_abarrotes():
    if request.method == 'POST':
        # prototipo para guardar reserva de abarrotes
        return redirect(url_for('dashboard'))
    return render_template('comprar_abarrotes.html')

@app.route('/admin/agregar_usuario', methods=['GET', 'POST'])
def admin_agregar_usuario():
    # Solo accesible si role == True (Admin)
    if request.method == 'POST':
        rut = request.form.get('rut')
        username = request.form.get('nombre')
        password = request.form.get('password')
        return redirect(url_for('dashboard'))
    return render_template('admin_user.html')


