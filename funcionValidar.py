import re

def validar_usuario(email: str, password: str):
    errores=[]

    #Validar que el correo sea gmail
    if not re.fullmatch(r"^[a-zA-Z0-9._%+-]+@gmail\.com$", email):
        errores.append("El correo debe de ser de dominio GMAIL (ejemplo: usuario@gmail.com)")

    #Validar la seguirdad de la contraseña
    if len(password) < 8:
        errores.append("La contraseña tiene que ser mayor a 8 caracteres")
    if not re.search(r"[A-Z]", password):
        errores.append("La contraseña debe de incluir al menos una letra Mayúscula")
    if not re.search(r"[a-z]",password):
        errores.append("La contraseña debe de incluir al menos una letra en Minuscula")
    if not re.search(r"\d",password):
        errores.append("La contraseña debe de llevar al menos un número")
    if not re.search(r"@!#$%&/()=,.-{}", password):
        errores.append("La contraseña debe de incluir al menos un caracter especial (  + @ ! # $ % & / ( ) = , . - ) ")
    
    # Si hay errores, los devuelve, si no, confirma que la validación fue exitosa

    if errores:
        return{"Válido": False, "errores": errores}
    else:
        return{"Valido", True, "mensaje","Usuario validado correctamente"}
    
user_email = input("Ingrese su correo: ")
user_password = input("Ingrese su contraseña: ")

#ahora toca validar con LA FUNCIÓN 

resultado = validar_usuario(user_email, user_password)

if resultado["Válido"]:
    print(resultado["mensaje"])
else:
    print("\n ⚠️ Se encontraron los siguientes ERRORES: ")
    for errores in resultado["errores"]:
        print("error")