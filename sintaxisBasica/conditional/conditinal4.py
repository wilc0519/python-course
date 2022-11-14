from readline import read_init_file


salarioPresidente = int(input("Salario del presidente: "))
print('Salario presidenta: ' +str(salarioPresidente))

salarioDirectivo = int(input("Salario del directivo: "))
print('Salario directivo: ' +str(salarioDirectivo))

salarioJefeArea = int(input("Salario del jefe de area: "))
print('Salario jefe de area: ' +str(salarioJefeArea))

salarioAdministrativo = int(input("Salario del administrativo: "))
print('Salario administrativo: ' +str(salarioAdministrativo))

if salarioAdministrativo<salarioJefeArea<salarioDirectivo<salarioPresidente:
    print('Remuneracion correcta')
else:
    print('Algo esta mal')