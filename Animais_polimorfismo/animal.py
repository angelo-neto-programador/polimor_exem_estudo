class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def envelhecer(self):
        self.idade += 1
        print(f"{self.nome} envelheceu! Agora tem {self.idade} anos.")


    def faz_som(self):
        print("f{self.nome} emite um som desconhecido.")

    def mover(self):
        print(f"{self.nome} está se movendo.")

    def testar(self):
        print(f"\nOlhando {self.__class__.__name__}:")
        self.faz_som
        self.mover()

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}, Idade: {self.idade} anos")