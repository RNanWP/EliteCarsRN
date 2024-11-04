from db.connection import conectar
import mysql.connector

def inserir_cliente(nome, cpf, rg):
    conn = conectar()
    cursor = conn.cursor()
    sql = "INSERT INTO clientes (nome, cpf, rg) VALUES (%s, %s, %s)"
    valores = (nome, cpf, rg)
    
    try:
        cursor.execute(sql, valores)
        conn.commit()
        print("Cliente inserido com sucesso!")
    except mysql.connector.Error as err:
        print(f"Erro ao inserir cliente: {err}")
    finally:
        cursor.close()
        conn.close()

def obter_clientes():
    conn = conectar()
    cursor = conn.cursor()
    sql = "SELECT * FROM clientes"
    
    try:
        cursor.execute(sql)
        clientes = cursor.fetchall()
        return clientes
    except mysql.connector.Error as err:
        print(f"Erro ao obter clientes: {err}")
        return []
    finally:
        cursor.close()
        conn.close()

def atualizar_cliente(id, novo_nome, novo_cpf, novo_rg):
    conn = conectar()
    cursor = conn.cursor()
    sql = "UPDATE clientes SET nome = %s, cpf = %s, rg = %s WHERE id = %s"
    valores = (novo_nome, novo_cpf, novo_rg, id)
    
    try:
        cursor.execute(sql, valores)
        conn.commit()
        print("Cliente atualizado com sucesso!")
    except mysql.connector.Error as err:
        print(f"Erro ao atualizar cliente: {err}")
    finally:
        cursor.close()
        conn.close()

def deletar_cliente(id):
    conexao = conectar()
    cursor = conexao.cursor()
    
    try:
        # Verifique se há vendas relacionadas antes de deletar
        cursor.execute("SELECT COUNT(*) FROM vendas WHERE cliente_id = %s", (id,))
        count = cursor.fetchone()[0]

        if count > 0:
            print("Não é possível deletar o cliente, pois ele possui vendas relacionadas.")
            return

        sql = "DELETE FROM clientes WHERE id = %s"
        cursor.execute(sql, (id,))
        conexao.commit()
        print("Cliente deletado com sucesso!")
    except mysql.connector.Error as err:
        print(f"Erro ao deletar cliente: {err}")
    finally:
        cursor.close()
        conexao.close()
