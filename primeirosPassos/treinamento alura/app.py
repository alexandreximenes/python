# -*- coding: UTF-8 -*-
def cadastrar(nomes):
	print('Digite seu nome : ')
	nome = input()
	nomes.append(nome)

def listar(nomes):
	print('Listando nomes...')
	for nome in nomes:
		print(nome)

def menu():
	nomes = []
	escolha = ''
	while(escolha != '0'):
		print('Digite 1 para cadastrar, 2 para listar, 0 para sair')
		escolha = input()

		if(escolha == '1'):
			cadastrar(nomes)	

		if(escolha == '2'):
			listar(nomes)
