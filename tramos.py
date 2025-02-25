print("Te indicamos que tipo de impositivo te corresponde:)")

name=input("Ingresa tu nombre: ")
renAnual = float(input("Ingresa tu renta anual: "))

if renAnual < 10000:
    tipo = 5
    print("Hola ",name,"Tu tipo de impositivo es del 5%, y tienes que pagar: ",renAnual*tipo/100,'$')
elif renAnual > 10000 and renAnual <= 20000:
    tipo =15
    print("Hola ",name,"Tu tipo de impositivo es del 15%, y tienes que pagar: ",renAnual*tipo/100,'$')
elif renAnual > 20000 and renAnual <= 35000:
    tipo = 20
    print("Hola ",name,"Tu tipo de impositivo es del 20%, y tienes que pagar: ",renAnual*tipo/100,'$')
elif renAnual >35000 and renAnual <= 60000:
    tipo = 30
    print("Hola ",name,"Tu tipo de impositivo es del 30%, y tienes que pagar: ",renAnual*tipo/100,'$')
elif renAnual > 600000:
    tipo = 45
    print("Hola ",name,"Tu tipo de impositivo es del 45%, y tienes que pagar: ",renAnual*tipo/100,'$')

    