from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Necesario para usar flash messages

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    confirm_password = request.form['confirm_password']
    
    # Verificar que las contraseñas coincidan
    if password != confirm_password:
        flash('Las contraseñas no coinciden', 'error')
        return redirect(url_for('index'))

    # Validar campos vacíos
    if not name or not email or not password:
        flash('Todos los campos son obligatorios', 'error')
        return redirect(url_for('index'))

    # Verificar formato del correo electrónico
    if '@' not in email:
        flash('Correo electrónico inválido', 'error')
        return redirect(url_for('index'))

    # Guardar en la base de datos
    try:
        save_to_database(name, email, password)
        flash('Registro exitoso', 'success')
    except Exception as e:
        flash(f'Error al guardar en la base de datos: {str(e)}', 'error')

    return redirect(url_for('index'))

def save_to_database(name, email, password):
    config = {
        'user': 'root',
        'password': 'Enrique154',
        'host': '127.0.0.1',
        'database': 'python',
    }
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",(name, email, password))
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == '__main__':
    app.run(debug=True)