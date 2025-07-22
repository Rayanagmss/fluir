import sqlite3

def conectar():
    """
    Cria conexão com o banco SQLite 'pedidos.db'.
    Usa row_factory para retornar resultados acessíveis por nome da coluna.
    """
    conn = sqlite3.connect('pedidos.db')
    conn.row_factory = sqlite3.Row
    return conn

def criar_tabela():
    """
    Cria a tabela 'pedidos' se não existir ainda.
    Campos: id, cpf, endereço, status e data do pedido.
    """
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pedidos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cpf TEXT NOT NULL,
            bairro TEXT NOT NULL,
            rua TEXT NOT NULL,
            cidade TEXT NOT NULL,
            estado TEXT NOT NULL,
            numero TEXT NOT NULL,
            complemento TEXT,
            status TEXT NOT NULL,
            data TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def inserir_pedido(pedido):
    """
    Insere um novo pedido no banco.
    Recebe um dicionário com os dados do pedido.
    """
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO pedidos (cpf, bairro, rua, cidade, estado, numero, complemento, status, data)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        pedido['cpf'], pedido['bairro'], pedido['rua'], pedido['cidade'], pedido['estado'],
        pedido['numero'], pedido.get('complemento'), pedido['status'], pedido['data']
    ))
    conn.commit()
    conn.close()

def buscar_pedido_por_cpf(cpf):
    """
    Busca o primeiro pedido registrado no banco pelo CPF.
    Retorna None se não encontrar.
    """
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM pedidos WHERE cpf = ?', (cpf,))
    pedido = cursor.fetchone()
    conn.close()
    return pedido
