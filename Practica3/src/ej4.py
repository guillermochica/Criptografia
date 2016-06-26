# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 12:21:24 2016

@author: guillermo
"""

#*****************************************************************************
def h(x,b):
    """
    Función de compresión 
    
    """
    n = 48478872564493742276963
    #a0 y a1 dos cuadrados arbitrario mod n
    a0 = (6347823468234**2) % n
    a1 = (5143151387122**2) % n
    
    return ((x**2)  * (a0**b) * (a1 **(1-b))) % n
#*****************************************************************************

def resumen(x,m):
    """
    Función resumen que usa una estructura de merkle damgard usando h como
    función de compresión
    
    Entrada:
        x: vector inicial en forma de entero
        m: mensaje al que aplicar el resumen en forma de lista de bits
    
    Salida:
        salida: el resumen aplicado a m en forma de entero
    """
    #x vector inicial, m mensaje al que aplicar el hash
    
    salida = 0
    for i in range(0,len(m)):
        #Construccion merkle damgard
        #La salida de la h se combina en una nueva h con
        #el nuevo bloque de mensaje que es m[i]
        salida = h(x,m[i]) #m[i] es b 
        x = salida #lo que sustituye al vector inicial en los sucesivos pasos es la salida de h
    
    return salida
#*****************************************************************************


print resumen(7687,[1,0,1,1])