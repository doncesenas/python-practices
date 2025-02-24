print("Este programa imprimirá tu información si eres mayor de edad")

age=int(input("Ingresa tu edad: "))
name=str(input("Ingresa tu nombre: "))
school=str(input("Ingresa tu institución academica: "))

if age >= 18:
    print("Tus",age," años cumplen con la mayoría de edad:) ")
else:
    print("Tus ",age," años NO cumplen con la mayoría de edad >:(")