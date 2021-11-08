# Ejercicio 9

# a) Hacer una función que reciba dos enteros y retorne el mayor.

# def mayor (a,b):
#     if a > b:
#         return a
#     elif b > a:
#         return b
#     else:
#         return "Ninguno, porque pusiste 2 iguales rey/reina."


# n = int(input("Ingrese un primer número entero: "))
# m = int(input("Ingrese un segundo número entero: "))

# print("El número mayor entre",n,"y",m,"es",mayor(n,m))

########################################################################################################################################################################
# b) Hacer una función que reciba tres enteros y retorne el mayor.

# def mayorTres (a,b,c):
#     if a > b and a > c:
#         return a
#     elif b > a and b > c:
#         return b
#     elif c > a and c > b:
#         return c
#     else:
#         return "Ninguno, porque pusiste 3 iguales rey/reina."


n = int(input("Ingrese un primer número entero: "))
m = int(input("Ingrese un segundo número entero: "))
o = int(input("Ingrese un tercer número entero: "))

print("El número mayor entre",n,",",m,"y",o,"es",mayorTres(n,m,o))
