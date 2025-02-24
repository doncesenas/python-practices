print("De acuerdo a tu genero, te asignaremos a un grupo")

name=input("Ingresa tu nombre: ")
gender=input("Ingresa tu genero (H o M)")

if gender == "M":
    if name.lower() < "m":
        group = "A"
    else:
        group = "B"
else:
    if name.lower() > "n":
        group = "B"
    else:
        group = "A"

    print("Tu grupo es: ", group)