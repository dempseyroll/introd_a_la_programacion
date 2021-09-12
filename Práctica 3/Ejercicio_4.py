# Ejercicio 4

# a) Hacer un programa que muestre, mediante un ciclo, los números desde el 5 hasta el
# 11 salteando de a 2 elementos (5, 7, 9 y 11)
# b) Hacer un programa que permita al usuario elegir un número m y un n y luego
# muestre todos los naturales entre m y n, pero salteando de a 3. Por ejemplo, si el
# usuario ingresara un n igual a 2 y un m igual a 14, el programa deberá mostrar
# 2, 5, 8, 11, 14.
# c) Hacer un programa que permita al usuario elegir un número n, un m y un p y
# luego muestre todos los naturales entre m y n, pero salteando de a p números. Por
# ejemplo, si el usuario ingresara un n igual a 2 y un m igual a 14, y un p igual a 4,
# el programa deberá mostrar 2, 6, 10, 14.

# a)

# for num in range(5,12,2):
#    print(num)

# b)

# m = int(input("Ingrese un num m: "))
# n = int(input("Ingrese un num n: "))

# if n < m:
#    for num in range(n,m+1,3):
#        print(num)
# else:
#    for num in range(m,n+1,3):
#        print(num)

# c)

n = int(input("Ingrese un número n: "))
m = int(input("Ingrese un número m: "))
p = int(input("Ingrese un número p: "))

for num in range(n,m+1,p):
    print(num)