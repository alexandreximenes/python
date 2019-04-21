import random

def jogar():
    nao_enforcou = False
    nao_acertou = False
    erros = 0

    imprime_mensagem_de_abertura()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    total_tentativas = len(palavra_secreta)

    print(letras_acertadas)

    while(not nao_enforcou and not nao_acertou):
        chute = pede_chute()
        if chute != '':
            informa_se_ja_havia_informado_esta_palavra(chute, letras_acertadas)
            if chute in palavra_secreta:
                erros = marca_chute_correto(chute, erros, letras_acertadas, palavra_secreta)
            else:
                erros += 1
                informa_palavra_aviso_de_letra_errada(chute, erros, total_tentativas)
        nao_enforcou = erros == total_tentativas
        print(letras_acertadas)
        if (not "_" in letras_acertadas):
            print("\nParabéns você acertou a palavra secreta,  ** {} **\n".format(palavra_secreta.upper()))
            break;


def informa_palavra_aviso_de_letra_errada(chute, erros, total_tentativas):
    print("[ {} ] não faz parte da palavra secreta, você tem mais {} tentativas "
          .format(chute, total_tentativas - erros))


def marca_chute_correto(chute, erros, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[index] = chute
        index += 1
    return erros

def informa_se_ja_havia_informado_esta_palavra(chute, letras_acertadas):
    # palavra_secreta.find()
    if chute in letras_acertadas:
        print("[ {} ] você já havia informado".format(chute))


def pede_chute():
    return input("Informe uma letra ").strip().upper()


def inicializa_letras_acertadas(palavra_secreta):
    return ["_" for letra in palavra_secreta]


if(__name__ == "__main__"):
    jogar()


def imprime_mensagem_de_abertura():
    print("********************************* Bem vindo no jogo da forca *********************************")

def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return  palavra_secreta
