print('asignaturas optativas periodo 2022-2023')
print('Asignaturas optativas: Informatica grafica - redes - app moviles')

opcion = input('Seleccione asignatira optativa: ')
asignatura =opcion.lower()

if asignatura in ('informatica grafica', 'redes' ,'app moviles'):
    print('asignatura seleccionada correctamente')
else:
    print('Asignatura seleccionada no existe')