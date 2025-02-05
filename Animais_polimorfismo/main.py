from peixe import Peixe
from reptil import Reptil
from anfibio import Anfibio
from ave import Ave
from mamifero import Mamifero

if __name__ == "__main__":
    animais = [
        Peixe("Nemo"),
        Reptil("Cobra"),
        Anfibio("Sapo"),
        Ave("Papagaio"),
        Mamifero("Leão")
    ]

    for animal in animais:
        animal.testar()
