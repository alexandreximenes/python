
def jogar():
    print("********************************* Bem vindo no jogo da forca *********************************")
    nao_enforcou = False
    nao_acertou = False


    palavra_secreta = 'banana'

    while(not nao_enforcou and not nao_acertou):
        chute = input("Informe uma letra ")
        if chute != '':
            # palavra_secreta.find()
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    print("Encontrei a letra {} na posição {}".format(letra, index))
                index += 1




    print("******************************************** Fim do jogo *******************************************")

if(__name__ == "__main__"):
    jogar()