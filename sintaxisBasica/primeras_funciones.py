import math
def ecuacion_segundo_grado(a, b, c):
    primera_raiz = (-b + math.sqrt(math.pow(b, 2)- 4*a*c))/2*a
    segunda_raiz = (-b - math.sqrt(math.pow(b, 2)- 4*a*c))/2*a

    return primera_raiz ,segunda_raiz


print(ecuacion_segundo_grado(1, 3, 2))
