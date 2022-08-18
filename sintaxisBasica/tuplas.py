miTupla = ('juan', 'Manuel', 'Pedro', 1, 20.2, True,1, 'Pedro')#Las tuplas son inmutables

print(miTupla)
print(miTupla.index('Pedro'))

miLista = list(miTupla)#transformar una tupla a una lista

print(miLista)

miTupla2 = tuple(miLista)#convierte una lista a tupla

print(miTupla2)

print('Manuel' in miTupla)#busca el elemento en la tupla si encuentra devuelve true, de lo contrario devuelve false
print(miTupla.count('Pedro'))#busca el numero de coincidencias en la tupla
print(len(miTupla))#devuelve la longitud de la tupla

tuplaUnitaria = ('Miguel',)#tupla unitaria
print(len(tuplaUnitaria))

miTupla3 = ('Miguel', 14, 2, 2022)
nombre, dia, mes, anio = miTupla3#desempaquetado de tuplas
print(nombre)
print(anio)
print(dia)
print(mes)
