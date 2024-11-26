import mysql.connector
from mysql.connector import Error


class AppBD:
    def __init__(self):
        print("Inicializando o AppBD...")

    def abrirConexao(self):
        """Estabelece a conexão com o banco de dados."""
        try:
            self.connection = mysql.connector.connect(
                host="127.0.0.1",
                port=3306,  # Porta padrão do MySQL no XAMPP
                user="root",
                password="",  # Senha padrão do XAMPP
                database="loja",
            )
            if self.connection.is_connected():
                print("[DEBUG] Conexão com MySQL estabelecida.")
        except Error as e:
            print(f"[ERRO] Falha ao conectar ao MySQL: {e}")
            self.connection = None

    def selecionarDados(self):
        """Seleciona todos os dados da tabela Produto."""
        try:
            self.abrirConexao()
            if not self.connection:
                print("[DEBUG] Conexão falhou. Operação abortada.")
                return

            cursor = self.connection.cursor()
            print("[DEBUG] Executando SELECT * FROM Produto")
            cursor.execute("SELECT * FROM Produto")
            registros = cursor.fetchall()
            print(f"[DEBUG] Registros retornados: {registros}")
            return registros
        except Error as e:
            print(f"[ERRO] Erro ao selecionar dados: {e}")
        finally:
            if self.connection:
                self.connection.close()
                print("[DEBUG] Conexão fechada.")

    def inserirDados(self, codigo, nome, preco):
        """Insere um novo produto na tabela."""
        try:
            self.abrirConexao()
            if not self.connection:
                print("[DEBUG] Conexão falhou. Operação abortada.")
                return

            cursor = self.connection.cursor()
            query = "INSERT INTO Produto (Codigo, Nome, Preco) VALUES (%s, %s, %s)"
            valores = (codigo, nome, preco)
            print(f"[DEBUG] Executando: {query} com valores {valores}")
            cursor.execute(query, valores)
            self.connection.commit()
            print(f"[DEBUG] {cursor.rowcount} registro(s) inserido(s).")
        except Error as e:
            print(f"[ERRO] Erro ao inserir dados: {e}")
        finally:
            if self.connection:
                self.connection.close()
                print("[DEBUG] Conexão fechada.")

    def atualizarDados(self, codigo, nome, preco):
        """Atualiza os dados de um produto existente."""
        try:
            self.abrirConexao()
            if not self.connection:
                print("[DEBUG] Conexão falhou. Operação abortada.")
                return

            cursor = self.connection.cursor()
            query = "UPDATE Produto SET Nome = %s, Preco = %s WHERE Codigo = %s"
            valores = (nome, preco, codigo)
            print(f"[DEBUG] Executando: {query} com valores {valores}")
            cursor.execute(query, valores)
            self.connection.commit()
            print(f"[DEBUG] {cursor.rowcount} registro(s) atualizado(s).")
        except Error as e:
            print(f"[ERRO] Erro ao atualizar dados: {e}")
        finally:
            if self.connection:
                self.connection.close()
                print("[DEBUG] Conexão fechada.")

    def excluirDados(self, codigo):
        """Exclui um produto da tabela."""
        try:
            self.abrirConexao()
            if not self.connection:
                print("[DEBUG] Conexão falhou. Operação abortada.")
                return

            cursor = self.connection.cursor()
            query = "DELETE FROM Produto WHERE Codigo = %s"
            valores = (codigo,)
            print(f"[DEBUG] Executando: {query} com valores {valores}")
            cursor.execute(query, valores)
            self.connection.commit()
            print(f"[DEBUG] {cursor.rowcount} registro(s) excluído(s).")
        except Error as e:
            print(f"[ERRO] Erro ao excluir dados: {e}")
        finally:
            if self.connection:
                self.connection.close()
                print("[DEBUG] Conexão fechada.")


'''# Exemplo de uso:
app = AppBD()
app.inserirDados(1, "Produto A", 25.50)
app.selecionarDados()
app.atualizarDados(1, "Produto A Atualizado", 30.75)
app.selecionarDados()
app.excluirDados(1)
app.selecionarDados()'''
