from peixe import Peixe
from reptil import Reptil
from anfibio import Anfibio
from ave import Ave
from mamifero import Mamifero

def testar_animal(animal):
    print("\nTestando animal:")
    animal.exibir_informacoes()
    animal.envelhecer()
    animal.faz_som()
    animal.mover()

if __name__ == "__main__":
    leao = Mamifero("Leão", 5)
    testar_animal(leao)

    tubarao = Peixe("Tubarão", 3)
    testar_animal(tubarao)

    aguia = Ave("Águia", 4)
    testar_animal(aguia)

    cobra = Reptil("Cobra", 2)
    testar_animal(cobra)

    sapo = Anfibio("Sapo", 2)
    testar_animal(sapo)
