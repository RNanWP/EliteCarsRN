from db.connection import conectar

def inserir_venda(data_venda, valor_total, cliente_id, modelo_veiculo):
    conn = conectar()
    cursor = conn.cursor()
    sql = "INSERT INTO vendas (data_venda, valor_total, cliente_id, modelo_veiculo) VALUES (%s, %s, %s, %s)"
    valores = (data_venda, valor_total, cliente_id, modelo_veiculo)
    cursor.execute(sql, valores)
    conn.commit()
    print("Venda inserida com sucesso!")
    cursor.close()
    conn.close()

def obter_vendas():
    conn = conectar()
    cursor = conn.cursor()
    sql = "SELECT * FROM vendas"
    cursor.execute(sql)
    vendas = cursor.fetchall()
    cursor.close()
    conn.close()
    return vendas

def atualizar_venda(id, nova_data_venda, novo_valor_total, novo_cliente_id, novo_modelo_veiculo):
    conn = conectar()
    cursor = conn.cursor()
    sql = "UPDATE vendas SET data_venda = %s, valor_total = %s, cliente_id = %s, modelo_veiculo = %s WHERE id = %s"
    valores = (nova_data_venda, novo_valor_total, novo_cliente_id, novo_modelo_veiculo, id)
    cursor.execute(sql, valores)
    conn.commit()
    print("Venda atualizada com sucesso!")
    cursor.close()
    conn.close()

def deletar_venda(id):
    conn = conectar()
    cursor = conn.cursor()
    sql = "DELETE FROM vendas WHERE id = %s"
    cursor.execute(sql, (id,))
    conn.commit()
    print("Venda deletada com sucesso!")
    cursor.close()
    conn.close()
