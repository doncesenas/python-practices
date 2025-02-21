##Esta es una calculadora
print("**Esta es una calculadora que realiza operaciones de 2 números que captures**")


op=str(input("Ingresa el operador: "))
num1=int(input("Ingresa el primer número: "))
num2=int(input("Ingresa el segundo número: "))

if op == '*':
    print("El resultado es: ",num1*num2)
elif op == '+':
    print("El resultado es: ",num1+num2)
elif op == '-':
    print("El resultado es: ",num1-num2)
elif op == '/':
    print("El resultado es: ",num1/num2)
else:
    print("Operador inválido")