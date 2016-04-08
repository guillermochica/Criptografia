# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 09:35:13 2016

@author: guillermo
Práctica 1: Ejercicio 5
"""
from powermod import expmod

#*****************************************************************************
def petitpasgrandpas(a,b,p):
    """
    Implementación del algoritmo paso enano-paso gigante
    Calcula x tal que a^x = b mod p
    
    Entrada: 
        a, b: enteros
        
        p: primo
    
    Salida: 
        x tal que a^x= b mod p si hay solución 
        
        False si no hay solución
    
    """
    #Calculamos s: primer primo que elevado a 2 da > que p-1
    s=1
    while(s**2<p-1):
        s=s+1
    
    #Sacamos la lista grande y la pequeña
    L = [expmod(a,s*i,p) for i in range(1,s+1)]
    l = [(b*expmod(a,i,p))%p for i in range(s)]
    
    #Buscamos la insterseccion entre L y l
    n = list(set(L) & set(l))
    
    #Si no hay intersección, no hay solución
    if not n:
        print "No hay solución"
        return False
    
    #x = i*b - j
    #i indice de n en L +1
    #j indice de n en l
    i = L.index(n[0]) + 1
    j = l.index(n[0])
    
    x = i*s -j
    
    return x
#*****************************************************************************