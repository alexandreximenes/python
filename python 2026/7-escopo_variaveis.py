"""
Escopo variaveis globais e locais
"""

var1 = 'Computer Science'
print(var1)
print(type(var1))

def varGlobal():
    print(var1)
def varLocal():
    var2 = 'Computer Science 2'
    print(var2)

varGlobal()
varLocal()


