
class Conta:

    def __init__(self, numero, titular, saldo, limite):
        # print("construtor de conta {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        # self.data = Data(data)

    @staticmethod
    def codigo_banco():
        return "001"

    @property
    def limite(self):
        return self.__limite

    def valor_disponivel(self):
        return self.__limite + self.saldo

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    def __pode_sacar(self, valor):
        if(valor < self.valor_disponivel()):
            return True
        return False

    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, titular):
        self.__titular = titular

    def extrato(self):
        print("Conta do {} com saldo de {} e limite de {}".format(self.__titular, self.__saldo, self.__limite))

    def depositar(self, valor):
        self.__saldo += valor
        print("Conta do {} possui novo saldo de {} e limite de {}".format(self.__titular, self.__saldo, self.__limite))

    def sacar(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        print("Conta do {} possui novo saldo de {} e limite de {}".format(self.__titular, self.__saldo, self.__limite))

    def transferir(self, valor, destinatario):
        self.sacar(valor)
        destinatario.depositar(valor)
        print("Transferencia OK, conta do {} possui saldo de {} e conta do {} tem saldo de {}"
              .format(self.__titular, self.__saldo, destinatario.__titular, destinatario.__saldo))

    @property
    def saldo(self):
        saldo = self.__saldo
        print("Conta do {} possui saldo de {} e limite de {}".format(self.__titular, saldo, self.__limite))
        return self.__saldo
