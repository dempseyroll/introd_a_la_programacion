# Ejercicio 14

# Escribir un programa que pida al usuario dos enteros y los guarde en dos variables. Si el
# primero de los valores fuera menor que el segundo, el programa deberá además intercambiar los
# valores de las variables y mostrarlos de mayor a menor.

nro_1 = int(input("Ingrese un nro entero: "))
nro_2 = int(input("Ingrese 2do num entero: "))

if nro_1 < nro_2:
    aux=nro_2
    nro_2=nro_1
    nro_1=aux
    print("Se enrocan los números y se devuelven de mayor a menor:\n",nro_1,"\n",nro_2)
else:
    print("Los números son:\n",nro_1,"\n",nro_2)

