# Ejercicio 2

# Un ciudadano argentino está exento de votar en estos casos:
# Tiene más de 70 años
# Tiene entre 18 y 70 años pero se encuentra a más de 500 km del centro de votación.
# Suponiendo que las variables edad y distancia representan la edad y la distancia del ciudadano,
# escribir la expresión lógica que representa esta situación.

edad_limite = 70
distancia_limite = 500

edad_votante= int(input("Ingrese la edad: "))


if edad_votante > 70:
    print("Queda exento de la obligación de votar, usted es mayor de 70 años")
else:
    distancia= int(input("Ingrese la distancia: "))
    if edad_votante>=18 and distancia>distancia_limite:
        print("Queda exento de la obligación de votar, usted se encuentra a más de 500 km del centro.\nTampoco admitimos tetones.")
    else:
        print("Usted puede votar, no es un gordito tetón")