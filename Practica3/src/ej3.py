# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 12:00:28 2016

@author: guillermo
"""

from euclides import mcd
#******************************************************************************
def rabin():
    """
    Función que calcula los factores primos de un entero y los devuelve
    """
    
    #mcd(x-y,n) es un divisor no trivial de n

    p = mcd(48478872564493742276963,37659670402359614687722+12)[0]
    q = mcd(48478872564493742276963,37659670402359614687722-12)[0]
    
    print p*q #Comprobación de que son divisores de n 
    
    return p,q    
#******************************************************************************

p,q = rabin()
print p,q
print p*q