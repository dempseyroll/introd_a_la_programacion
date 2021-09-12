# Ejercicio 11

#Se desea escribir un programa que pida al usuario tres números y luego muestre el mayor de
# ellos. Escribir el programa en papel, realizar 3 pruebas de escritorio y luego pasarlo a Python y
# verificar los resultados.

nro_1=int(input("Ingrese numero 1: "))
nro_2=int(input("Ingrese numero 2: "))
nro_3=int(input("Ingrese numero 3: "))

if nro_1>nro_2 and nro_1>nro_3:
    print("El numero mayor es: ",nro_1)
elif nro_2>nro_1 and nro_2>nro_3:
    print("El numero mayor es: ",nro_2)
else:
    print("El numero mayor es: ",nro_3)
