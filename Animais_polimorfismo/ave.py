from animal import Animal

class Ave(Animal):
    def __init__(self, nome):
        super().__init__(nome)


    def faz_som(self):
        print(f"{self.nome} carnta ou pia alegremente.")

    def mover(self):
        print(f"{self.nome} está voando.")