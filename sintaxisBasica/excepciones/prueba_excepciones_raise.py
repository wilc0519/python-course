def evaluaEdad(edad):
    if edad < 0:
        raise TypeError("No se permite edades negativas")
    if edad < 20:
        return "eres muy joven"
    
    elif edad < 40:
        return "eres joven"

    elif edad < 65:
        return "eres adulto"

    elif edad < 100:
        return "eres adulto mayor"

print(evaluaEdad(-12))
