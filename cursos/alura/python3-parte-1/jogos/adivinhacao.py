import random

def jogar():
    print("**************************************")
    print("Seja bem vindo ao jogo de adivinhação!")
    print("**************************************")

    numero_secreto = random.randrange(1, 101)
    tentativas = 15
    rodadas = 1
    acertou = False
    pontos = 1000

    print("Selecione o nível de difículdade")
    dificuldade = int(input("Fácil (1) Médio (2) Difícil (3): "))

    if(dificuldade == 2):
        tentativas = 10
    elif(dificuldade == 3):
        tentativas = 5

    while(rodadas <= tentativas and acertou == False):
        print("Tentativa {} de {}".format(rodadas, tentativas))
        chute = int(input("Digite um número entre 1 e 100: "))

        if(chute < 1 or chute > 100):
            print("O número obrigatóriamente deve estar entre 1 e 100. Digite novamente...")
            continue

        acertou = numero_secreto == chute
        if(acertou):
            print("\nPARABÉNS, você acertou o número secreto {} =D !!!".format(numero_secreto))
            print(">>> Você fez {} pontos <<<\n".format(pontos))
            break
        else:
            comparacao = ""
            if(chute < numero_secreto):
                comparacao = "menor"
            elif(chute > numero_secreto):
                comparacao = "maior"

            pontos = pontos - abs(numero_secreto - chute)

            print("Você errou :c ... Seu chute foi {} que o número secreto!\n".format(comparacao))

        rodadas = rodadas + 1

    if(acertou == False):
      print(">>> O número secreto era {} <<<\n".format(numero_secreto))

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()