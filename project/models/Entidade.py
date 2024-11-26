from abc import ABC, abstractmethod

class Entidade(ABC):
    def __init__(self, id:int):
        self.id = id
        
    @abstractmethod
    def salvar(self):
        pass
    
    @abstractmethod
    def excluir(self):
        pass
    
    