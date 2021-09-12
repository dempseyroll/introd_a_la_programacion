#Ejercicio 17

#La empresa que administra los cajeros automáticos lo contrata para que programen la entrega de
#billetes, el usuario ingresa la cantidad de dinero que desea y usted debe indicar cuantos billetes de cada
#denominación se debe entregar. Es importante entregar siempre la menor cantidad de billetes. Ayuda:
#El operador % da el resto de la división a/b, y el operador // da la parte entera del cociente de a/b.

dinero_solicitado=int(input("Ingrese el dinero que desea retirar: "))

bill_1000=dinero_solicitado // 1000
resto_1=dinero_solicitado % 1000

if resto_1 == 0:
    print("Usted recibe\n",bill_1000,"billetes de 1000 pesos")
else:
    bill_500=resto_1 // 500
    resto_2=resto_1 % 500
    if resto_2 == 0:
            print("""Usted recibe:
            """,bill_1000,"""billetes de 1000 pesos
            """, bill_500,"""billetes de 500 pesos""")
    else:
        bill_200=resto_2 // 200
        resto_3=resto_2 % 200
        if resto_3 == 0:
            print("""Usted recibe:
            """,bill_1000,"""billetes de 1000 pesos
            """, bill_500,"""billetes de 500 pesos
            """,bill_200,"""billetes de 200 pesos""")
        else:
            bill_100=resto_3 // 100
            resto_4=resto_3 % 100
            if resto_4 == 0:
                 print("""Usted recibe:
                """,bill_1000,"""billetes de 1000 pesos
                """, bill_500,"""billetes de 500 pesos
                """,bill_200,"""billetes de 200 pesos
                """,bill_100,"""billetes de 100 pesos""")
            else:
                bill_50=resto_4 // 50
                resto_5=resto_4 % 50
                if resto_5 == 0:
                    print("""Usted recibe:
                    """,bill_1000,"""billetes de 1000 pesos
                    """, bill_500,"""billetes de 500 pesos
                    """,bill_200,"""billetes de 200 pesos
                    """,bill_100,"""billetes de 100 pesos
                    """,bill_50,"""billetes de 50 pesos""")
                else:
                    bill_20=resto_5 // 20
                    resto_6=resto_5 % 20
                    if resto_6 == 0:
                        print("""Usted recibe:
                        """,bill_1000,"""billetes de 1000 pesos
                        """, bill_500,"""billetes de 500 pesos
                        """,bill_200,"""billetes de 200 pesos
                        """,bill_100,"""billetes de 100 pesos
                        """,bill_50,"""billetes de 50 pesos
                        """,bill_20,"""billetes de 20 pesos""")
                    else:
                        bill_10=resto_6 // 10
                        resto_7=resto_6 % 10
                        if resto_7 == 0:
                            print("""Usted recibe:
                            """,bill_1000,"""billetes de 1000 pesos
                            """, bill_500,"""billetes de 500 pesos
                            """,bill_200,"""billetes de 200 pesos
                            """,bill_100,"""billetes de 100 pesos
                            """,bill_50,"""billetes de 50 pesos
                            """,bill_20,"""billetes de 20 pesos
                            """,bill_10,"""billetes de 10 pesos""")

#Fua re vivido, creo que podría haberlo hecho en menos líneas obviamente.








