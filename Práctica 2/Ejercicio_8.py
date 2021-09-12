# Ejercicio 8

# Escribir en papel un programa que tome un número entero positivo ingresado por el usuario
# y muestre por pantalla "Usted ingresó un número de una sola cifra" o "Usted ingresó un número
# de más de una cifra" según corresponda. Realizar 4 corridas de escritorio, escribirlo en Python
# y luego correrlo en la computadora con los valores iniciales de las corridas y verificar que hayan
# dado como se esperaba.

num_positivo=int(input("Ingrese un numero positivo: "))

if num_positivo <= 9 and num_positivo>=0:
    print("Usted ingresó un número de una sola cifra")
elif num_positivo>9:
    print("Usted ingresó un número de más de una cifra")
else:
    print("Usted ingresó un número que no es entero positivo")
