from animal import Animal

class Anfibio(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def faz_som(self):
        print(f"{self.nome} faz um coaxar característico.")

    def mover(self):
        print(f"{self.nome} está saltando e nadando.")