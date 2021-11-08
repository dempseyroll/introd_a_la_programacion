# Ejercicio 8

# a) Escribir una función que tome un parámetro de tipo entero y devuelva la cantidad
# de divisores positivos de ese número.

# def divisoresPositivos(num_entero):
#    contador = 0
#    for num in range(1,num_entero+1):
#         if num_entero % num == 0:
#             contador += 1
#    return contador

# numero = int(input("Ingrese un número entero: "))

## divisoresPositivos(numero)
## Lo comenté porque estaba llamando 2 veces a la función al pedo, igual no cambió nada ya que obtuve el mismo resultado y funciona,
## pero dejé el código "más lindo"

# print("La cantidad de divisores de",numero,"es",divisoresPositivos(numero))

########################################################################################################################################################################
# b) Escribir una función que tome un parámetro de tipo entero y devuelva el valor True
# si se la llama con un número primo y False en caso contrario.

# def primoONo(num_entero):
#     contador = 0
#     for num in range(1,num_entero+1):
#         if num_entero % num == 0:
#             contador += 1
#     if contador > 2:
#         return False # resultado número NO primo (tiene más divisores además del 1 y dividirse por sí mismo)
#     else:    
#         return True # resultado número primo


# numero = int(input("Ingrese un número entero: "))

# print(primoONo(numero))

########################################################################################################################################################################
# c) ¿Cuál es el número primo más grande que encontraste?

## Khé?

########################################################################################################################################################################
# d) Hacer una función (no pura) que reciba un entero e imprima sus factores primos.
# Por ejemplo para a = 20 la función debe mostrar 2 y 5.
# Nota: Los números primos son aquellos cuyos únicos divisores positivos son ellos
# mismos y el 1

# def factoresPrimos(num_entero):
#     #divisores_primo = 2
#     #contador = 0
#     factores = ""
#     for num in range(2,num_entero+1):
#         if num_entero % num == 0 and primoONo(num):
#             factores += str(num) + " "
#     return factores          
    


numero = int(input("Ingrese un número entero: "))

print("Los factores primos de",numero,"son",factoresPrimos(numero))