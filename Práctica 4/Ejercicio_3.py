# Ejercicio 3

# a) Escribir una función que reciba como parámetro una cadena y la muestre en pantalla
# 3 veces.

# cadena = input("Ingrese cualquier cosa por favor: ")
# repetidor = 4

# def tresVeces(expresion):
#    tres_veces = "" 
#     for char in range(1,repetidor):
#         print(expresion)
#         tres_veces = tres_veces + "\n"
#     return tres_veces

# tresVeces(cadena)

########################################################################################################################################################################
# b) Guardar esta definición de función en un archivo.

# DONE

########################################################################################################################################################################
# c) Hacer un programa que le pida al usuario una cadena y que la muestre en pantalla
# 3 veces utilizando la función definida anteriormente.

import funcion_ej3

cadena = input("Ingrese cualquier cosa por favor: ")

funcion_ej3.tresVeces(cadena)
