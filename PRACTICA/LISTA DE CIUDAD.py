#Crea una lista vacía y luego que el usuario pueda agregar 5 nombres de ciudad usando el método append() y mostrarlo en pantalla.

Lista_ciudad = []
contador =1

for cont in range (5):

    Datos = input ("Ingrese los datos: ")
    Lista_ciudad.append(Datos)
    contador +=1

print(Lista_ciudad)