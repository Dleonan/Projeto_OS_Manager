import sqlite3

# Conecta ao banco de dados (ou cria se não existir)
conn = sqlite3.connect('usuarios.db')

# Cria um cursor
cursor = conn.cursor()

# Cria a tabela de usuários (se ainda não existir)
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario TEXT NOT NULL,
    senha TEXT NOT NULL
)
''')

# Exemplo: Inserindo um usuário
cursor.execute('''
INSERT INTO usuarios (usuario, senha) VALUES ('admin', '1234')
''')

# Salva as mudanças e fecha a conexão
conn.commit()
conn.close()
