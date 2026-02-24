"""
String
"""
print('nome') #nome
print(type('nome')) #<class 'str'>


# nome = input("qual seu nome? ") #ale xim
# nome = nome.title()
# print(nome) #Ale Xim

nome = """Ale"""
print(nome) #Ale
print(type('nome')) #<class 'str'>

nome = """Ale's"""
print(nome) #Ale's
print(type('nome')) #<class 'str'>

nome = """Ale's"""
print(nome) #Ale's
print(nome.upper())

nome = """Ale Xim"""
print(nome) #Ale Xim
print(nome.split())  #['Ale', 'Xim']

nome = "Alexandre Ximenes"
print(nome)
print(nome.split())  #['Alexandre', 'Ximenes']
print(nome[0:9])  #Alexandre
print(nome[10:])  #[Ximenes]
print(nome.split()[0])  #Alexandre
#começa no primeiro elemento, vai até o ultimo e inverta
print(nome[::-1])  #senemiX erdnaxelA
print(nome.replace('x', 'X'))  #AleXandre Ximenes
#palindromo
palavra = "socorram me subino onibus em marrocos"
print(palavra)  #socorram me subino onibus em marrocos
print(palavra[::-1])  #socorram me subino onibus em marrocos




