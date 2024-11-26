from project.models.Entidade import Entidade

class Cliente(Entidade):
    def __init__(self, id, nome:str, email:str, telefone:str):
        super().__init__(id)
        self.nome = nome
        self.email = email
        self.telefone = telefone
        
        
    def salvar(self):
        return(f"Cliente: {self.nome} salvo com sucesso!")
    
    def excluir(self):
        certeza = str(input(f"Você tem certeza que deseja excluir o usuario: {self.nome}? [ SIM / NÃO]")).upper().strip()
        if certeza == "SIM":
            return(f"Cliente: {self.nome} excluido com sucesso!")
        else:
            print(f"Exclusão cancelada!")
        
        
    def atualizarDados(self, nome:None, email:None, telefone:None):
        if nome:
            self.nome = nome
        if email:
            self.email
        if telefone:
            self.telefone
        print(f"Dados de {self.nome} atualizados com sucesso!")
        
