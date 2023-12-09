class Empleado:
    def _init_(self, nombre="", apellidos="", edad=0, direccion="", email="", sueldo=0):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.sexo = sexo
        self.direccion = direccion
        self.email = email
        self.sueldo = sueldo

    def AsignarSueldo(self, sueldo):
        self.sueldo = sueldo

    def CalcularAfp(self):
        # El AFP es el 2.87% del sueldo
        afp = 0.0287 * self.sueldo
        return afp

    def CalcularSfs(self):
        # El SFS es el 3.04% del sueldo
        sfs = 0.0304 * self.sueldo
        return sfs

    def CalcularImpuestoRenta(self):
        # Deducciones de TSS
        sfs = self.sueldo * 0.0304
        afp = self.sueldo * 0.0287
        total_deducciones = sfs + afp

        # Base Imponible
        base_imponible = self.sueldo - total_deducciones

        # Multiplicar por 12
        base_anual = base_imponible * 12

        # Verificar en qué rango cae
        if base_anual <= 416220.00:
            impuesto_mensual = 0
        elif 416220.00 < base_anual <= 624329.00:
            excedente = base_anual - 416220.00
            impuesto_anual = excedente * 0.15
            impuesto_mensual = impuesto_anual / 12
        elif 624329.00 < base_anual <= 867123.00:
            excedente = base_anual - 624329.00
            impuesto_anual = excedente * 0.20 + 31216.00  # Sumar el monto fijo adicional
            impuesto_mensual = impuesto_anual / 12
        elif base_anual > 867123.00:
            excedente = base_anual - 867123.00
            impuesto_anual = excedente * 0.25 + 6516.00
            impuesto_mensual = impuesto_anual / 12
        else:
            impuesto_mensual = 0

        return impuesto_mensual

    def imprimirinformacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Apellidos: {self.apellidos}")
        print(f"Edad: {self.edad}")
        print(f"Sexo: {self.sexo}")
        print(f"Dirección: {self.direccion}")
        print(f"E-mail: {self.email}")
        print(f"Sueldo: {self.sueldo}")
        print(f"AFP: {self.Calcular_Afp()}")
        print(f"SFS: {self.Calcular_Sfs()}")
        print(f"IRS: {self.Calcular_Impuesto_Renta():.2f}")


# Obtener datos del usuario
nombre = input("Ingrese el nombre: ")
apellidos = input("Ingrese los apellidos: ")
edad = int(input("Ingrese la edad: "))
sexo = input("Ingrese el sexo: ")
direccion = input("Ingrese la dirección: ")
email = input("Ingrese el correo electrónico: ")
sueldo = float(input("Ingrese el sueldo: "))

# Ejemplo de uso con datos ingresados por el usuario
Empleado1 = Empleado(nombre=nombre, apellidos=apellidos, edad=edad, direccion=direccion, email=email, sueldo=sueldo)
Empleado1.imprimir_informacion()
Empleado1.paga_impuestos()
