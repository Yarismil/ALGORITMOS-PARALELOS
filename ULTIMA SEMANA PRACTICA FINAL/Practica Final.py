class Cliente:
    def __init__(self, numero_cuenta, saldo, contrasena):
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo
        self.contrasena = contrasena

class CajeroAutomatico:
    def __init__(self, cliente):
        self.cliente = cliente

    def validar_usuario(self, numero_cuenta, contrasena):
        return self.cliente.numero_cuenta == numero_cuenta and self.cliente.contrasena == contrasena

    def menu(self):
        print("Elige lo que quieres hacer")
        print("1. Retiro")
        print("2. Deposito")
        print("3. Transaccion")
        print("0. Salir")

    def retiro_efectivo(self, cantidad):
        if self.cliente.saldo >= cantidad:
            self.cliente.saldo -= cantidad
            print(f"Se retiraron {cantidad} de la cuenta {self.cliente.numero_cuenta}. Tu Saldo es de: {self.cliente.saldo}")
        else:
            print("Saldo insuficiente.")

    def deposito_efectivo(self, cantidad):
        self.cliente.saldo += cantidad
        print(f"Se depositaron {cantidad} en la cuenta {self.cliente.numero_cuenta}. Tu saldo es de : {self.cliente.saldo}")

    def transferencia_fondos(self, destinatario, cantidad):
        if self.cliente.saldo >= cantidad:
            destinatario.saldo += cantidad
            self.cliente.saldo -= cantidad
            print(f"Se transfirieron {cantidad} a la cuenta {destinatario.numero_cuenta}. Tu saldo es de : {self.cliente.saldo}")
        else:
            print("No tienes saldo suficiente para realizar la transferencia.")

# Creación de instancia con contraseña
cliente1 = Cliente("87221", 5000, "770012")

# Creación de instancia de CajeroAutomatico
cajero_automatico = CajeroAutomatico(cliente1)

# Solicitud
numero_cuenta = input("Ingrese el número de cuenta: ")
contrasena = input("Ingrese la contraseña: ")

# Validar
if cajero_automatico.validar_usuario(numero_cuenta, contrasena):
    print(f"Bienvenido al cajero automático. Número de cuenta: {cajero_automatico.cliente.numero_cuenta}.")

    while True:
        cajero_automatico.menu()

        opcion = input("Ingrese el número de la operación que desea realizar (0 para salir): ")

        if opcion == '0':
            print("Que tenga un feliz resto del dia")
            break

        if opcion.isdigit() and 1 <= int(opcion) <= 3:
            opcion = int(opcion)
            if opcion == 1:
                cantidad = float(input("Ingrese la cantidad a retirar: "))
                cajero_automatico.retiro_efectivo(cantidad)
            elif opcion == 2:
                cantidad = float(input("Ingrese la cantidad a depositar: "))
                cajero_automatico.deposito_efectivo(cantidad)
            elif opcion == 3:
                destinatario_numero_cuenta = input("Ingrese el número de cuenta del destinatario: ")
                destinatario = Cliente(destinatario_numero_cuenta, 0, "")  # Crear cliente temporal
                cantidad = float(input("Ingrese la cantidad a transferir: "))
                cajero_automatico.transferencia_fondos(destinatario, cantidad)
        else:
            print("Opción no válida. Ingrese un número del 1 al 3 o 0 para salir.")
else:
    print("Número de cuenta o contraseña incorrectos.")
