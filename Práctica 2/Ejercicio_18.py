# Ejercicio 18

# Una función cuadrática se escribe como ax2+bx+c. La misma puede tener una, dos o ninguna
# raíz. Escribir un programa que pida al usuario los datos de la misma, es decir, a, b y c, y muestre
# todas sus raíces, o el mensaje "No tiene raíces" cuando corresponda. Recordar que las raíces están
# dadas por la fórmula

#   −b ± √b2 − 4ac
#    2a

print("Este programa calcula ax^2 + bx + c = 0")

a = float(input("Ingrese el valor de a"))
b = float(input("Ingrese el valor de b"))
c = float(input("Ingrese el valor de c"))
print("ingreso a=",a,"b=",b,"c=",c)
if(a != 0):

    discriminante = b*b - 4*a*c

    #precondicion a != 0
    if(discriminante > 0):
        x1 = (-b +(discriminante)**0.5)/(2*a)
        x2 = (-b -(discriminante)**0.5)/(2*a)
        print("Las soluciones son: ", x1, " y ", x2)
    else:
        if(discriminante==0):
            x1 = -b/(2*a)
            print("La solucion es: ", x1)
        #caso discriminante < 0
        else:
            print("La ecuacion no tiene solucion")
