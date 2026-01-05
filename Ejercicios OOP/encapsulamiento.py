class CuentaBancaria:
    def __init__(self,titular,saldo):
        self._titular=titular
        self.__saldo=saldo


cuenta1=CuentaBancaria("Ximena",100000)
print(f"el nombre al que está la cuenta es {cuenta1._titular}")