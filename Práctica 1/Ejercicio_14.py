#Ejercicio 14

#Una empresa telefónica desea un programa para calcular el importe de sus clientes. Sabiendo que el
#costo por comunicación es de $7 y por cada segundo se cobra $0, 5 hacer dicho programa. Se deben
#ingresar la cantidad de llamadas realizadas y el tiempo total de comunicación, el programa debe devolver
#el precio a cobrar.

comunicacion=7
cada_segundo=0.5

cant_llamadas=int(input("Ingrese la cantidad de llamadas realizadas: "))
tiempo_total_de_com=int(input("Ingrese el tiempo total de comunicacion por todas las llamadas: ")) #El ejercicio no lo especifica,
#por lo cual yo asumo que es en segundos mi ciela

Precio_a_cobrar=cant_llamadas * comunicacion +(cada_segundo * tiempo_total_de_com)

print("El precio a cobrar es: ",Precio_a_cobrar,"pesos")


#Creo que está bien.