# Ejercicio 26

# Hacer un programa que dada una palabra y una letra, imprima la cantidad de apariciones de esa letra.

palabra = input("Ingrese una palabra por favor: ")
letra = input("Ahora ingrese una letra: ")
cant_veces = 0

for i in palabra:
    if i == letra:
        cant_veces += 1

print("La letra",letra,"aparece",cant_veces,"veces en la palabra",palabra)
