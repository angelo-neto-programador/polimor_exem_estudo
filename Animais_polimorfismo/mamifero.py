from animal import Animal

class Mamifero(Animal):
    def __ini__(self, nome):
        super().__init__(nome)

    def faz_som(self):
        print(f"{self.nome} emite um som caracteristico de mamífero.")

    def mover(self):
        print(f"{self.nome} está caminhando.")