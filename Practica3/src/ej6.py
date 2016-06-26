# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 13:48:24 2016

@author: guillermo
"""
from random import randint
from euclides import mcd
from powermod import expmod

#*****************************************************************************
def ej6(n,d,e):
    """
    Algoritmo para encontrar los factores primos de n, dados d y e
    
    Entrada:
        n: entero a factorizar
        d: llave pública de la función Td
        e: llave privada de la función inversa de Td, Te
    
    Salida:
        False: si no es capaz de encontrar los factores
        p y q: factores primos de n
    """
    #una inversa de Zn -> Zn, x -> x^5 es x -> x^10000000074000000101
    #Te inversa de Td mod n, si lo conocemos, podemos factorizar n

    #de -1 = 2^a * b
    #de-1 = de1
    de1 = d*e - 1
    
    #Expresamos d*e-1 como (2**a)*b con b impar
    #Calculamos a y b
    b = de1
    a=0
    while (b%2==0):
        b = b//2
        a=a+1
    
    
    while True: #repetimos con distintos x hasta encontrar factores no triviales
        
        #x aleatorio entre 1 y n
        x = randint(1,n-1)
        gcd = mcd(x,n)[0]
        
        if (gcd!=1): #hemos encontrado un factor->stop
            return gcd
        
        if (gcd==1):
            #y = x^b mod n
            y = expmod(x,b,n)
    
        for i in range(a): #hay que repetir a veces
            z = y
            y = expmod(y,2,n) # y = y^2 mod n
            
            if (y == n-1):
                #Fail
                return False
            if (y==1):
                #exito
                p = mcd(n,z+1)[0]
                q = mcd(n,z-1)[0]
                if(p!=n and p!=1):
                    #Acabamos solo si no son factores triviales
                    return p,q
    
    return False
#*****************************************************************************

n = 50000000385000000551
d = 5
e = 10000000074000000101
print ej6(589,7,13) #ejemplo libro
print ej6 (n,d,e)