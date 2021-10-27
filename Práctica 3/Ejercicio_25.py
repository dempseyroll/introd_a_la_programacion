# Ejercicio 25

# Hacer una programa que, dada una palabra, la escriba recuadrada por asteriscos. Por ejemplo,
# si la palabra es "Ganaste", el programa debería escribir:
# ***********
# * Ganaste *
# ***********

# palabra = input("Ingrese una palabra: ")
# asterisco = "*"

# print(asterisco * len(palabra) + "****\n*"," ",palabra," ",asterisco,"\n",asterisco * len(palabra) + "****\n",sep="")

# Lo de arriba fue una negreada. Con más de un print queda más prolijo el código:

palabra = input("Ingrese una palabra: ")
asterisco = "*"

print(asterisco * len(palabra) + "****\n*",palabra,asterisco)
print(asterisco * len(palabra) + "****\n")
