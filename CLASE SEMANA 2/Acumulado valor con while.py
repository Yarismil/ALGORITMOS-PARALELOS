numero =1
sueldo= 0
total= 0

while numero <=5:

    sueldo =int (input("Ingrese sueldo:"))

    total = total + sueldo/12

    numero = numero + 1

print ("Total de sueldos:", total)
