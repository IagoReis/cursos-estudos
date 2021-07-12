import adivinhacao
import forca

def escolher():
    print("**************************************")
    print("** Seja bem vindo ao jogos Python! ***")
    print("**************************************")

    print("Escolha o seu jogo")
    jogo = int(input("(1) Adivinhação (2) Forca: "))
    print("")

    if(jogo == 1):
        adivinhacao.jogar()
    elif(jogo == 2):
        forca.jogar()

if(__name__ == "__main__"):
    escolher()