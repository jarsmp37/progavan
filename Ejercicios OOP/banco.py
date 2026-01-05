class Banco:
    def __init__(self,nombre,saldo):
        self.__nombre=nombre
        self.__saldo=saldo

    #Getter
    def nombrecliente(self):
        return self.__nombre
    
    def obtenersaldo(self):
        return self.__saldo
    
    #Setter
    def deposito(self,cant1):
        self.__saldo += cant1
        return f"Tu nuevo saldo es {self.__saldo}"
    
    def retirar(self,cant2):
        if self.__saldo<cant2:
            return "No tienes saldo suficiente"
        else:
            self.__saldo-=cant2
            return f"Tu nuevo saldo es {self.__saldo}"
