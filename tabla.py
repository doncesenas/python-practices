print("Este programa muestra la tabla de multiplicar del 1 al 10, del número que ingreses.")

num = int(input("Ingresa un número: "))

for i in range(1,11): #el range genera los números del 1 al 10
    print(f"{num} x {i} = {num*i}") #la cadena f dentro del print, permite incluir variables siempre y cuando estén dentro
    #de {} sin la necesidad de concatenarla

    


