class Alumno:
    nombre=""
    apellido=""

    def nombrecompleto (self):
        return self.nombre +""+ self.apellido
    
alu = Alumno()
alu.nombre = input("Nombre..:")
alu.apellido = input("Apellido..:")

print (alu.nombrecompleto())