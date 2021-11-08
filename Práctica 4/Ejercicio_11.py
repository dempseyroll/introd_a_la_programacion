# Ejercicio 11

# a) Hacer una función que sume los divisores propios de un número.

# def sumaDivisoresPropios(a):
#     suma = 0
#     for num in range(1,a):
#         if a % num == 0:
#             suma += num
#     return suma

# n = int(input("Ingrese un número: "))

# print("La suma de los divisores propios de",n,"es",sumaDivisoresPropios(n))

########################################################################################################################################################################
# b) Hacer una función que indique si un número es perfecto. Número perfecto: a es
# perfecto si la suma de sus divisores propios es igual a a.

# Ejemplos de número perfecto: 6, 28 y 496

# def esPerfecto(a):
#     suma = 0
#     for num in range(1,a):
#         if a % num == 0:
#             suma += num
#     if suma == a:
#         return print(a,"es Perfecto")
#     else:
#         return print(a,"no es Perfecto")

# n = int(input("Ingrese un número: "))

# esPerfecto(n)

########################################################################################################################################################################
# c) Hacer una función que determine si un número ingresado por el usuario es un número
# abundante. Número abundante: todo número natural que cumple que la suma de sus
# divisores propios es mayor que el propio número. Por ejemplo, 12 es abundante ya
# que sus divisores son 1, 2, 3, 4 y 6 y se cumple que 1+2+3+4+6=16, que es mayor
# al propio 12.

# Ejemplo de número abundante: 12

# def esAbundante(a):
#     suma = 0
#     for num in range(1,a):
#         if a % num == 0:
#             suma += num
#     if suma > a:
#         return print(a,"es Abundante")
#     else:
#         return print(a,"no es Abundante")

n = int(input("Ingrese un número: "))

esAbundante(n)