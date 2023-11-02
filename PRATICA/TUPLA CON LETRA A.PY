#Crea una tupla con 5 palabras. Cuenta cuántas veces aparece la letra 'a' en total en todas las palabras.

tupla_letra = ("Granja", "Avena", "Milagro", "Perro", "Cadena")
contador =1

for palabra in tupla_letra:
    contador += palabra.count('a')

print(contador)