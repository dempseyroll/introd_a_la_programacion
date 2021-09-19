#Ejercicio 13
# a) Hacer un programa que permita al usuario elegir un número positivo n y luego
# muestre en pantalla las n primeras sumas parciales de la sucesión an = 2n. Es decir,
# 2 6 12 20...

# e) ¿A qué valor se va acercando la suma del inciso anterior a medida que utilizamos
# un valor alto de n? --> Entiendo que se va a acercando cada vez más al 0.


# n = int(input("Ingrese un número n: "))

# if n <= 0:
#     print("ERROR -",n,"no es un número positivo")

# else:
#     for i in range(1,n+1):
#         calcula_término = i * (i + 1)
#         print("El término",i,"de las sumas parciales de la sucesión an = 2n es",calcula_término)

# a) con "while":

# n = int(input("Ingrese un número n: "))
# contador=1

# if n <= 0:
#     print("ERROR -",n,"no es un número positivo")

# else:
#     while contador <= n:
#         calcula_término = contador * (contador + 1)
#         print("El término",contador,"de las sumas parciales de la sucesión an = 2n es",calcula_término)
#         contador+=1

###################################################################################################################################
# b) Idem anterior para la sucesión an = n^2

# n = int(input("Ingrese un número n: "))

# if n <= 0:
#     print("ERROR -",n,"no es un número positivo")

# else:
#     for i in range(1,n+1):
#         calcula_término = i ** (i + 1)
#         print("El término",i,"de las sumas parciales de la sucesión an = 2n es",calcula_término)

# b) con "while":

# n = int(input("Ingrese un número n: "))
# contador=1

# if n <= 0:
#     print("ERROR -",n,"no es un número positivo")

# else:
#     while contador <= n:
#         calcula_término = contador ** (contador + 1)
#         print("El término",contador,"de las sumas parciales de la sucesión an = 2n es",calcula_término)
#         contador+=1

###################################################################################################################################
# c) Idem anterior para la sucesión an = n^3 - n^2

# n = int(input("Ingrese un número n: "))

# if n <= 0:
#     print("ERROR -",n,"no es un número positivo")

# else:
#     for i in range(1,n+1):
#         calcula_término = i ** (i + 2) - i ** (i + 1)
#         print("El término",i,"de las sumas parciales de la sucesión an = 2n es",calcula_término)

# c) con "while":

# n = int(input("Ingrese un número n: "))
# contador=1

# if n <= 0:
#     print("ERROR -",n,"no es un número positivo")

# else:
#     while contador <= n:
#         calcula_término = contador ** (contador + 2) - contador ** (contador + 1)
#         print("El término",contador,"de las sumas parciales de la sucesión an = 2n es",calcula_término)
#         contador+=1

###################################################################################################################################
# d) Idem anterior para la sucesión an = 1 / n^2

# n = int(input("Ingrese un número n: "))

# if n <= 0:
#     print("ERROR -",n,"no es un número positivo")

# else:
#     for i in range(1,n+1):
#         calcula_término = 1 / i ** (i + 1)
#         print("El término",i,"de las sumas parciales de la sucesión an = 2n es",calcula_término)

# d) con "while":

n = int(input("Ingrese un número n: "))
contador=1

if n <= 0:
    print("ERROR -",n,"no es un número positivo")

else:
    while contador <= n:
        calcula_término = 1 / contador ** (contador + 1)
        print("El término",contador,"de las sumas parciales de la sucesión an = 2n es",calcula_término)
        contador+=1