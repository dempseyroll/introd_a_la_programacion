# Ejercicio 7

# a) Escribir una función que se llame elevarAlCubo que tome un número y retorne el
# valor de ese número al cubo.
# b) Guardar el ejercicio anterior en un archivo llamado funcionCubo.py
# c) Correr el siguiente código en un archivo nuevo y chequear que los resultados sean
# correctos:
# print(0, "al cubo:", elevarAlCubo(0))
# print(1, "al cubo:", elevarAlCubo(1))
# print(2, "al cubo:", elevarAlCubo(2))
# print(3, "al cubo:", elevarAlCubo(3))
# print(4, "al cubo:", elevarAlCubo(4))
# print(5, "al cubo:", elevarAlCubo(5))
# print(6, "al cubo:", elevarAlCubo(6))
# print(-1, "al cubo:", elevarAlCubo(-1))
# print(-2, "al cubo:", elevarAlCubo(-2))
# print(-3, "al cubo:", elevarAlCubo(-3))
# print(-4, "al cubo:", elevarAlCubo(-4))
# print(-5, "al cubo:", elevarAlCubo(-5))

import funcioncubo

n = int(input("Por favor ingrese un número: "))

print(funcioncubo.elevarAlCubo(n))


## Hechos todos. la función está en el archivo funcioncubo.py y la prueba del punto c) en el archivo ejercicio_7c.py
