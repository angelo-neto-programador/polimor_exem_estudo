from animal import Animal

class Reptil(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def faz_som(self):
        print(f"{self.nome} emite um som rastejante...")

    def mover(self):
        print(f"{self.nome} está rastejando.")