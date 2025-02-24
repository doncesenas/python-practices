class Coche:
    ##Permite crear una clase
    def __init__(self, marca, modelo):
        ## El método init es un emetodo especial que Python reconoce para crear una instancia
        self.marca = marca
        self.modelo = modelo
        self.arrancado = False

    def arrancar(self):
        self.arrancado=True
        print("El", self.marca, self.modelo, " se ha arrancado")

    def parar(self):
        self.arrancado=False
        print("El", self.marca, self.modelo, " se a parado")

Corolla=Coche("Corolla","Sedan STD 2010")
ChevyPop=Coche("Chevy Pop", "Hatchback STD 2001")

print(type(Corolla))
print(type(ChevyPop))

print(Corolla.marca, Corolla.modelo)
print(ChevyPop.marca, ChevyPop.modelo)

Corolla.arrancar()
ChevyPop.arrancar()

print(Corolla.arrancado)
print(ChevyPop.arrancado)

Corolla.parar()
ChevyPop.parar()

print(Corolla.arrancado)
print(ChevyPop.arrancado)