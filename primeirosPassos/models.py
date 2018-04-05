# -*- coding: UTF-8 -*-
class Perfil(object):
	'Classe padrão para perfis de usuários'
	
	def __init__(self, nome, telefone, empresa):
		self.nome = nome
		self.telefone = telefone
		self.empresa = empresa
		self.curtidas = 0

	def imprimir(self):
		print('Dados Cadastrais : \n'+ self.nome + ' \n' + self.telefone + ' \n' + self.empresa + ' \n' + self.curtidas)

	def curtir(self):
		self.curtidas+=1

	def obter_curtidas(self):
		return self.__curtidas

	@classmethod
	def gerar_perfis(classe, nome_arquivo):
		arquivo = open(nome_arquivo, 'r')
		perfis = []
		for linha in arquivo:
			token = linha.split(',')
			perfis.append(classe(*token))
			arquivo.close()
			return perfis

class Perfil_Vip(Perfil):
	'Classe padrão para perfis de usuários vip'

	def __init__(self, nome, telefone, empresa, apelido=''):
		super(Perfil_Vip, self).__init__(nome, telefone, empresa)
		self.apelido = apelido

	def obter_creditos(self):
		return super(Perfil_Vip, self).obter_curtidas() * 10.0
