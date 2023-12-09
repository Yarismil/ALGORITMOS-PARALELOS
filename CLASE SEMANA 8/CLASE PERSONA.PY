class Persona:
    nombre = ""
    apellidos = ""
    edad= ""
    sexo = ""
    dirreción = ""

    def Persona1(self):
        return self.nombre + " " + self.apellidos + " , " + self.edad + self.sexo + " ," + self.dirreción

Pers = Persona()
Pers.nombre = input("Nombre..:")
Pers.apellidos = input("Apellidos..:")
Pers.edad = input("Edad..:")
Pers.dirreción = input("Dirreción..:")

print(Pers.Persona1())