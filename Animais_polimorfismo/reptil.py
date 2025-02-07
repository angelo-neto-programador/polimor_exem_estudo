from animal import Animal

class Reptil(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def faz_som(self):
        print(f"{self.nome} emite um som rastejante...")

    def mover(self):
        print(f"{self.nome} está rastejando.")