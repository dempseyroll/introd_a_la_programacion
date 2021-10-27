# Ejercicio 23

# a) Escribir un programa que pida al usuario un número n y muestre una línea de n
# asteriscos. Ejemplo, para n = 8, el programa deberá mostrar:
# ********

# asteriscos = int(input("Ingrese un número de asteriscos: "))

# for i in range(1,asteriscos+1):
#     print("*",end="")

## con while:

# asteriscos = int(input("Ingrese un número de asteriscos: "))
# contador = 0

# while contador < asteriscos:
#     print("*",end="")
#     contador += 1

####################################################################################################################################
# b) Escribir un programa que pida al usuario un número n y muestre n líneas de
# 1, 2, 3, ...n asteriscos respectivamente. Ejemplo, para n = 5, el programa deberá
# mostrar:
# *
# **
# ***
# ****
# *****

# n = int(input("Ingrese un número de asteriscos: "))
# asteriscos = "*"

# for i in range(1,n+1):
#     print(asteriscos)
#     asteriscos += "*"

## con while

# n = int(input("Ingrese un número de asteriscos: "))
# asteriscos = "*"
# contador = 0

# while contador < n:
#     print(asteriscos)
#     asteriscos += "*"
#     contador += 1

####################################################################################################################################
# c) Escribir un programa que pida al usuario un número n y muestre n líneas de 2n − 1
# asteriscos respectivamente. Ejemplo, para n = 5, el programa deberá mostrar:
# *
# ***
# *****
# *******
# *********

# n = int(input("Ingrese un número de asteriscos: "))
# asteriscos = "*"


# for i in range(1,n+1):
#     print(asteriscos)
#     asteriscos = asteriscos + "**"

## con while

n = int(input("Ingrese un número de asteriscos: "))
asteriscos = "*"
contador = 0

while contador < n:
    print(asteriscos)
    asteriscos = asteriscos + "**"
    contador += 1
