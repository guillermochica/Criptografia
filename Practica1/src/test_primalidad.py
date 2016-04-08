# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 11:03:34 2016

@author: guillermo
Práctica 1: Ejercicio 4
"""

from powermod import expmod
from random import randrange

#******************************************************************************
def millerrabin(p):
    """
    Implementación del algoritmo de mille rabin para comprobar si un número
    es primo
    
    Entrada:
        p: número candidato
        
    Salida:
        True: Si es probablemente primo
        
        False: Si no es primo
    """
    
    #Expresamos p-1 como (2**u)*s
    #Calculamos s y u
    s = p-1
    u=0
    while (s%2==0): #vemos si es primo
        s = s//2
        u=u+1
    
    
    #Escogemos un a aleatorio entre 2 y p-2 Unif[2,p-2] p-2>2
    #randrange(inicio, fin, salto)
    #inicio: se incluye en el rango
    #fin: fin del rango, no se incluye en el rango
    a = randrange(2,p-1) 
       
    #Si a**s=1 o a**s=-1
    if(expmod(a,s,p)==1 or expmod(a,s,p)==p-1): #p-1 es -1 en mod p
        return True
    else:
        #Desde i=1 hasta u-1
        for i in range(1,u, 1):
            #Si a^((2^k)*u) igual a -1 con k<u -> probablemente primo
            exp=(2**i)*s
            if (expmod(a,exp,p)==p-1): 
                return True
            #Si a^((2^k)*u) igual a 1 no precedido de -1 -> no primo
            elif (expmod(a,exp,p)==1):
                return False
        #Si no aparece el 1-> No primo
        return False
        
#*****************************************************************************
def esprimo(p,n):
    """
    Función que pasa el test de miller rabin varias veces, y dice si es primo
    o no con un porcentaje
    
    Entrada: 
        p: número que pasa test
        
        n: número de veces que se hace el test
    
    Salida: 
        True si primo, False si no primo
    """
    siprimo=0   
    for i in range (1,n,1):
        primo = millerrabin(p)
        if (primo==True):
            siprimo=siprimo+1
        else:
            #print "No es primo"
            return False
    #Calculamos porcentajes:
        
    porcentajeprimo = (float(siprimo)/n)*100
    #Además, calculamos la probabilidad de que sea primo
    prob = ((4**n-1)/float(4**n))*100
    
    print "Probablemente primo. El "+str(porcentajeprimo)+" % de veces ha dado probablemente primo"
    print "Es primo con una probabilidad mayor o igual que "+str(prob)+" %"
    
    return True
    
#*****************************************************************************
