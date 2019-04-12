import adivinhacao
import forca

print("********************************* Bem vindo á tela inicial do jogo *********************************")


print("(1) Forca (2) Adivinhação")

jogo_str = input("Qual voce quer jogar")
if jogo_str != '':
    jogo = int(jogo_str)
    if jogo == 1:
        print("Jogo da forca foi escolhido")
        forca.jogar()
    if jogo == 2:
        print("Jogo de adivinhação foi escolhido")
        adivinhacao.jogar()
else:
    print("Opção não encontrada, por favor verifique e tente novamente.")
print("******************************************** Fim do jogo *******************************************")
