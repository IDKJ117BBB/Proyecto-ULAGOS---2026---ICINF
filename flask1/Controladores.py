from flask import render_template, redirect, url_for, request
from modelos import Modelos
from app import app

@app.route('/')
def index():
    # ventana principal o login
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    # prototipo de validación de datos
    rut = request.form.get('rut')
    password = request.form.get('password')
    
    # aquí la verificacion, la lógica está en Modelos.py
    if Modelos.User.get(rut, password):
        return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    # ventana de selección: almuerzos o abarrotes
    return render_template('dashboard.html')

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
        # Prototipo: model.User.agregar_usuario()
        return redirect(url_for('dashboard'))
    return render_template('admin_user.html')
""""
if __name__ == '__main__':
    with app.app_context():
        Modelos.db.create_all() # samu, esto crea la base de datos si no existe. En caso de... edit 31/06
    app.run(debug=True)"""

# edit 01/06, y me faltan algunas cositas pero esto avancé, posta me sirvió mucho tu forma de programar, de hecho, fue una gran guia :)
