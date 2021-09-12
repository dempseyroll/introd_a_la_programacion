#Ejercicio 13, me salteo el 11 porque es re pete.

#Suponga que una persona desea invertir su capital en un banco y quiere saber cuánto dinero tendrá en
#su cuenta si el banco incrementa el 6 % mensual(no acumulativo). Se le debe pedir al usuario el capital
#a invertir y la cantidad de meses.

capital=int(input("Ingrese su capital a invertir: "))
cant_meses=int(input("Ingrese la cantidad de meses que quiere invertir: "))

calculo=(capital*6/100) * cant_meses + capital

print("Usted tendrá en su cuenta: ",calculo,"de pesos")