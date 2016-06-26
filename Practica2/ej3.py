# -*- coding: utf-8 -*-
"""
Created on Wed May  4 09:49:50 2016

@author: guillermo
"""
from powermod import expmod

#******************************************************************************
def nlfsr(f, s, k):
    """
    Función que aplica el registro no lineal de desplazamiento asociado a f
    
    Entrada:
        f: función polinómica como lista de exponentes de monomios [[],[],[]]
        
        s: semilla en forma de lista [1,1,1...] de la misma longitud que f
        
        k: longitud del registro generado
        
    Salida:
        x: secuencia de longitud k obtenida al aplicar a s el registro no lineal
        de desplazamiento con retroalimentación asociado a f
    """
    
    #Si la longitu de salida es menor o igual que el tamaño de la semilla
    if(k<=len(s)):
        return s[:k]
    
    x = list(s)
    total=0
    prod=1
    
    for i in range(k-len(s)): #repetimos k-len(s) veces, para tener una secuencia de tamaño k
        for l in range(len(f)):#repetimos tantas veces como listas haya en f
            for j in range(len(f[0])):#calculamos la potencia en cada indice de s y f
                prod = prod* expmod(s[j],f[l][j],2)
            
            total = (total + prod)%2
            prod = 1
        #Ya hemos hecho la suma para todas las lista dada una semilla
        #Cambiamos semilla y repetimos
        x.append(total)
        s.pop(0)
        s.append(total)
        total = 0
    
    return x
#******************************************************************************
f = [[1,1,1,0],[0,0,0,0],[0,0,1,0],[0,0,0,1]]
s = [1,0,1,1]
print nlfsr(f,s,100)