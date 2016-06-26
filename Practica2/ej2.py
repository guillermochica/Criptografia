# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 09:39:15 2016

@author: guillermo
"""
from ej1 import golomb
#******************************************************************************
def productoescalar(c,r):
    """"
    Producto escalar modulo 2 de dos listas de 0 y 1
    
    Entrada:
        c: lista de 0 y 1 ej [1,1,1]
        r: lista de 0 y 1 ej [1,1,1]
    
    Salida:
        El producto escalar en modulo 2
    """
    s = 0
    for i in range(len(c)):
        s = s + c[i]*r[i]
    
    return s%2
#******************************************************************************
def lfsr(c,s,l):
    """
    Implementación de lfsr
    
    Entrada:
        c: lista coeficientes polinomio conexión en orden [cL,...,c1]
    
        s: lista de semilla en orden [s0,...sL-1] de la misma longitud que c
    
        l: longitud secuencia salida
    
    Salida:
        s: resultado de aplicar el registro de desplazamiento 
    """
    
    #Si la longitud de salida es menor o igual que el tamaño de la semilla
    if (l <= len(s)):
        return s[:l]
    
    #copiamos s en r que será el registro
    r=[]
    for i in s:
        r.append(i)
    
    for i in range(l):
        prod = productoescalar(c,r)
        #añado el nuevo valor
        s.append(prod)
        #muevo el registro a la izquierda
        r.pop(0) #quitamos el primer elemento
        r.append(prod) #añadimos el nuevo valor
    
    return s
#******************************************************************************
"""Pruebas:
c = [1,0,1,0]
s = [1,0,0,1]
print lfsr(c,s,20)],20)

#Cumple golomb, c es polinomio primitivo
g = lfsr([1,0,0,0,0,1,0,0,0],[1,0,1,1,0,1,0,0,0],600)
print golomb(g[0:(2**9)-1]) #el periodo es 2**L - 1 (L=9)
#Polinomios reducibles: (D⁴+D²+1) periodo menor que el periodo máximo 2**L-1 y depende de la semilla
print lfsr([1,0,1,0],[1,1,1,0],20) #periodo 6
print lfsr([1,0,1,0],[0,1,1,0],20) #periodo 3
#Polinomios irreducibles: (D⁴+D³+D²+D) Periodo no depende de semilla, pero es divisor del periodo máximo 2**L-1
print lfsr([1,1,1,1],[1,1,1,0],20) #periodo 5
print lfsr([1,1,1,1],[0,1,1,0],20)"""
print lfsr([1,0,0,1],[1,0,1,1],5)