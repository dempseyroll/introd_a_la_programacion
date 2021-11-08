# Ejercicio 12

# Hacer una función que indique si un número es Poderoso: Número poderoso: es un número
# natural n que cumple que todos sus divisores primos al cuadrado también son divisores, es decir,
# si p es un divisor primo entonces p2 también lo es. Por ejemplo, el número 36 es un número
# poderoso ya que los únicos primos que son divisores suyos son 2 y 3 y se cumple que 4 y 9
# también son divisores de 36.

# def esPoderoso(numero):
#     acumulador = 0
#     for num in range(2,numero+1):
#         if numero % num == 0 and primoONo(num):
#             candidato = num**2
#             if numero % candidato == 0:
#             #primoONo(candidato) == False and 
#                 acumulador += 1
#     if acumulador != 0:
#         return print(numero,"es Poderoso")
#     else:
#         return print(numero,"no es Poderoso")

# def primoONo(num_entero):
#     contador = 0
#     for num in range(1,num_entero+1):
#         if num_entero % num == 0:
#             contador += 1
#     if contador > 2:
#         return False # resultado número NO primo (tiene más divisores además del 1 y dividirse por sí mismo)
#     else:    
#         return True # resultado número primo

p = int(input("Ingrese un número para evaluar: "))

esPoderoso(p)