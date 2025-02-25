print("Bienvenidos a juegos El Bodoque")

nombre=input("Que tal, ¿cual es tu nombre?: ")
age=int(input("Ingresa tu edad para saber el costo de tu entrada: "))

if age < 4:
    print("Puedes pasar gratis, con supervisión de un adulto:)")
    precio = 0
elif age >= 8 and age < 18:
    precio = 50
    print("Hola ",nombre, " el costo de tu entrada es de $",precio,"$.00mxn")
elif age >= 18:
    precio=100
    print("Hola ",nombre," el costo de tu entrada es de $",precio,".00mxn")
