# Ejercicio 27

# Escribir un programa que pida al usuario una cadena e indique si esta posee un diptongo (dos vocales unidas).

palabra = input("Ingrese una palabra por favor: ") 
vocales = "aeiou"
primer_vocal = ""
anterior=""
diptongo = 0

# Prueba: laura

for i in palabra:
    if i in vocales:
        primer_vocal = i
        if anterior in vocales and i == primer_vocal:
            diptongo += 1
            break        
    anterior = i

print("La palabra",palabra,"tiene",diptongo,"diptongo.")

## En realidad quedó desprolijo, porque no estaría contemplando los casos que tengan más de un diptongo. Me hubiera gustado
## meterle esa complejidad.
## Me falla con las palabras que empiezan con una vocal y no tienen realmente diptongo.
## Por ejemplo: astro, alejandro.