class Animal:
    def __init__(self, nome):
        self.nome = nome

    def faz_som(self):
        print("f{self.nome} emite um som desconhecido.")

    def mover(self):
        print(f"{self.nome} está se movendo.")

    def testar(self):
        print(f"\nOlhando {self.__class__.__name__}:")
        self.faz_som
        self.mover()