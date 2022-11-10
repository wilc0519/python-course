for i in range(5): # recorre la posiciones del 0 al 4
    print(i)

for i in range(5,8): #
    print(i)

for i in range(2,24,4):
    print (i)


email = input("Ingresa tu email: ")
status = False
for i in range(len(email)):
    if email[i] == '@':
        status = True
if status:
    print('Email correcto')
else:
    print('Email incorrecto') 
