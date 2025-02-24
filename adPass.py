print("Este programa te pide una contraseña y la va a comparar a ver si es la misma que hemos asignado nosotros: ")

key='contraseña'
user=input("Introduce tu usuario: ")
password=input("Introduce tu contraseña: ")

if key==password.lower():
    ## La función lower nos permite convertir todos los caracteres a minusculas de la variable que estamos seleccionado

    print("La contraseña conincide:)")
else:
    print("La contraseña NO coincide: ")