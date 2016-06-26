# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 20:20:05 2016

@author: guillermo
"""

from euclides import mcd
from euclides import inverso
from powermod import expmod
from test_primalidad import esprimo

#*****************************************************************************
def inversorsa(p,q,y):
    """
    Función que calcula el inverso de la función RSA f : Zn -> Zn, x -> x^e .
    
    Entrada:
        p: numero de identidad
        q: fecha de nacimiento
        y: el valor al que calcular el inverso
    Salida:
        x: el inverso de la función RSA para el valor y
    """
    #pprimo el menor primo entero mayor que mi numero de identidad
    pprimo = False
    #qprimo el primer primo mayor que mi fecha de nacimiento
    qprimo = False
    
    while not pprimo:
        if (esprimo(p,10)):
            pprimo = True
        else:
            p = p+1
    
    while not qprimo:
        if (esprimo(q,10)):
            qprimo = True
        else:
            q = q+1
    
    n = p*q
    
    e = 2
    phi = (p-1)*(q-1)
    while (mcd(e,phi)[0] !=1 ):
        e = e+1
    
    #inverso de x^e=y es sacar x dado e y y
    
    d = inverso(e, phi)
    x = expmod(y,d,n)
    return x
    #print expmod(x,e,n)
    
#*****************************************************************************
p=77378395
q=19930530
y = 1234567890 #elemento al que calcular el inverso
print inversorsa(p,q,y)