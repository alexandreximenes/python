import random

print("********************************* Bem vindo no jogo de adivinhação *********************************")

total_de_tentativas = 0
rodada = 1
# numero_secreto = round(random.random() * 100)
numero_secreto = round(random.randrange(1,101))

print("Qual nivel de dificuldade?")
print("(1) Facil (2) Medio (3) Dificil")

nivel = int(input("Defina o nivel: "))
pontos = 100

if nivel == 1:
    total_de_tentativas = 10
elif nivel == 2:
    total_de_tentativas = 5
else:
    total_de_tentativas = 3

for rodada in range(1, total_de_tentativas + 1):

    print("Tentativa {:d} de {:d}".format(rodada, total_de_tentativas))

    chute_str = int(input("Digite o seu numero entre 1 e 100: "))

    chute = int(chute_str)

    if chute < 1 or chute > 100:
        print("Voce deve digitar um número entre 1 e 100")
        continue

    print("Você digitou", chute)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Você acertou e fez {:d}, parabens !!!!".format(pontos))
        break
    else:
        if maior:
            print("Voce nao acertou, seu chute foi maior que o numero secreto")
        elif menor:
            print("Voce nao acertou, seu chute foi menor que o numero secreto")
        pontos_perdidos = abs(numero_secreto - chute)
        pontos -= pontos_perdidos



print("******************************************** Fim do jogo *******************************************")
