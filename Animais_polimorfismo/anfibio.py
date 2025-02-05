from animal import Animal

class Anfibio(Animal):
    def __ini__(self, nome):
        super().__init__(nome)

    def faz_som(self):
        print(f"{self.nome} faz um coaxar característico.")

    def mover(self):
        print(f"{self.nome} está saltando e nadando.")