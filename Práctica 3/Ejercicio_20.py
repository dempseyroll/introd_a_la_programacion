# Ejercicio 20

# Hacer un programa que simule el juego de la quiniela. El usuario debe elegir un número del
# 0 al 99 y un monto a apostar, si acierta el número gana 70 veces lo apostado. (El número de la
# suerte debe ser elegido al azar)

import random

numero = int(input("Elija por favor un número del 00 al 99: "))
apuesta = int(input("Por favor ingrese su apuesta: "))
quiniela = random.randrange(00,100)

if numero == quiniela:
    premio = apuesta * 70
    print("GANASTE! Tu premio es de",premio,"pesos!")
else:
    print("No tuviste suerte... El número ganador fue",quiniela)
