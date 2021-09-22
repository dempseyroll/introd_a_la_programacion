# Ejercicio 14
# El logaritmo natural de 2 (ln(2)) se puede aproximar de la siguiente manera:

# ln(2) = 1 − 1/2 + 1/3 − 1/4 + 1/5 . . .

# a) Escribir un programa que le pregunte al usuario la cantidad de términos a sumar y
# que muestre la aproximación de ln(2) con esa cantidad de términos. 

# import math

# cant_terminos = int(input("Ingrese cantidad de términos para el cálculo de ln(2): "))
# primer_term = 1
# resultado = 1

# for i in range(2,cant_terminos+2):
#     if i % 2 == 0:
#         calculo = resultado - (primer_term / i)
#         print("Calculo de ln(2):",resultado,"-", primer_term,"dividido", i,"=",calculo)
#         resultado = calculo
#     else:
#         calculo = resultado + (primer_term / i)
#         print("Calculo de ln(2):",resultado,"+", primer_term,"dividido", i,"=",calculo)
#         resultado = calculo

################################################################################################################################
# b) ¿A partir de cuántos términos el valor alcanzado está a menos de 0.1 del valor que
# da la calculadora? En python se puede aproximar este valor usando math.log(2)

# math.log(2)
# 0.6931471805599453

# import math
# log2= math.log(2)
# print(log2)

# suma=0
# i=1

# while(abs(log2-suma)>=0.1):
#     termino=1/i
#     if i%2==0:
#         suma=suma-termino
#     else:
#         suma=suma+termino
#     i=i+1
# print(i,suma)

# A partir de 6 términos.

################################################################################################################################
# c) ¿A partir de cuántos términos el valor alcanzado está a menos de 0.01 del valor que
# da la calculadora?

# import math
# log2= math.log(2)
# print(log2)

# suma=0
# i=1

# while(abs(log2-suma)>=0.01):
#     termino=1/i
#     if i%2==0:
#         suma=suma-termino
#     else:
#         suma=suma+termino
#     i=i+1
# print(i,suma)

# A partir de 51 términos.

################################################################################################################################
# d) Modificar el programa para que en lugar de pedir la cantidad de términos a sumar,
# pida al usuario un número decimal e (muy chico) y calcule la suma hasta que el
# error comparado con el valor de la calculadora sea menor que e.

import math
e= math.e
print(log2)

suma=0
i=1

while(abs(log2-suma)>=e):
    termino=1/i
    if i%2==0:
        suma=suma-termino
    else:
        suma=suma+termino
    i=i+1
print(i,suma)


## Entiendo maso estos ejercicios.