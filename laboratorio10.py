# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 15:13:00 2020

@author: Juan Camilo Ramirez
"""

##Asicacion de variables##
a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de la potencia: "))

def a_power_b(a,b):
   potencia = 1
   while (b>0):
       potencia = potencia*a
       b = b-1
       
   return potencia

print("\nEl resulatado es:", a_power_b(a,b))