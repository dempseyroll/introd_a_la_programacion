# Ejercicio 2

# a) Hacer un programa que muestre, mediante un ciclo, los números desde el 4 hasta el
#   7 (4, 5, 6 y 7).
# b) Hacer un programa que permita al usuario elegir un número m y un n y luego
# muestre todos los naturales entre m y n (m, m + 1, m + 2, · · · , n − 1, n). ¾Qué pasa
# si n es menor que m?

# a)

# for num in range(4,8,1):
#    print(num)

# b)

m = int(input("Ingrese un numero m: "))
n = int(input("Ingrese un número n: "))

if n < m:
    for i in range(m,n-1,-1):
        print(i)
else:
    for num in range(m,n+1,1):
        print(num)