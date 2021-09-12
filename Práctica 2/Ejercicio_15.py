# Ejercicio 15

# Escribir un programa que pida al usuario tres enteros y los guarde en tres variables a, b y c.
# El programa deberá luego hacer que en la variable a quede el menor de los valores recibidos, en
# b el intermedio y en c el mayor (es decir, ordenará los valores).

a = int(input("Ingrese el valor A: "))
b = int(input("Ingrese el valor B: "))
c = int(input("Ingrese el valor C: "))

#Inicial
print("Los valores ingresados son:\nA:",a,"\nB:",b,"\nC:",c)

if(a>b):
    aux=a
    a=b
    b=aux
if(a>c):
    aux=a
    a=c
    c=aux
if(b>c):
    aux=b
    b=c
    c=aux

#Final
print("Los valores ordenados son:\nA:",a,"\nB:",b,"\nC:",c)


