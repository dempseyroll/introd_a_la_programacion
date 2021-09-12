# Ejercicio 8

# a) Hacer un programa que reciba un número n y muestre todas las potencias de 2
# menores a n. Por ejemplo, si el usuario ingresa 20, el programa mostrará: 1 2 4 8
# 16. Ayuda: pensar primero si sería más práctico utilizar la sentencia while o for.
# b) Hacer un programa que reciba un número n (n > 0) y muestre las n primeras
# potencias de 2. Por ejemplo, si el usuario ingresa 6, el programa mostrará: 1 2 4 8
# 16 32.
# c) Hacer un programa que reciba un número n (n > 0) y muestre las n primeras
# potencias de n. Por ejemplo, si el usuario ingresa 4, el programa mostrará: 1 4 27
# 256. Es decir, 1^1 2^2 3^3 4^4.

# a)

# n = int(input("Ingrese un número: "))
# cont = 0

# while 2 ** cont < n:
#    print(2 **cont)
#    cont += 1

# b)

# n = int(input("Ingrese un número: "))
# cont = 0

# while 2 ** cont < 2**n:
#    print(2 ** cont)
#    cont = cont + 1

# c)

n = int(input("Ingrese un número: "))
cont = 1
base=1
while base ** cont <= n**n:
    print(base ** cont)
    cont = cont + 1
    base = base + 1

