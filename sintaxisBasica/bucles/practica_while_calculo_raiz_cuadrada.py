import math
print("Programa de calculo raiz cuadrada")
numero = int(input("Ingrese número: "))
intentos = 0

while numero<0:
    print("no se puede obtener la raiz cuadrada de un número negativo")

    if intentos == 2:
        print("exediste tu numero de intentos")
        break
    
    numero = int(input("Ingrese número"))
    if numero<0:
        intentos= intentos+1

if intentos < 2:
    print("la rais cuadrada de: ", numero, " es ", int(math.sqrt(numero)))

