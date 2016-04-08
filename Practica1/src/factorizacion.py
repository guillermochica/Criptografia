# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 11:59:24 2016

@author: guillermo
Práctica 1: Ejercicio 7
"""
from euclides import mcd
from test_primalidad import esprimo
from random import randint
#*****************************************************************************
def isqrt(n):

    """
    Implementación del método de newton para el cálculo de raíces cuadradas
    
    Entrada: 
        n: entero
    
    Salida:
        x: raíz cuadrada de n
    """    
    if(n==0):
    	return 0
    if(n==1):
    	return 1

    x = n

    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x
    
#*****************************************************************************
def factoriza(n):
    """
    Implementación del método de Fermat para factorización de enteros
    
    Entrada:
        n: entero positivo
        
    Salida:
        a y b tal que n=a*b no triviales (ni 1 ni -1)
        False si no consigue factorizar porque no existe un a y b equidistantes (ejemplo 
    """
    #Comprobamos que n no es primo
    if(esprimo(n,10)):
        return False    
    #x raiz de n redondeando por arriba
    x = isqrt(n) + 1
    
    while(x<n):
        k = x**2 - n
    	#Si k es un cuadrado
        if (isqrt(k)**2 == k): #n = (x^2-k) = (x²-l²) = (x-l)*(x+l)
            l = isqrt(k)
            a = x-l
            b = x+l
            return [a,b]
        else:
            x = x+1
    
    return False
#*****************************************************************************
def f(x,c,n):
    """
    Función pseudoaleatoria usada en el cálculo de la rho de pollard
    
    Entrada:
        x,c,n, enteros
        
    Salida:
        Valor aleatorio
    """
	
    return (x**2 + c)%n
#*****************************************************************************
def pollard(n):
    """
    Implementación de ro de pollard para factorización de enteros
    
    Entrada:
        n: entero NO PRIMO, el numero que se quiere factorizar
    
    Salida:
        d factor no trivial de n
        
        False si n es primo
    """
    #Comprobamos que n no es primo
    if(esprimo(n,10)):
        return False
    
    while(True):
        x = 2
        y = 2
        d = 1
        c = randint(1,n-1) #c != de 0 y -2
        
        while (d==1):
            x = f(x,c,n)
            y = f(f(y,c,n),c,n)
            d = mcd(abs(x-y),n)[0]
        
        if(d !=n): #Si d igual a n, seguimos intentando con otro c
            return d
   
    
    return d
#*****************************************************************************
