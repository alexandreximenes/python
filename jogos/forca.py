
def jogar():
    print("********************************* Bem vindo no jogo da forca *********************************")
    nao_enforcou = False
    nao_acertou = False

    erros = 0
    palavra_secreta = 'abacaxi'.upper()
    letras_acertadas = ["_" for letra in palavra_secreta]
    total_tentativas = len(palavra_secreta)

    print(letras_acertadas)

    while(not nao_enforcou and not nao_acertou):
        chute = input("Informe uma letra ").strip().upper()
        if chute != '':
            # palavra_secreta.find()
            if chute in letras_acertadas:
                print("[ {} ] você já havia informado".format(chute))
            if chute in palavra_secreta:
                index = 0
                for letra in palavra_secreta:
                    if chute == letra:
                        letras_acertadas[index] = chute
                    index += 1
            else:
                erros += 1
                print("[ {} ] não faz parte da palavra secreta, você tem mais {} tentativas ".format(chute, total_tentativas-erros))

        nao_enforcou = erros == total_tentativas
        print(letras_acertadas)
        if (not "_" in letras_acertadas):
            print("\nParabéns você acertou a palavra secreta,  ** {} **\n".format(palavra_secreta.upper()))
            break;



    print("******************************************** Fim do jogo *******************************************")

if(__name__ == "__main__"):
    jogar()