# Ejercicio 19

# a) Escribir un programa que permita al usuario elegir un número m y un n y muestre
# todos los pares de numeros que se pueden formar con los números que están entre
# ellos, pero esta vez que lo haga sin repetir inversos. Por ej. si el usuario ingresara 4
# y 6, el programa deberá mostrar
# 4 4
# 4 5
# 4 6
# 5 5
# 5 6
# 6 6

# m = int(input("Ingrese un número M: "))
# n = int(input("Ingrese un número N: "))

# for i in range(m,n+1):
#     for j in range(m,n+1):
#         print(i,j)
#     m +=1
    

# con while:

# m = int(input("Ingrese un número M: "))
# n = int(input("Ingrese un número N: "))
# contador = 0

# while contador <= n:
#     for i in range(m,n+1):
#         for j in range(m,n+1):
#             print(i,j)
#         m +=1
#     contador+=1


####################################################################################################################################
# b) Cambiar el programa para que use sólo un ciclo en vez de dos.

m = int(input("Ingrese un número M: "))
n = int(input("Ingrese un número N: "))

i = m
j = m   # Usaríamos variables aux. para manipular los cambios de m en comparativa de n y el ciclo.
flag = True

while i <= n:
    if j <= n:
        print(i,j) # Acá está el ciclo principal, donde me imprime nros. en las 2 columnas.
        j += 1
    else:
        i += 1
        flag = False
    if flag == False:
        j = i    
        flag = True
