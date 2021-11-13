# Ejercicio 14

# Hacer un programa que solicite al usuario un número entero positivo e indique cuál es el
# número primo mayor más cercano. Usar funciones. Por ejemplo, si el usuario ingresa 24, el
# programa devolverá 29 (29 es el número primo más cercano mayor que 24). Si el usuario ingresa
# 5 el programa devolverá 7.

## Función

def mayorPrimoCercano(numero):
    for num in range(numero+1, numero*2):
        if primoONo(num):
            return num

def primoONo(num_entero):
    contador = 0
    for num in range(1,num_entero+1):
        if num_entero % num == 0:
            contador += 1
    if contador > 2:
        return False # resultado número NO primo (tiene más divisores además del 1 y dividirse por sí mismo)
    else:    
        return True # resultado número primo


## Programa principal

n = int(input("Ingrese un número entero positivo por favor: "))

print("El número primo mayor más cercano a",n,"es",mayorPrimoCercano(n))