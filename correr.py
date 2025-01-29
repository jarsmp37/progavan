from banco import Banco

cliente1=Banco("Angel",100000)
print(cliente1.nombrecliente())
print(cliente1.obtenersaldo())
print(cliente1.deposito(20000))
print(cliente1.obtenersaldo())
print(cliente1.retirar(60000))
print(cliente1.retirar(70000))
