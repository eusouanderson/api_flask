from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Função para conectar ao banco de dados em memória
def conectar_bd():
    conn = sqlite3.connect(':memory:')  # Banco de dados em memória
    conn.row_factory = sqlite3.Row  # Para retornar os dados como dicionário
    return conn

# Criar a tabela no banco de dados
def criar_tabela():
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE Produto (
            Codigo INTEGER PRIMARY KEY,
            Nome TEXT NOT NULL,
            Preco REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Rota para listar todos os produtos
@app.route('/produtos', methods=['GET'])
def listar_produtos():
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Produto")
    produtos = cursor.fetchall()
    conn.close()
    return jsonify([dict(produto) for produto in produtos])

# Rota para adicionar um novo produto
@app.route('/produtos', methods=['POST'])
def adicionar_produto():
    novo_produto = request.get_json()
    codigo = novo_produto['Codigo']
    nome = novo_produto['Nome']
    preco = novo_produto['Preco']
    
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Produto (Codigo, Nome, Preco) VALUES (?, ?, ?)", (codigo, nome, preco))
    conn.commit()
    conn.close()
    return jsonify({"message": "Produto adicionado com sucesso!"}), 201

# Rota para atualizar um produto
@app.route('/produtos/<int:codigo>', methods=['PUT'])
def atualizar_produto(codigo):
    produto_atualizado = request.get_json()
    nome = produto_atualizado['Nome']
    preco = produto_atualizado['Preco']
    
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("UPDATE Produto SET Nome = ?, Preco = ? WHERE Codigo = ?", (nome, preco, codigo))
    conn.commit()
    conn.close()
    return jsonify({"message": "Produto atualizado com sucesso!"})

# Rota para excluir um produto
@app.route('/produtos/<int:codigo>', methods=['DELETE'])
def excluir_produto(codigo):
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Produto WHERE Codigo = ?", (codigo,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Produto excluído com sucesso!"})

if __name__ == '__main__':
    criar_tabela()  # Criar a tabela ao iniciar a aplicação
    app.run(debug=True)
