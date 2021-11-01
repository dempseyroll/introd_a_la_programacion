# Ejercicio 5

# Definir una función que devuelva el valor absoluto de un número. (Hacerlo sin utilizar la
# función abs)

def absoluto(numero):
    abs = 0
    if numero < 0:
        abs = numero + (-numero * 2 )
    elif numero > 0:
        abs = numero
    else:
        abs = 0
    return abs

num = int(input("Ingrese un número para calcular su módulo: "))

print("El valor absoluto de", num, "es", absoluto(num))
