class Estudiante:
    nombre = ""
    apellido= ""
    Edad = ""
    Sexo = ""
    Direccion= ""
    Matrícula = ""
    Carrera = ""
    Email= ""
    Telefono = ""

    def Estudiante1(self, nombre, apellido, Edad ,Sexo, Direccion, Matrícula, Carrera, Email,Telefono):
        return nombre +" "+ apellido +" "+ Edad +" "+ Sexo +" "+ Direccion +" "+ Matrícula +" "+ Carrera +" "+ Email +" "+ Telefono
    
Estd = Estudiante()
nombre = input("Nombre..:")
apellido = input("Apellido..:")
Edad = input("Edad..:")
Sexo = input("Sexo..:")
Direccion = input("Direccion..:")
Matrícula = input("Matrícula..:")
Carrera = input("Carrera..:")
Email = input("Email..:")
Telefono = input("Telefono..:")

print (Estd.Estudiante1(nombre,apellido, Edad, Sexo, Direccion, Matrícula, Carrera, Email, Telefono))