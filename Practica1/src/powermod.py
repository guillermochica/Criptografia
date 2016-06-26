# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 10:16:53 2016

@author: guillermo
Práctica 1: Ejercicio 3
"""
#********************************************************
def expmod(b,e,m):
    """
    Calcula la potencia modular de un número
    
    Entrada:
        b: base entera
        
        e: exponente entero
       
        m: modulo entero
    
    Salida:
        prod: resultado de (b^e) mod n
    """
    #b = base
    #e = exponente
    #m = modulo
    s=e
    prod=1 #En prod voy almacenando el resultado de las potencias
    a=b
    
    while(s>0):
        #Caso 1: primer bit es 1
        if(s%2==1):
            #Cambio prod
            prod = (prod * a) % m
            #Cambio s
            s = (s-1)/2
        #Caso 2: primer bit es 0
        elif (s%2==0):
            #No cambio prod
            #Cambio s
            s = s / 2
        #Cambio a
        a = (a*a) % m
        if(a==1):
            return prod
    
    #Devuelvo el resultado:
    return prod
#********************************************************

