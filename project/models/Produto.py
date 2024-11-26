class Produto():
    def __init__(self, nome:str, preco:float, quantidade_Estoque:int):
        self.nome = nome
        self.preco = preco
        self.quantidade_Estoque = quantidade_Estoque
        
    def salvar(self):
        print(f"Produto {self.nome} salvo com sucesso!")
        
    def excluir(self):
        certeza = input(f"Você tem certeza que deseja excluir o produto: {self.nome}? [ SIM / NÃO] ").upper().strip()
        while certeza not in ["SIM", "NÃO"]:
            certeza = input("Resposta inválida! Digite [SIM] ou [NÃO]: ").upper().strip()
        
        if certeza == "SIM":
            return f"Produto: {self.nome} excluído com sucesso!"
        else:
            return "Exclusão cancelada!"
        
    def atualizar_Estoque(self, quantidade: int):
        if quantidade == 0:
            print(f"A quantidade para atualização não pode ser zero!")
        elif quantidade > 0:
            self.quantidade_Estoque += quantidade
            print(f"Estoque de {self.nome} aumentado em {quantidade}. Novo estoque: {self.quantidade_Estoque}")
        elif quantidade < 0 and self.quantidade_Estoque + quantidade >= 0:
            self.quantidade_Estoque += quantidade
            print(f"Estoque de {self.nome} diminuído em {-quantidade}. Novo estoque: {self.quantidade_Estoque}")
        else:
            print(f"Estoque insuficiente para diminuir em {abs(quantidade)} unidades!")
