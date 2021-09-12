#Ejercicio 15

#Un vendedor recibe un sueldo base de $22000 más un 10 % extra del total de sus ventas, el vendedor
#desea saber cuánto dinero obtendrá en total en el mes si ha logrado realizar 3 ventas este mes. Tenga en
#cuenta el sueldo básico y la comisión por las ventas. Hacer un programa que solicite el monto de cada
#una de las ventas del mes e indique cuál será el sueldo nal del vendedor.

sueldo_base=22000

venta1=int(input("Ingrese el monto de la 1er venta: "))
venta2=int(input("Ingrese el monto de la 2da venta: "))
venta3=int(input("Ingrese el monto de la 3er venta: "))

total_ventas=venta1+venta2+venta3
diez_porciento=total_ventas/10

sueldo_final=sueldo_base+total_ventas+diez_porciento

print("El sueldo final del vendedor será: ",sueldo_final)


#Como acá todavía no vimos ciclos for, me limité a hacerlo con 3 ventas tal como
#lo indica el ejercicio. gg izi.