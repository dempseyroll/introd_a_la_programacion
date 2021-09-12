# Ejercicio 6

# a) Escribir en papel un programa que pida al usuario dos números, y que muestre en
# pantalla al mayor de ambos. Luego hacer 3 corridas de escritorio, luego pasarlo a
# Python y por último correr el programa con los valores iniciales de las corridas y
# vericar que funciona como se esperaba.
# b) Ídem anterior pero para encontrar el menor

nro_uno= int(input("Ingrese un numero: "))
nro_dos= int(input("Ingrese un segundo numero: "))

if nro_uno > nro_dos:
    print ("El mayor es: ", nro_uno)
else:
    if nro_dos > nro_uno:
        print("El mayor es: ", nro_dos)
    else:
        print("Ambos son iguales")
