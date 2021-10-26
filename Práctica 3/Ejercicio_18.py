# Ejercicio 18

# a) Escribir un programa que permita al usuario elegir un número m y un n y muestre
# todos los pares de numeros que se pueden formar con los números que están entre
# ellos. Por ej. si el usuario ingresara 4 y 6, el programa deberá mostrar
# 4 4
# 4 5
# 4 6
# 5 4
# 5 5
# 5 6
# 6 4
# 6 5
# 6 6


# m = int(input("Ingrese un número M: "))
# n = int(input("Ingrese un número N: "))


# for i in range(m,n+1):
#     for j in range(m,n+1):
#         print(i,j)

# con while:

# m = int(input("Ingrese un número M: "))
# n = int(input("Ingrese un número N: "))
# contador = 0

# while contador < m*2+1:
#     for i in range(m,n+1):
#         for j in range(m,n+1):
#             print(i,j)
#             contador+=1    

########################################################################################################################################################################
# b) Cambiar el programa para que use sólo un ciclo en vez de dos.

m = int(input("Ingrese un número M: "))
n = int(input("Ingrese un número N: "))

i=m
j=m
flag=True

while(i<=n):
    if(j<=n):
        print(i,j)
        j=j+1
    else:   # cuando el "j" completa su recorrido, pasa al else donde "reinicia" la secuencia.
        j=m
        flag=False
    if(flag==False): # Antes se cambia el flag para poder pasar un if que moverá un paso del ciclo while y aumenta en uno la primer columna ("i"). Luego devuelve el flag a "False".
        i=i+1
        flag=True


