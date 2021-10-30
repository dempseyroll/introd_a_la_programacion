# Ejercicio 28

# Escribir un programa que pida al usuario una cadena y una letra y reemplace las apariciones
# de dicha letra por asteriscos. Por ejemplo, si el usuario ingresa:
# "programador"
# "r"
# el programa debe devolver "p ∗ og ∗ amado∗"

palabra = input("Ingrese una palabra por favor: ") 
letra = input("Ingrese una letra ahora: ")
palabra_nueva = ""

for i in palabra:
    if i == letra:
        i = "*"
    palabra_nueva += i

print("La palabra nueva formada es:", palabra_nueva)