class Persona():
    def __init__(self, nombre, edad, lugar_de_residencia):
        self.nombre = nombre
        self.edad = edad
        self.lugar_de_residencia = lugar_de_residencia

    def descripcion(self):
        print("Nombre:", self.nombre, "Edad:", self.edad, "Residencia:", self.lugar_de_residencia)


class Empleado(Persona):
    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):
        super().__init__(nombre_empleado, edad_empleado, residencia_empleado)
        self.salario = salario
        self.antiguedad = antiguedad

    def descripcion(self):
        super().descripcion()
        print("Salario:", self.salario, "Antigueda:", self.antiguedad)


Wilmer = Empleado(1500, 3, "Wilmer", 43, "Ecuador")
print(Wilmer.descripcion())

print(isinstance(Wilmer, Empleado))