def divide():
    try:
        primer_valor = (float(input("ingresar el primer valor: ")))
        segundo_valor = (float(input("Ingresar el segundo valor: ")))
        operacion_division = primer_valor/segundo_valor
        print(operacion_division)
    
    except ValueError:
        print("El valor introducido es erroneo ")

    except ZeroDivisionError:
        print("No se puede dividir para 0!")

    finally:
        print("Operarción finalizada")

divide()