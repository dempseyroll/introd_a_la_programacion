# Ejercicio 21

# Hacer un programa que permita al usuario jugar al piedra, papel o tijera contra la computadora. Se debe jugar al mejor de 5, es decir, si uno de los participantes consigue 3 victorias el
# juego termina

import random

# opciones
piedra = 0
papel = 1
tijera = 2

# controles
victoria = 3
juego = 5
contador = 0
ganados = 0
perdidos = 0
empatados = 0


while contador < juego:
    jugador = int(input("""Juguemos! Piedra, papel o tijera? Elegí tu opción:
0) piedra
1) papel
2) tijera
"""))
    rival = random.randrange(0,3)
    if jugador == rival:
        print ("Empatamos! ambos elegimos",jugador,". Volvemos a jugar.")
        empatados += 1
        contador += 1
        if empatados == 3:
            print("EMPATAMOS 3 veces! No podemos definir un ganador. FIN DEL JUEGO. Gracias por jugar.")
            break
    elif (jugador == 0 and rival == 2) or (jugador == 1 and rival == 0) or (jugador == 2 and rival == 1):
        print ("GANASTE! Elegiste",jugador,"y yo",rival,".")
        ganados += 1
        contador += 1
        if ganados == victoria:
            print("Me derrotaste! Muchas gracias por jugar.")
            break
    elif (jugador == 2 and rival == 0) or (jugador == 0 and rival == 1) or (jugador == 1 and rival == 2):
        print ("PERDISTE! Elegiste",jugador,"y yo",rival,".")
        perdidos += 1
        contador += 1
        if perdidos == 3:
            print("Te derroté. Suerte la próxima!")
            break


## No hago el ejercicio 22 porque me pareció muy boludo.