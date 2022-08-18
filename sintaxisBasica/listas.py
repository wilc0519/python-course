mi_lista = ['Loures', 'Wilmer', 'Nana', 'Lilo', 'Miguel', 2, True, 23.12 ] 

print(mi_lista)
print(mi_lista[2])
print(mi_lista[0:2]) #porcion de lista

mi_lista.append('Andrea')#agrega elemento al final dela lista
mi_lista.insert(5, 'Christian')#agrega el elemento en la posicion indicada
mi_lista.extend(['Raul', 'Manuel', 'Pedro'])#agrega varios elementos a la lista
mi_lista.remove(True)#elimina elemento 
mi_lista.pop()#elimina el ultimo elemento de la lista
print(mi_lista.index('Nana')) #devuelve el indice de la posisicon de Nana en la lista, si existe mas de una coincidencia decuelve el indice de la primera coincidencia
print('Lilo' in mi_lista)#la funcion (in) devuelve true si el elemento se encuentra en la lista, caso contrario devuelve false
print(mi_lista * 3) #devuelve los elementos de la lista por triplicado

list1 = [1,2,3,4]
list2 = [5,6,7,7]
newList = list1 + list2#crea una nueva lista con los elementos de las listas concatenadas 
print(newList)
