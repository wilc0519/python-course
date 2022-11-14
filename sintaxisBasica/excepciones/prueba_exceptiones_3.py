import math
def calculaRaizCuadrada(numero):

    if numero < 0 :
        raise ValueError ("El número no puede ser negativo")

    else:
        return math.sqrt(numero)

numero_para_calcular_raiz_cuadrada = (float(input("Ingresa numero: ")))

try: 
    print(calculaRaizCuadrada(numero_para_calcular_raiz_cuadrada))

except ValueError as ErrorDeNumeroNegativo:
    print(ErrorDeNumeroNegativo)

print("programa terminado")