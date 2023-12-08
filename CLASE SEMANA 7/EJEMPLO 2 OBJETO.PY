class Alumno:


    def nombrecompleto (self, nombre, apellido):
        return nombre +""+ apellido
    
alu = Alumno()
nombre = input("Nombre..:")
apellido = input("Apellido..:")

print (alu.nombrecompleto(nombre,apellido))