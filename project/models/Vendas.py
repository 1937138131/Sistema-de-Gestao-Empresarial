from project.models.Cliente import Cliente

class Venda:
    def __init__(self, id, cliente: Cliente, produtos=None):
        self.id = id
        self.cliente = cliente
        self.produtos = produtos if produtos is not None else []
        self.total = 0.0
        
    def salvar(self):
        return f"Venda de {self.cliente.nome} salva com sucesso!"
    
    def excluir(self):
        certeza = input(f"Você tem certeza que deseja excluir a venda de {self.cliente.nome}? [ SIM / NÃO] ").upper().strip()
        while certeza not in ["SIM", "NÃO"]:
            certeza = input("Resposta inválida! Digite [SIM] ou [NÃO]: ").upper().strip()
        
        if certeza == "SIM":
            return f"Venda de {self.cliente.nome} excluída com sucesso!"
        else:
            return "Exclusão cancelada!"
    
    def calcular_Total(self):
        self.total = sum([produto.preco for produto in self.produtos])
        return f"O total da venda é: R${self.total:.2f}"

    def adicionar_Produto(self, produto):
        self.produtos.append(produto)
        print(f"Produto {produto.nome} adicionado à venda.")
    
    def listar_Produtos(self):
        if not self.produtos:
            print("Nenhum produto na venda.")
        for produto in self.produtos:
            print(f"- {produto.nome} - R${produto.preco:.2f}")
