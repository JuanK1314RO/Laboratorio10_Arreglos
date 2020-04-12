# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 15:13:00 2020

@author: Juan Camilo Ramirez
"""

##funcion para calcular la potencia##
def a_power_b(a, b):
    potencia = 1
    while (b>0):
        potencia = potencia*a
        b = b - 1
    return potencia

##COntadores##
a=1##Este es para empezar el ciclo while##
cont_impares=0
cont_pares=0
cont=0
while a!=0:
    a = int(input("Ingrese base: "))
    b = abs(int(input("Ingrese exponente: ")))
    cont = cont + 1
    if a_power_b(a, b)%2 != 0:
       cont_impares += 1
    else:
        cont_pares += 1
    print("El resultado es: "+str(a_power_b(a, b)))
print("\nLa cantidad de impares es:", cont_impares)
print("\nLa cantidad de pares es:", cont_pares)
print("\nLa cantidad de potencias es:",cont)