# Ejercicio 29

# Hacer un programa que genere una clave provisoria para la gestión online de clientes de una
# empresa. El programa le pedirá el apellido y generará una clave de 5 caracteres, tomará las
# primeras 4 consonantes de la palabra ingresada. Cuando las consonantes no alcancen a 4, las
# faltantes las reemplazará por "*". Ejemplos:
# clemente CLMN
# rivera RVR*
# oreo R***
# La clave se completará con 1 dígito generado aleatoriamente entre 0 y 9.
# Ejemplos: CLMN1 RVR*4 R***7

import random

apellido = input("Por favor ingrese su apellido completamente en letra minúscula: ")
vocales = "aeiou"
digito_random = random.randrange(0,10)
clave = ""
limite = 4

print("Generando clave... aguarde un momento por favor...")

for letra in apellido:
    if letra not in vocales:
       # letra = letra.upper()
        clave += letra.upper()
        if len(clave) == limite:
            break

control_clave = len(clave)    

if len(clave) == limite:
    clave += str(digito_random)
    clave = clave.upper()
    print("La clave generada es: ",clave)
else:
    while control_clave < limite:
        clave += "*"
        control_clave += 1
    print("La clave generada es: ",clave + str(digito_random))

