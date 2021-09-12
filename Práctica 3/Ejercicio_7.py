# Ejercicio 7 - rehago algunos de los anteriores pero con while

# Ejercicio 1
# a) Hacer un programa que muestre, mediante un ciclo, los primeros 5 números naturales
# (1, 2, 3, 4 y 5).
# b) Hacer un programa que permita al usuario elegir un número n y luego muestre los
# primeros n números naturales (1, 2, · · · , n).
# Ejercicio 2
# a) Hacer un programa que muestre, mediante un ciclo, los números desde el 4 hasta el
# 7 (4, 5, 6 y 7).
# b) Hacer un programa que permita al usuario elegir un número m y un n y luego
# muestre todos los naturales entre m y n (m, m + 1, m + 2, · · · , n − 1, n). ¾Qué pasa
# si n es menor que m?
# Ejercicio 3
# a) Hacer un programa que muestre, mediante un ciclo, los 5 números naturales que le
# siguen al 10 (11, 12, · · · , 15).
# b) Hacer un programa que permita al usuario elegir un número n y luego muestre los
# 5 números naturales que le siguen a n (n + 1, n + 2, · · · , n + 5).
# c) Hacer un programa que permita al usuario elegir un número n y un número c, y
# luego muestre los c números naturales que le siguen a n (n + 1, n + 2, · · · , n + c).

# 1) a)
# n=1
# while n < 6:
#    print(n)
#    n = n + 1

# 1) b)

# n = int(input("Ingrese un número: "))
# cont = 1
# while cont <= n:
#    print(cont)
#    cont = cont + 1

# 2) a)
# cuatro = 4

# while cuatro <= 7:
#    print(cuatro)
#    cuatro += 1

# 2) b)

# m = int(input("Ingrese un número m: "))
# n = int(input("Ingrese un número n: "))

# if n < m:
#    while n <= m:
#        print(n)
#        n += 1
# else:
#    while m <= n:
#        print(m)
#        m +=1

# 3) a)
# once = 11

#while once <= 15:
#    print(once)
#    once += 1

# 3) b)

# n = int(input("Ingrese un número: "))
# n=n+1
# final = n + 5

# while n+1 <= final:
#    print(n)
#    n += 1

# 3) c)

# n = int(input("Ingrese un número n: "))
# c = int(input("Ingrese un número c: "))
# n = n+1
# limite= n+c

# while n < limite:
#    print(n)
#    n += 1
