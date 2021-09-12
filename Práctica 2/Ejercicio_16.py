# Ejercicio 16

# Un año es bisiesto si es múltiplo de 4. Pero no siempre, las excepciones son los años múltiplos
# de 100 que no son múltiplos de 400 (1900 no es bisiesto pero 2000, sí). Escribir en papel un
# programa que diga si un año ingresado por el usuario es bisiesto, realizar varias pruebas de
# escritorio, luego pasarlo a Python y vericar los resutlados.

anio=int(input("Ingrese un año: "))

if anio < 1000:
    print("debe ser un año de 4 cifras. Error.")

if anio % 4 == 0:
    if anio % 100 == 0 and anio % 400 != 0:
        print(anio,"no es bisiesto")
    else:
        print(anio,"es bisiesto")
else:
    print(anio,"no es bisiesto")