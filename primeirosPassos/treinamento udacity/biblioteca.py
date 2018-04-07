def gera_nome_convite(convite):
	posicao_final = len(convite)
	posicao_incial = posicao_final - 4
	parte1 = convite[0:4]
	parte2 = convite[posicao_incial:posicao_final]
	print('%s %s' % (parte1, parte2))



def cadastrar(nomes):
	nomes = nomes
	print(nomes)
	return len(nomes)