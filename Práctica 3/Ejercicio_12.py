# Ejercicio 12
# a) Hacer un programa que permita al usuario elegir un número positivo n y luego
# muestre en pantalla los n primeros términos de la sucesión an = 2n. Es decir 2, 4,
# 6...

# n = int(input("Ingrese un número n: "))

# if n <= 0:
#     print("ERROR -",n,"no es un número positivo")

# else:
#     for i in range(1,n+1):
#         calcula_término = 2 * i
#         print("El término",i,"de la sucesión an = 2n es",calcula_término)

# a) con "while":

# n = int(input("Ingrese un número n: "))
# contador=1

# if n <= 0:
#     print("ERROR -",n,"no es un número positivo")

# else:
#     while contador <= n:
#         calcula_término = 2 * contador
#         print("El término",contador,"de la sucesión an = 2n es",calcula_término)
#         contador+=1

###################################################################################################################################
# b) Idem anterior para la sucesión an = 2n − 1.

# n = int(input("Ingrese un número n: "))

# if n <= 0:
#     print("ERROR -",n,"no es un número positivo")

# else:
#     for i in range(1,n+1):
#         calcula_término = 2 * i - 1
#         print("El término",i,"de la sucesión an = 2n - 1 es",calcula_término)

# b) con "while":

# n = int(input("Ingrese un número n: "))
# contador=1

# if n <= 0:
#     print("ERROR -",n,"no es un número positivo")

# else:
#     while contador <= n:
#         calcula_término = 2 * contador - 1
#         print("El término",contador,"de la sucesión an = 2n es",calcula_término)
#         contador+=1

###################################################################################################################################
# c) Idem anterior para la sucesión an = n^2

# n = int(input("Ingrese un número n: "))

# if n <= 0:
#     print("ERROR -",n,"no es un número positivo")

# else:
#     for i in range(1,n+1):
#         calcula_término = i**2
#         print("El término",i,"de la sucesión an = 2n es",calcula_término)

# c) con "while":

# n = int(input("Ingrese un número n: "))
# contador=1

# if n <= 0:
#     print("ERROR -",n,"no es un número positivo")

# else:
#     while contador <= n:
#         calcula_término = contador ** 2
#         print("El término",contador,"de la sucesión an = 2n es",calcula_término)
#         contador+=1

###################################################################################################################################
# d) Idem anterior para la sucesión an = n^3 − n^2

# n = int(input("Ingrese un número n: "))

# if n <= 0:
#     print("ERROR -",n,"no es un número positivo")

# else:
#     for i in range(1,n+1):
#         calcula_término = i**3 - i**2
#         print("El término",i,"de la sucesión an = 2n es",calcula_término)

# d) con "while":

# n = int(input("Ingrese un número n: "))
# contador=1

# if n <= 0:
#     print("ERROR -",n,"no es un número positivo")

# else:
#     while contador <= n:
#         calcula_término = contador ** 3 - contador ** 2
#         print("El término",contador,"de la sucesión an = 2n es",calcula_término)
#         contador+=1

###################################################################################################################################
# e) Idem anterior para la sucesión an = 1/n^2

# n = int(input("Ingrese un número n: "))

# if n <= 0:
#     print("ERROR -",n,"no es un número positivo")

# else:
#     for i in range(1,n+1):
#         calcula_término = 1 / i**2
#         print("El término",i,"de la sucesión an = 2n es",calcula_término)

# e) con "while":

n = int(input("Ingrese un número n: "))
contador=1

if n <= 0:
    print("ERROR -",n,"no es un número positivo")

else:
    while contador <= n:
        calcula_término = 1 / contador ** 2
        print("El término",contador,"de la sucesión an = 2n es",calcula_término)
        contador+=1