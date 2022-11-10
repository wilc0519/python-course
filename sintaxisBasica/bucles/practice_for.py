for num in [1,2,3,4,5,6,7,8,9,10]: #se ejecuta tantas veces como elementos tenga el arreglo
    print(num, "x 2")
    print (num *  2)

for i in ['Wilmer', 'Ivan', 'Lopez', 'Carrera']: #se ejecuta tantas veces como elementos tenga el arreglo
    print(i, end=" ")

print('')

for i in 'wilclopezcar': #se ejecuta tantas veces como numero de caracteres tenga un string
    print('hola', end=" ")

print('')
email = input("Ingrese correo electronico: ")
count = 0
for i in email:
    if i =='@' or i=='.':
        count += 1
if count==2:
    print('Email is correct')
else:
    print('Email is not correct')