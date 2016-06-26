# -*- coding: utf-8 -*-
"""
Created on Wed May 25 11:01:46 2016

@author: guillermo
"""
from euclides import inverso

#La clave publica es la lista supercreciente cambiada, el emisor la conoce
#La clave privada es la lsita supercreciente sin modificar, solo la tiene el receptor
#*****************************************************************************
def cifrado(m,kpub):
    """
    Cifrado de knapstack
    
    Entrada:
        m: mensaje a cifrar formado por lista binaria de 1 y 0
        
        kpub: secuencia obtenida a partir de una supercreciente[a1*...ak*] haciendo u*kpriv[i]modn
        
    Salida:
        sum: mensaje cifrado
    """
    sum = 0
    for i in range(len(m)):
        sum = sum + m[i]*kpub[i]
    
    return sum
    
#*****************************************************************************
def greedy(n,s):
    """
    Algoritmo avaricioso
    
    Entrada:
        n: número del cual quiere conocerse sus sumandos en la lista s
        
        s: secuencia supercreciente
    
    Salida:
        sum: lista que contiene los elementos de s que al sumar dan n
    """
    
    suma = []
    #encontramos el primer elemento de la mochila que sea anterior a n
    for i in range(len(s)):
        if (s[i] >= n):
            suma.append(s[i-1])
    if (len(suma)==0):
        suma.append(s[len(s)-1])
    
    j=0
    fin = False
    aux= n- suma[0]
    while not fin:
        for i in range(len(s)):
            #si s[i] es mayor que aux, nos quedamos con s[i-1]
            #siempre y cuando s[i-1] no esté ya en suma y no sea 1
            if (s[i] >= aux and s[i-1] not in suma and aux!=1 and s[i-1]<aux):
                suma.append(s[i-1])
                j = j+1
                aux = aux - suma[j]
                if (aux in s):
                    suma.append(aux)
                if (aux ==1): #si aux ya es 1, paro
                    fin = True
        
        #Comprobamos si la suma de los elementos de la lsita sum da n
        if (sum(suma)==n):
            fin = True
        
    return suma
                
#*****************************************************************************
def descifrado(c, kpriv):
    """
    Descifrado de knapstack
    
    Entrada:
        c: mensaje cifrado
        
        kpriv: formada por una secuencia super creciente [a1...ak], n y u tal que gcd(n,u)=1
        
    Salida:
        d: lista binaria del mensaje descifrado
    """    
    a = kpriv[0] #la secuencia supercreciente
    n = kpriv[1]
    u = kpriv[2]
    
    v = inverso(u,n)
    
    b = (v*c) % n #b  = Sum m[i]*a[i]
    print b
    #descomponemos b como suma de elementos de la mochila
    lista =  greedy(b,a)
    print lista
    #Expresamos los elementos de la mochila como binario
    d = []
    for i in a:
        if i in lista: #si el elemento de lista está en mochila, ponemos 1
            d.append(1)
        else:
            d.append(0)
    
    return d
#*****************************************************************************    
    
#s= [1,2,4,8,16,32]
#print greedy(27,s)

m = [0,1,1,0,0,1,0,1]
a = [1,3,7,15,31,63,127,255]
n = 557
u = 323
kpriv = [a,n,u]
kpub=[] #kpub = a*u mod n
for i in a:
    kpub.append((i*u)%n)
    
c = cifrado(m, kpub)
d = descifrado(c, kpriv)
print m
print d