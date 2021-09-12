# Ejercicio 7

# Escribir en papel un programa que pida al usuario dos números de punto flotante y muestre
# su promedio. Además, si el promedio es mayor que 7 el programa debe mostrar en pantalla
# "Aprobado" y si no, debe mostrar "Desaprobado". Después de hacerlo en papel, pasarlo a Python.

nro_1= float(input("Ingrese un número: "))
nro_2= float(input("Ingrese segundo numero: "))

promedio=(nro_1+nro_2)/2
print("Promedio: ", promedio)

if promedio>7:
    print("Aprobado")
else:
    print("Desaprobado")
