# Ejercicio 12

# Un profesor clasifica las notas de sus alumnos de la siguiente manera:
#   1-3 Reprobado
#   4-6 Debe rendir examen final
#   7-10 Eximido
#   a) Escribir un programa que indique la clasificación de una nota.
#   b) Escribir un programa que pida 3 notas, calcule el promedio e indique la clasificación
# del mismo.

nota_1= int(input("Ingrese nota 1: "))
nota_2= int(input("Ingrese nota 2: "))
nota_3= int(input("Ingrese nota 3: "))
promedio= (nota_1+nota_2+nota_3) / 3

if promedio >=7:
    print(promedio, "Eximido")
elif promedio >= 4 and promedio <= 6:
    print(promedio, "Debe rendir examen final")
else:
    print(promedio, "Reprobado")

