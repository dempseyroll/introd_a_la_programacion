# Ejercicio 10

# Hacer en pseudocodigo y luego un programa que calcule el importe que se le facturará a un
# cliente por consumo de electricidad sabiendo que la compañía que se la provee cobra una tarifa
# fija de 480 pesos que incluye los primeros 200 KW consumidos y los KW excedentes se los cobra
# a 25,5 pesos el KW, además se agregan $78 de impuestos. Se leen los valores del medidor al
# comienzo y al fin del período.

tarifa_fija_200KW= 480
impuestos= 78
cada_kw= 25.5

kw=int(input("Ingrese los kw consumidos: "))

if kw<=200:
    print("Deberá pagar $", tarifa_fija_200KW)
else:
    calculo= (kw - 200) * 25.5 + tarifa_fija_200KW + impuestos
    print("Deberá pagar $", calculo)
