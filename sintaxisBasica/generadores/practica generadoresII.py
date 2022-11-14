def devuelve_ciudades(*ciudades):
    for ciudad in ciudades:
        yield from ciudad

ciudades_devueltas = devuelve_ciudades("Quito", "Guayaquil", "Ambato", "Cuenca", "Riobamba")

print(next(ciudades_devueltas))

print(next(ciudades_devueltas))