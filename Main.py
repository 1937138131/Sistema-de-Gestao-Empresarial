from project.models.Entidade import Entidade
from project.models.Cliente import Cliente
from project.models.Produto import Produto
from project.models.Vendas import Venda

produto1 = Produto(nome="Camiseta", preco=49.99, quantidade_Estoque=10)
produto2 = Produto(nome="Calça Jeans", preco=99.99, quantidade_Estoque=5)

cliente1 = Cliente(id=1, nome="João Silva", email="joao@gmail.com", telefone="123456789")

venda1 = Venda(id=1, cliente=cliente1)

venda1.adicionar_Produto(produto1)
venda1.adicionar_Produto(produto2)

print(venda1.calcular_Total())
venda1.listar_Produtos()
print(venda1.salvar())