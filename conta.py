
class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print(f'Construindo objeto{self}')
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

#----------------------------Métodos-------------------------------

    def extrato(self):
        print(f'{self.__saldo} do  {self.__titular}')

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        if self.__podeSacar(valor):
            self.__saldo -= valor
        else:
            print(f'Você não está autorizado a sacar este valor!')

    def tranferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)
#------------------------------------------------------------------
    def __podeSacar(self,valorSacar):
        valorDisponivel = self.__saldo + self.__limite
        return valorSacar <= valorDisponivel

    @staticmethod #ST Codigo banco
    # #static n precisa de objeto p funcionar
    def codigos_Bancos():
        return {'BB':'001', 'Caixa':'104', 'Bradesco': '237'}

    @property # GT Saldo
    def saldo(self):
        return self.__saldo

    @property #GT Titular
    def titular(self):
        return self.__titular

    @property # GT limite
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite
