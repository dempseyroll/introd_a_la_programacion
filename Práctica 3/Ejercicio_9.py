# Ejercicio 9

# a) Hacer un programa que permita al usuario elegir un número positivo n y luego
# muestre en pantalla todos los divisores de n.

#n = int(input("Ingrese un número n: "))

#if n < 0:
#    print("ERROR - No es un número positivo")

#else:
#    for test_divisor in range(1,n+1):
#        candidato= n % test_divisor
#        if candidato == 0:
#            print("Es divisor: ", test_divisor)
        
## a) con "while":

## n = int(input("Ingrese un número n: "))
## test_divisor= 1

## if n < 0:
##     print("ERROR - No es un número positivo")

## while test_divisor <= n:
##     candidato= n % test_divisor
##     if candidato == 0:
##         print("Es divisor: ", test_divisor)
##     test_divisor+=1


### b) Hacer un programa que permita al usuario elegir un número positivo n y luego
### muestre en pantalla todos los divisores pares de n.

### n = int(input("Ingrese un número n: "))

### if n < 0:
###     print("ERROR - No es un número positivo")

### else:
###     for test_divisor in range(1,n+1):
###         candidato= n % test_divisor
###         if test_divisor % 2 == 0 and candidato % test_divisor == 0:
###             print("Es divisor par: ", test_divisor)

### b) con "While":

### n = int(input("Ingrese un número n: "))
### test_divisor = 1

### if n < 0:
###     print("ERROR - No es un número positivo")

### else:
###     while test_divisor<=n:
###         candidato= n % test_divisor
###         if test_divisor % 2 == 0 and candidato % test_divisor == 0:
###             print("Es divisor par: ", test_divisor)
###         test_divisor+=1

#### c) Hacer un programa que permita al usuario elegir un número positivo n y luego
#### muestre en pantalla la cantidad de divisores de n.

#### n = int(input("Ingrese un número n: "))
#### contador_divisores = 0
#### if n < 0:
####     print("ERROR - No es un número positivo")

#### else:
####     for test_divisor in range(1,n+1):
####         candidato= n % test_divisor
####         if candidato == 0:
####             contador_divisores+=1

#### print("Cantidad total de divisores: ", contador_divisores)
        
#### c) con "while":

#### n = int(input("Ingrese un número n: "))
#### test_divisor= 1
#### contador_divisores = 0

#### if n < 0:
####     print("ERROR - No es un número positivo")

#### while test_divisor <= n:
####     candidato= n % test_divisor
####     if candidato == 0:
####         contador_divisores+=1
####     test_divisor+=1

#### print("Cantidad total de divisores: ", contador_divisores)

##### d) Hacer un programa que permita al usuario elegir un número positivo n y luego
##### muestre en pantalla la suma de los divisores de n.

##### n = int(input("Ingrese un número n: "))
##### total_divisores=0

##### if n < 0:
#####     print("ERROR - No es un número positivo")

##### else:
#####     for test_divisor in range(1,n+1):
#####         candidato= n % test_divisor
#####         if candidato == 0:
#####             total_divisores+=test_divisor
            
##### print("La suma de los divisores de",n,"es: ",total_divisores)
        
##### d) con "while":

##### n = int(input("Ingrese un número n: "))
##### test_divisor= 1
##### total_divisores = 0

##### if n < 0:
#####     print("ERROR - No es un número positivo")

##### while test_divisor <= n:
#####     candidato= n % test_divisor
#####     if candidato == 0:
#####         total_divisores+=test_divisor
#####     test_divisor+=1

##### print("La suma de los divisores de",n,"es",total_divisores)

###### e) Hacer un programa que permita al usuario elegir dos números positivos c y n y luego
###### muestre en pantalla los primeros c divisores de n.

###### n = int(input("Ingrese un número n: "))
###### c = int(input("Ingrese un número c: "))
###### divisores=""
###### coincidencias_c = 0

###### if n < 0 or c < 0:
######     print("ERROR - No es un número positivo")

###### else:
######     for test_divisor in range(1,n+1):
######         candidato= n % test_divisor
######         if candidato == 0:
######             divisores= divisores + str(test_divisor) + " "
######             coincidencias_c+=1
######             if coincidencias_c == c:
######                 print("Los primeros",c,"divisores de",n,"son:",divisores)

###### e) con "while":

###### n = int(input("Ingrese un número n: "))
###### c = int(input("Ingrese un número c: "))
###### test_divisor=1
###### divisores=""
###### coincidencias_c = 0

###### if n < 0 or c < 0:
######     print("ERROR - No es un número positivo")

###### else:
######     while test_divisor <= n:
######         candidato= n % test_divisor
######         if candidato == 0:
######             divisores= divisores + str(test_divisor) + " "
######             coincidencias_c+=1
######             if coincidencias_c == c:
######                 print("Los primeros",c,"divisores de",n,"son:",divisores)
######         test_divisor+=1


####### f) Hacer un programa que permita al usuario elegir dos números positivos c y n y luego
####### muestre en pantalla los últimos c divisores de n.

####### n = int(input("Ingrese un número n: "))
####### c = int(input("Ingrese un número c: "))
####### divisores=""
####### coincidencias_c = 0

####### if n < 0 or c < 0:
#######     print("ERROR - No es un número positivo")

####### else:
#######     for test_divisor in range(n,1,-1):
#######         candidato= n % test_divisor
#######         if candidato == 0:
#######             divisores= divisores + str(test_divisor) + " "
#######             coincidencias_c+=1
#######             if coincidencias_c == c:
#######                 print("Los últimos",c,"divisores de",n,"son:",divisores)

####### f) con "while":

n = int(input("Ingrese un número n: "))
c = int(input("Ingrese un número c: "))
test_divisor=n
divisores=""
coincidencias_c = 0

if n < 0 or c < 0:
    print("ERROR - No es un número positivo")

else:
    while test_divisor >= 1:
        candidato= n % test_divisor
        if candidato == 0:
            divisores= divisores + str(test_divisor) + " "
            coincidencias_c+=1
            if coincidencias_c == c:
                print("Los últimos",c,"divisores de",n,"son:",divisores)
        test_divisor-=1
