print("*********************************")
print("Bem vindo no jogo de adivinhação")
print("*********************************")

numero_secreto = 15

chute_str = int(input("Digite o seu numero: "))

chute = int(chute_str)

print("Você digitou", chute)

if (numero_secreto == chute):
    print("Você acertou, parabens !!!!")
else:
    print("Voce nao acertou, tente novamente")

    print("Fim do jogo")
