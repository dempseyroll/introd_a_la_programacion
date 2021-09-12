# Ejercicio 17

# Escribe un programa que pida los coeficientes de una ecuación de primer grado (ax + b = 0)
# y escriba la solución. Recuerda que una ecuación de primer grado puede no tener solución, tener
# una solución única, o que todos los números reales sean solución.

a = float(input("Ingrese el valor de A: "))
b = float(input("Ingrese el valor de B: "))

print ("ingreso A=",a,"B=",b)

if(a!=0):
    print("La solucion es: ",-b/a)
else:
    if(b==0):
        print("Tiene infinitas soluciones")
    else:
        print("No tiene solucion")
