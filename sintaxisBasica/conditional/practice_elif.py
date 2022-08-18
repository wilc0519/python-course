print('verificar nota')
nota_Alumno = int(input('Ingresar nota: '))

if nota_Alumno < 5:
    print('insuficiente')
elif nota_Alumno < 6:
    print('suficiente')
elif nota_Alumno < 7:
    print('bien')
elif nota_Alumno < 9:
    print('muy bien')
elif nota_Alumno > 10:
    print('Nota incorrecta')
else :
    print('Sobresaliente')
