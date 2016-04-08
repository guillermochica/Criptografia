# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 15:09:45 2016

@author: guillermo
Práctica 1: Ejercicio 6
"""
from powermod import expmod
from euclides import inverso

#*****************************************************************************
def jacobi(a,p):
    """
    Extensión del simbolo de legendre para p no primo

    Entrada:
        a: entero
        p: impar
        
    Salida:
        1 si a es residuo cuadrático mod p
        
        0 si p divide a a
        
        -1 en caso contrario
        
    """   
    if(p!=1):
       a = a%p
    else: #si (a/1)
        return 1
    
    #Comprobamos los casos base
    if (a==0):
        return 0
    if (a==1):
        return 1
    if (a==2):
        if ( p%8 == 1 or p%8 == 7):
            return 1
        else:
            return -1
    if (a == p-1):
        if (p%4 == 1):
            return 1
        if (p%4 == 3):
            return -1
    
    #saco u y s
    s = a
    u=0
    while (s%2==0): #vemos si es par
        s = s//2
        u=u+1
        
    #Reciprocidad cuadrático
    signo1=1
    signo2=1
    if (u%2==0):
        signo1 = 1
    else:
        if (p%8 == 1 or p%8 == 7):
            signo1 = 1
        else:
            signo1 = -1
    
    if (p%4==1 or s%4==1):
        signo2 = 1
    elif (p%4==3 and s%4==3):
        signo2 = -1
    #Damos la vuelta        
    a = p
    p = s
    
    return signo1*signo2*jacobi(a,p)
#*****************************************************************************
    
def raizmodulo(a,p):
    """
    Dado a y p primo con Jacobi(a,p)=1, devuelve r tal que r²=a mod p
    
    Entrada:
        a: entero
        
        p: primo
    
    Salida:
        r: raiz de a mod p si a es un residuo cuadrático modulo p
        
        False: si a no es un residuo cuadrático modulo p
    """
    
    #Comprobamos que a es un residuo cuadrático mod p
    if(jacobi(a,p)!=1):
        return False
    
    #Expresamos p-1 como (2**u)*s
    #Calculamos s y u
    s = p-1
    u=0
    while (s%2==0):
        s = s//2
        u=u+1
    
    if (u==1):
        r = a**((p+1)/4)
        return r
    if (u>=2):
        #Busco n tal que jacobi(n,p)=-1
        n=1
        while (jacobi(n,p)!=-1):
            n = n+1
        #b es n**s mod p
        b = expmod(n,s,p)
        r = expmod(a, (s+1)/2, p)
        inversoa = inverso(a,p)
        
        for j in range(u-1):
            
            base = expmod(r,2,p) * inversoa
            exponente = 2**(u-2-j)
            if (expmod(base,exponente,p)) == p-1:
                r = (r*b)%p
            
            b = expmod(b,2,p)
        
        return r
#*****************************************************************************
def teoremachino(a,b,p,q):
    """
    Implementación del teorema chino de los restos.
    
    Dado a, b, p, q, devuelve x tal que x=amodp y x=bmodq
    
    Entrada:
        a y b: enteros
        
        p y que: primos
    
    Salida:
        x: solución de x=amodp y x=bmodp. x único modulo pq
    """
    x = inverso(p,q)*(b-a)*p+a
    
    return x%(p*q)
#*****************************************************************************
def raizmodn(a,p,q):
    """
    Algoritmo que calcula las raices cuadradas de a mod n a partir de las
    raices de a mod p y q, con n=q
    
    Entrada: 
        a entero residuo cuadrático modulo p y q
        
        p y q: primos
    
    Salida: 
        raices de a mod n con n=p*q
        
        False si a no es residuo cuadrático modulo p y q
    """
    if (jacobi(a,p)!=1 and jacobi(a,q)!=1):
        return False
    
    n = p*q
    
    r1 = raizmodulo(a,p)
    r2 = raizmodulo(a,q)
    
    s1 = teoremachino(r1,r2,p,q) #caso r1 r2
    s2 = n - s1 #caso -r1 -r2
    s3 = teoremachino(r1,q-r2,p,q) #caso r1 -r2
    s4 = n - s3 #caso -r1 r2
    
    return [s1,s2,s3,s4]
#*****************************************************************************