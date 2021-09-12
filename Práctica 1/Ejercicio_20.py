# Ejercicio 20

# Escribir en Python un programa que pida al usuario que ingrese tres valores y los guarde en tres
# variables, x, y, y z. El programa deberá intercambiar circularmente los valores de x, y y z, es decir, x
# debe tomar el valor de y, y el de z y z el de x. Y luego mostrarlos en pantalla:

#   El valor de x es: <x>
#   El valor de y es: <y>
#   El valor de z es: <z>
# donde en lugar de <x>, <y> y <z> deberá mostrarse el valor de las respectivas variables.

x = input("Ingrese X: ")
y = input("Ingrese Y: ")
z = input("Ingrese Z: ")

print("""Inicial:
    ""","X: ",x,"""
    ""","Y: ",y,"""
    ""","Z: ",z)

aux=y
aux_2=x
y=z
x=aux
z=aux_2

print("""Final:
    ""","X: ",x,"""
    ""","Y: ",y,"""
    ""","Z: ",z,)


# izi pisi
