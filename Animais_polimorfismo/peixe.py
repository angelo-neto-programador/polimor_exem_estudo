from animal import Animal

class Peixe(Animal):
    def __ini__(self, nome):
        super().__init__(nome)


    def faz_som(self):
        print(f"{self.nome} nao faz som, mas borbulha na água.")

    def mover(self):
        print(f"{self.nome} está nadando")