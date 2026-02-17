import random as r

print("***********************************")
print("Jogo de adivinhacao")
print("***********************************")

numero_incial = 1
numero_final = 100

numero_secreto=int(r.randrange(numero_incial,numero_final+1))

def dica():
    if chute_menor:
        print("Seu chute foi menor que o numero secreto")
    elif (chute_maior):
        print("Seu chute foi maior que o numero secreto")

total_tentativas = 3
rodada = 1

# while(total_tentativas > 0):
for rodada in range(1, total_tentativas + 1):

    chute = int(input("Digite um numero entre {} e {}: ".format(numero_incial, numero_final)))

    if chute < numero_incial or chute > numero_final:
        continue

    chute_menor = chute < numero_secreto
    chute_maior = chute > numero_secreto
    acertou = numero_secreto == chute

    if(acertou):
        print("Você acertou ! ! !")
        break;
    else:
        print("Tentativa {} de {}".format(rodada, total_tentativas))
        print("Você digitou:", chute)
        print("Você errou.")
        dica()

print("O numero secreto era {}".format(numero_secreto))