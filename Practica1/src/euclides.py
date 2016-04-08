# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 11:06:44 2016

@author: guillermo
Práctica 1: Ejercicios 1 y 2
"""
#******************************************************
def mcd(a,b):
    """
    Implementación del algoritmo de euclides para el cálculo del MCD y los
    coeficientes de Bezout
    
    Entrada: 
        a, b: enteros 
    
    Salida:
        El mcd y los coeficientes u y b
    """


    #Inicilizamos u y v para a y b
    u_a=1
    v_a=0
    u_b=0
    v_b=1

    while(b!=0):
        #Hallamos cociente
        c = a / b
        #Valores futuros de u y v
        aux_u = u_a - c*u_b
        aux_v = v_a - c*v_b
        #Valor futuro d b
        aux_b = a - c*b
        #Hacemos los cambios
        u_a=u_b
        v_a=v_b
        u_b=aux_u
        v_b=aux_v
        a=b
        b=aux_b
        
    #a es el mcd, u el inverso si a es 1
    return [a,u_a, v_a]
#************************************************************
    
def inverso(a,n):
    """
    Algortimo para calcular el inverso modular de un número
    
    Entrada: 
        a y n enteros
    
    Salida: 
        El inverso modulo n de a: a^-1 mod n
    """
    d_u=mcd(a,n)
    if (d_u[0]!=1):
        print "No existe el inverso modulo "+str(n)+ " para "+str(a)
    else:
        #1=u*a+v*n -> u es el inverso
        return d_u[1]%n
        
#***********************************************************