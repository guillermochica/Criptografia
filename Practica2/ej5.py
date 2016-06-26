# -*- coding: utf-8 -*-
"""
Created on Wed May 11 10:31:43 2016

@author: guillermo
"""
from ej2 import lfsr

def berlekamp(s):
    """
    Implementación del algoritmo berlekamp massey
    
    Entrada:
        s: secuencia binaria de tamaño n, en forma de lista, ordenada [s0,...sn-1]
    
    Salida:
        L: complejidad lineal de s
        C: Polinomio de conexión que genera s con un lfsr
    """
    L=0
    C=[1]
    m=-1
    B=[1]
    N=0
    
    #d=1 cuando me encuentro el primer elemento de s que sea 1
    
    while (s[N]==0):
        N = N + 1
    
    #Primer elemento distinto de 0 -> d=1
    d=1
    T=list(C)
    #Cambiamos C
    #bd = B(D)*D^N-m
    Nm = N-m
    bd = list(B)
    for i in range(Nm): 
        bd.insert(0,0)
    #C + bd
    if (len(C)<=len(bd)):
        suma = list(bd)
        for i in range(len(C)):
            suma[i] = (C[i]+bd[i])%2
        C = list(suma)
    else:
        suma = list(C)
        for i in range(len(bd)):
            suma[i] = (C[i]+bd[i])%2
        C = list(suma)
    
    if (L<=N/2):
        L = N +1-L
        m = N
        B = list(T)
    
    N = N+1

    while (N<len(s)):
        
        #Calculamos discrepancia
        #aux = sumatoria de C(i)*s(N-i)
        aux = 0
        for i in range(1,L+1): #sumatoria de i=1 hasta L
            aux = aux + C[i]*s[N-i]
        d = (s[N] + aux)%2
        
        if (d==1):
            T=list(C)
            #Cambiamos C
            #bd = B(D)*D^N-m
            Nm = N-m
            bd = list(B)
            for i in range(Nm): 
                bd.insert(0,0)
            #C + bd
            if (len(C)<=len(bd)):
                suma = list(bd)
                for i in range(len(C)):
                    suma[i] = (C[i]+bd[i])%2
                C = list(suma)
            else:
                suma = list(C)
                for i in range(len(bd)):
                    suma[i] = (C[i]+bd[i])%2
                C = list(suma)
            
            if (L<=N/2):
                L = N +1-L
                m = N
                B = list(T)
                #C = list(C[0:L])
            
        N = N+1
    

    return [L,C]
                
#******************************************************************************
s2 = [1,0,0,1,1,0,1,1,1,0]
s = [1,0,1,1,1,1,0,0,0,1,0,0,1,1]
x = berlekamp(s2)
print 'L = ',x[0]
print 'lfsr = ',x[1]

