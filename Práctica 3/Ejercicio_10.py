# Ejercicio_10
# Hacer un programa que permita al usuario elegir un número positivo n y luego muestre en
# pantalla el producto (es decir, la multiplicación) de los numeros entre 1 y n
# Pruebas: 4, 10, 27

# n = int(input("Ingrese un número n: "))

# if n < 0:
#     print("ERROR - No es un número positivo")

# else:
#     for numero in range(1,n):
#         producto = numero * (numero + 1)
#         print("El Producto de",numero,"X",numero +1,"es:",producto)

# NOTA: Supongo que era así el ejercicio, con este código me dio el resultado a como lo entendí en el enunciado.

# Ahora con "while":

n = int(input("Ingrese un número n: "))
multiplicador = 1

if n < 0:
    print("ERROR - No es un número positivo")

while multiplicador < n:
    producto = multiplicador * (multiplicador + 1) 
    print("El Producto de",multiplicador,"X",multiplicador + 1,"es:",producto)
    multiplicador+=1

# Ídem a lo dicho en el comentario "NOTA" anterior.