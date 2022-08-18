distancia = int(input('Ingresar distancia de movilizacion: '))
numero_hermanos = int(input('Ingresar numero de hermanos: '))
salario_familiar = int(input('Ingresos familiares aniales: '))

if distancia > 40 and numero_hermanos >2 or salario_familiar < 20000:
    print('Beca aprobada')
else:
    print('Beca denegada')