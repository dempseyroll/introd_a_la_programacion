# Ejercicio 11
# Hacer un programa que reciba un número m y determine el primer n para el cual la suma
# 1+2+...+n > m. Por ejemplo, si el usuario ingresa 11 se deberá retornar 5 ya que 1+2+3+4 =
# 10 < 11 y 1 + 2 + 3 + 4 + 5 = 15 > 11
# Pruebas: 11, 20, 45

# m = int(input("Ingrese un número m: ")) # Limite hasta donde se intentará sumar todos los nros. desde 1 a n

# candidato=0
# resultado=0
# if m <= 0:
#     print("ERROR -",m,"no es un número positivo")

# else:
#     while resultado < m:
#         resultado = resultado + candidato
#         if resultado > m:
#             print("El numero de corte es:",candidato,",","ya que",resultado,"es mayor a",m)
#         candidato = candidato + 1


# con "for":

m = int(input("Ingrese un número m: ")) # Limite hasta donde se intentará sumar todos los nros. desde 1 a n

resultado=0
if m <= 0:
    print("ERROR -",m,"no es un número positivo")

else:
    for numero in range(1,m):
        resultado = resultado + numero
        if resultado > m:
            print("El numero de corte es:",numero,",","ya que",resultado,"es mayor a",m)
            break