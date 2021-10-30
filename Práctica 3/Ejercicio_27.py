# Ejercicio 27

# Escribir un programa que pida al usuario una cadena e indique si esta posee un diptongo (dos vocales unidas).

palabra = input("Ingrese una palabra por favor: ") 
vocales = "aeiou"
anterior=" "
diptongo = 0

for i in palabra:
    if anterior in vocales and (i in vocales):
        diptongo += 1
        break        
    anterior = i

print("La palabra",palabra,"tiene",diptongo,"diptongo.")


# Pruebas diptongo: laura, leer, astronauta, paula, florencia,
# Pruebas sin diptongo: astro, alejandro, jarro, taza, elefante
# éxito!
