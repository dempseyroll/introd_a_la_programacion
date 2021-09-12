#Ejercicio 18

#Escribir un programa en Python que pida al usuario una cantidad de segundos y muestre en pantalla
#la cantidad de días, minutos y segundos que representa. Por ejemplo, si el usuario ingresa 86461 segundos
#el programa debe mostrar por pantalla: 1 día 0 horas 1 minuto 1 segundo.

segundos=int(input("Ingrese una cantidad de segundos: "))

# 1 día = 86400 segs
# 1 hora = 3600 segs
# 1 minuto = 60 segs

dias= segundos / 86400
resto= segundos % 86400
horas= resto / 3600
resto= resto % 3600
minutos= resto / 60
resto= resto % 60
segundos= resto


print("""La cantidad de segundos ingresada equivale a
""", dias,"dias\n",horas,"horas\n",minutos,"minutos\n",segundos,"segundos.")