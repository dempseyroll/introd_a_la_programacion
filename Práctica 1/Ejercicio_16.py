#Ejercicio 16

#Determinar cuántos segundos tiene una hora, y cuántos tiene un día.
#Escribir una expresión matemática que transforme un lapso de tiempo expresado en segundos a uno
#expresado en minutos.
#Escribir otra para transformar a horas y una última que transforme a días.
#Escribir un programa en Python que pida al usuario una cantidad de segundos y muestre cuantos
#minutos son, así como también cuantas horas y cuantos días.

segundos=int(input("Inserte cantidad de segundos: "))

hora_en_segundos=3600
dia_en_segundos=3600*24


segundos_a_minutos=segundos/60
segundos_a_horas=segundos/hora_en_segundos
segundos_a_dias=segundos/dia_en_segundos


print("Los segundos ingresados tienen equivalencias con el resto de medidas de tiempo de la siguiente forma\nMinutos: ",segundos_a_minutos,"\nHoras: ",segundos_a_horas,"\nDías: ",segundos_a_dias)