# Ejercicio 1

# a) Hacer un programa que muestre, mediante un ciclo, los primeros 5 números naturales
#   (1, 2, 3, 4 y 5).
# b) Hacer un programa que permita al usuario elegir un número n y luego muestre los
# primeros n números naturales (1, 2, · · · , n).

# a)

# for num in range(1,6,1):
#    print(num)

# b)

n= int(input("Ingrese un número entero: "))

for num in range(1,n+1,1):
    print(num)
