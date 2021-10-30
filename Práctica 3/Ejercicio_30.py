# Ejercicio 30

# Hacer un programa que solicite dos cadenas, nombre y apellido y arme el legajo de estudiantes
# de la universidad de la siguiente manera:
# Los 3 primeros números del legajo coinciden con los primeros del dni luego "_", luego las 3
# primeras letras del apellido y por ultimo la primera y ultima del nombre.
# Por ejemplo:
# JavierRodriguez 38946702
# Legajo: 389_rodjr

nombre = input("Por favor ingrese su Nombre: ")
apellido = input("Por favor ingrese su Apellido: ")
dni = input("Ahora ingrese por favor su DNI: ")

print ("Armando su Legajo. Por favor aguarde un instante...")

limite_dni_y_apellido = 3
legajo_dni = ""
separador = "_"
legajo_apellido = ""
legajo_nombre = ""

for numero in dni:
    legajo_dni += numero.lower()
    if len(legajo_dni) == limite_dni_y_apellido:
        break

for letra in apellido:
    legajo_apellido += letra.lower()
    if len(legajo_apellido) == limite_dni_y_apellido:
        break

cont=0
for letra in nombre:
    if(cont==0 or cont==len(nombre)-1):
        legajo_nombre += letra.lower()
    cont=cont+1

print("Su legajo es: ",legajo_dni + separador + legajo_apellido + legajo_nombre)