# Ejercicio 3

# a) Hacer un programa que muestre, mediante un ciclo, los 5 números naturales que le
# siguen al 10 (11, 12, · · · , 15).
# b) Hacer un programa que permita al usuario elegir un número n y luego muestre los
# 5 números naturales que le siguen a n (n + 1, n + 2, · · · , n + 5).
# c) Hacer un programa que permita al usuario elegir un número n y un número c, y
# luego muestre los c números naturales que le siguen a n (n + 1, n + 2, · · · , n + c).

# a)

# for num in range(11,16,1):
#    print(num)

# b)

# n = int(input("Ingrese un número: "))

# for num in range(n+1,n+6,1):
#    print(num)

# c)

n = int(input("Ingrese un número n: "))
c = int(input("Ingrese un número c: "))

for num in range(n+1,n+c,1):
    print(num)