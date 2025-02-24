print("Este programa permite saber si eres apto para declarar impuestos: ")

name=str(input("Ingresa tu nombre: "))
age=int(input("Ingresa tu edad: "))
ingreso=int(input("Ingresa tus ingresos mensuales brutos: $"))

if age >= 16 and ingreso >= 1000:
    print("Cumples con los requisitos para declarar: ")
elif age < 16 and ingreso >= 1000:
    print("Cumples con el ingreso necesario, pero no con la edad para declarar: ")
elif age >=16 and ingreso <1000:
    print("Cumples con la edad, pero no con los ingresos necesarios para cotizar: ")
else:
    print("No cumples con ningún requisito para DECLARAR")