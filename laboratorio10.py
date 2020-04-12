# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 15:13:00 2020

@author: Juan Camilo Ramirez
"""

def a_power_b(a,b):
   potencia = 1
   while (b>0):
       potencia = potencia*a
       b = b-1
   print("\nEl resulatado es:", potencia )
   return potencia

a=1
while a<0 or a>0:
    a = int(input('Ingrese base:  '))
    b = abs(int(input('Ingrese exponente:  ')))
    a_power_b(a,b)
    
a_power_b.count()
print(a_power_b.count())