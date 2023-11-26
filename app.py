from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def connect_db():
    return sqlite3.connect('processos.db')

def init_db():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, email TEXT, senha TEXT)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS eventos (id INTEGER PRIMARY KEY AUTOINCREMENT, data TEXT, hora TEXT, evento TEXT, usuario_id INTEGER, FOREIGN KEY(usuario_id) REFERENCES usuarios(id))''')
    conn.commit()
    conn.close()

init_db()  # Cria a tabela se ela não existir

@app.route('/listausuarios', methods=['GET'])
def index():
    if request.method == 'GET':
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios")
        users = cursor.fetchall()
        conn.close()
        return render_template('listausuarios.html', users=users)

@app.route('/cadusuario', methods=['GET', 'POST'])
def cadusuario():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios (email, senha) VALUES (?, ?)", (email, senha))
        conn.commit()
        conn.close()

        return redirect(url_for('index'))

    return render_template('cadusuario.html')

if __name__ == '__main__':
    app.run(debug=True)

