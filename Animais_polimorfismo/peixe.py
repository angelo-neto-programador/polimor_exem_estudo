from animal import Animal

class Peixe(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)


    def faz_som(self):
        print(f"{self.nome} nao faz som, mas borbulha na água.")

    def mover(self):
        print(f"{self.nome} está nadando")