# Ejercicio 4

# a) Escribir una función que reciba dos números reales como parámetros y retorne su
# promedio.

# def promedio(primer_num,segundo_num):
#     promedio = print((primer_num + segundo_num) / 2)
#     return promedio

####################################################################################################################################
# b) Hacer un programa que pida al usuario dos números reales y muestre por pantalla
# el resultado de llamar a la función del primer inciso.

# n = int(input("Ingrese un primer número real: "))
# m = int(input("Ingrese un segundo número real: "))

# promedio(n,m)

####################################################################################################################################
# c) Idem de los dos anteriores pero con tres números. Escribir la función en el mismo
# archivo donde se escribió la del item a.

def promedio(primer_num,segundo_num,tercer_num):
    promedio = print((primer_num + segundo_num + tercer_num) / 3)
    return promedio

n = int(input("Ingrese un primer número real: "))
m = int(input("Ingrese un segundo número real: "))
l = int(input("Ingrese un tercer número real: "))


promedio(n,m,l)