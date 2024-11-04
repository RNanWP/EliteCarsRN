from models.cliente import inserir_cliente, obter_clientes, atualizar_cliente, deletar_cliente
from models.venda import inserir_venda, obter_vendas, atualizar_venda, deletar_venda

# Clientes
print("== Gerenciamento de Clientes ==")
inserir_cliente("João Mac", "12345678902", "1239567")
clientes = obter_clientes()
for cliente in clientes:
    print(cliente)
atualizar_cliente(1, "Judas Alberto", "12345678904", "1234767")
deletar_cliente(1)

# Vendas
print("\n== Gerenciamento de Vendas ==")
inserir_venda("2024-11-01", 350000.00, 1, "Mercedes-Benz S-Class")
vendas = obter_vendas()
for venda in vendas:
    print(venda)
atualizar_venda(1, "2024-11-01", 400000.00, 1, "BMW Série 7")
deletar_venda(1)
