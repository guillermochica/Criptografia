# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 09:46:48 2016

@author: guillermo
Practica 2: Ejercicio 1
"""
#*****************************************************************************
def primerpostulado(s):
    '''
    Algoritmo que aplica el primer postulado de Golomb
    
    Entrada:
        s: secuencia binaria a comprobar en forma de lista
    
    Salida:
        True si en s hay |numero de ceros - numero de unos| <=1
        
        False en caso contrario
    '''

    ceros = s.count(0)
    unos = s.count(1)
    
    if (abs(ceros - unos)<=1):
        return True
    else:
        return False

#*****************************************************************************
def segundopostulado(s):
    '''
    Algoritmo que aplica el segundo postulado de Golomb
    
    Entrada:
        s: secuencia binaria en forma de lista
    
    Salida:
        True si el número de rachas de 1 es igual al de 0, siempre que sea posible
        
        False: En caso contrario
    '''
    ##Hacemos tabla con numero de rachas en orden creciente (diccionario o lista)
    #cada elemento i del diccionario debe ser el doble que el i+1
    #dos ultimas posiciones: comprobar solo que es mayor o igual
    rachas={}
    for i in range(1,len(s)+1): #como mucho habra rachas de la longitud de s
        rachas[i]=0
    repeticiones=1
    #recorro la lista incrementando un contador que pongo a 0 cuando haya un cambio
    #si el primero y el ultimo son iguales, empiezo en la segunda posición
    #si no, empiezo en la primera
    if(s[0]!=s[len(s)-1]):#si el primero y el ultimo son distintos
        for i in range(len(s)):
            if(i!=len(s)-1): #si no estoy en la última posición
                if(s[i]==s[i+1]):
                    repeticiones=repeticiones+1
                if(s[i]!=s[i+1]):#cambio
                    rachas[repeticiones]=rachas[repeticiones]+1
                    repeticiones=1

            if(i==len(s)-1): #si estoy en la última posición: se que ultimo y primero son disintos
                
                rachas[repeticiones]=rachas[repeticiones]+1
    else:
        #si el primero y el ultimo son iguales
        for i in range(1,len(s)): #empiezo en la segunda posición
            if(i!=len(s)-1): #si no estoy en la última posición
                if(s[i]==s[i+1]):
                    repeticiones=repeticiones+1
                if(s[i]!=s[i+1]):#cambio
                    rachas[repeticiones]=rachas[repeticiones]+1
                    repeticiones=1
               # print repeticiones
            if(i==len(s)-1):#estoy en la última posición-primero y ultimo iguales
                repeticiones=repeticiones+1
                rachas[repeticiones]=rachas[repeticiones]+1
    #print rachas
    #Quito las últimas rachas que valen 0
    j=len(s)
    while(rachas[j]==0):
        rachas.pop(j)
        j=j-1
    #print rachas
    
    for i in range(1,len(s)):
        if (i<len(rachas)-1):

            if (rachas[i]!=rachas[i+1]*2):
                return False
        else: #estoy en la penúltima posición

            if (rachas[i]<rachas[i+1]):
                return False
            else:
                return True
    return True
                
            

#*****************************************************************************
def hamming(s,d):
    '''
    Algoritmo que calcula la distancia hamming de dos listas binarias
    
    Entrada:
        s y d: listas binarias
    
    Salida:
        distancia: distancia hamming
    '''
    #Calcula la distancia hamming de dos listas
    #s lista original, d lista desplazada
    distancia=0
    for i in range(len(s)):
        if (s[i]!=d[i]):
            distancia = distancia + 1
    
    return distancia
#*****************************************************************************
def desplazar(s):
    '''
    Función que desplaza un lista una posición a la derecha
    
    Entrada:
        s: lista a desplazar
        
    Salida:
        d: lista desplazada
    '''
    d=[] #nueva lista desplazada
    d.append(s[len(s)-1])
    for i in range(len(s)-1):
        d.append(s[i])
    
    return d
    
#****************************************************************************

def tercerpostulado(s):
    '''
    Función que aplica el tercer postulado de golomb
    
    Entrada:
        s: lista binaria
    
    Salida:
        True si la distancia hamming se mantiene constante entre la secuencia
        original y todos los posibles desplazamientos de s
        
        False en caso contrario
    '''
    
    d = desplazar(s)      
    distancia = hamming(s,d)
    #Hay desplazar la cadena len(s)-1 veces
    #como ya la hemos desplazado una vez, hay que llegar hasta len(s)-2
    #Range para una unidad antes de llegar a stop
    #Equivale a parar cuando d==s
    for i in range(1,len(s)-1): 
        d = desplazar(d)
        if(distancia!=hamming(s,d)):
            return False
    return True
        
#*****************************************************************************
def golomb(s):
    '''
    Función que aplica el postulado de golomb a una secuencia binaria
    
    Entrada:
        s: secuencia binaria en forma de lista
    
    Salida:
        True si cumple los tres postulados
        False en caso contrario
    '''
    

    if(primerpostulado(s)==False): #si postulado da false, devuelve false
        return False
    if(segundopostulado(s)==False):
        return False
    if(tercerpostulado(s)==False):
        return False
    #Todos los postulados han dado True->devuelve True
    return True
#*****************************************************************************

s7=[0,0,0,1,1,1,1,0,1,0,1,1,0,0,1] #la cumple segun apuntes jesus
print segundopostulado(s7)

