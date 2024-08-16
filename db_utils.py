import sqlite3

def conectar_banco():
    conn = sqlite3.connect('usuarios.db')
    return conn

def validar_login(usuario, senha):
    conn = conectar_banco()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM usuarios WHERE usuario = ? AND senha = ?", (usuario, senha))
    resultado = cursor.fetchone()

    conn.close()
    return resultado is not None