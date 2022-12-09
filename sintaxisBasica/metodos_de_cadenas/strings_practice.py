#nombre_de_usuario = input("introduce tu nombre de usuario: ")

#print(nombre_de_usuario.upper())
#print(nombre_de_usuario.capitalize())

edad = (input("Introduce tu edad: "))

while(edad.isdigit() == False):
    print("por favor, Introduce un valor numérico")
    edad = input("Introduce tu edad: ")

if int(edad) < 18:
    print("No puedes ingresar")

else:
    print("Puedes ingresar")