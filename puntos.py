bonificacion = 2400
inaceptable = 0.0
aceptable = 0.4
meritorio = 0.6
puntos = float(input("Captura tu puntuación: "))

if puntos == inaceptable:
    print("Su puntuación es INACEPTABLE: ")
    nivel = inaceptable
elif puntos == aceptable:
    print("Su puntuación es ACEPTABLE. ")
    nivel = aceptable
elif puntos == meritorio:
    print("Su puntuación es MERITORIA")
    nivel = meritorio
else:
    nivel = ""

if nivel == "":
    print("Esta puntuación no es válida")
else:
    print("Tu nivel de rendimiento es %s" % nivel)
    print("Te corresponde cobrar %.2f$ " % (puntos*bonificacion))