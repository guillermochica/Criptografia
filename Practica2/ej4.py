# -*- coding: utf-8 -*-
"""
Created on Wed May  4 11:25:42 2016

@author: guillermo
"""
from ej2 import lfsr
from ej5 import berlekamp
#*****************************************************************************
def geffe(lfsr1, lfsr2, lfsr3):
    """
    Implementación del generador de geffe
    
    Entrada:
        LFSR1,LFSR2,LFSR3: 3 lfsr
        
    Salida:
        s: igual a lfsr1lfsr2+lfsr2lfsr3+lfsr3
    
    La complejidad lineal de los lfsr es L1,L2 y L3
    Sus periodos p1 = (2^L1-1) p2 = (2^L2-1) p3 = (2^L3-1)
    Si L1,L2 y L3 son primos entre si, el periodo de s es p1*p2*p3

    """
    s=[]
    
    for i in range(len(lfsr1)):
        s.append((lfsr1[i]*lfsr2[i]+lfsr2[i]*lfsr3[i]+lfsr3[i])%2)
    
    return s
#*****************************************************************************
def cifrado(m,k):
    """
    Implementación de un cifrado de flujo
    
    Entrada:
        m: mensaje a cifrar
        k: clave de la misma longitud que m
    
    Salida:
        c = m+k  (suma componente a componente modulo 2)
    """
    c=[]
    for i in range(len(m)):
        c.append((m[i]+k[i])%2)
    
    return c

#*****************************************************************************
def descifrado(c,k):
    """
    Descifrado de un cifrado de flujo
    
    Entrada:
        c: mensaje cifrado
        k: clave
    
    Salida:
        m = c+k (suma componente a componente modulo 2), el mensaje en claro
    """
    d =[]
    
    for i in range(len(c)):
        d.append((c[i]+k[i])%2)
        
    return d

#*****************************************************************************
#Ejemplo donde el periodo de salida sea p1p2p3
#Necesitamos 3 LFSR cuya L sea primos entre sí, por ejemplo:
#L1=3, L2=5,L3=7

lfsr1=lfsr([1,0,1],[1,0,0],4997)
lfsr2=lfsr([1,1,0,1,1],[1,0,0,1,1],4995)
lfsr3=lfsr([1,1],[1,0],4998)
k=geffe(lfsr1,lfsr2,lfsr3)

p1 = 2**3-1
p2 = 2**5-1
p3 = 2**2-1
#print p1*p2*p3

k.reverse()
Lk = berlekamp(k)[0]
pk = 2**Lk -1
print 'p1*p2*p3 = ', p1*p2*p3
print 'pk = ', pk

m=[1,0,1,1,0,1,1,0,1,0,0,1,0,0,1,1,0,1,0,1]
print "mensaje: ", m
c = cifrado(m,k)
print "cifrado: ", c
d= descifrado(c,k)
print "descifrado: ",d

