# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 19:52:09 2016

@author: guillermo
"""
from euclides import mcd,inverso
from hashlib import sha224
from powermod import expmod
#*****************************************************************************
def clavesRSA(p,q):
    """
    Generación de claves RSA. Las guarda en su correspondiente fichero.
    
    Entrada: 
        p,q: primos grandes y distantes entres sí
    
    Salida:
        e,n: clave publica
        d: clave privada
    """
    
    n = p*q
    phi = (p-1)*(q-1)
    
    e = 2
    while(mcd(phi,e)[0]!=1):
        e = e +1
    
    d = inverso(e,phi)
    
    #Abrimos con permisos de escritura los ficheros donde se guardarán las claves
    fpub = open("pub","w")
    fpriv = open("priv","w")
    
    #Escribimos en un fichero la clave publica y privada, separando e y d de n con un espacio
    fpub.write(str(e)+" ")
    fpub.write(str(n))
    
    fpriv.write(str(d)+" ")
    fpriv.write(str(n))
    
    return e,n,d
#*****************************************************************************
def firmaRSA(priv,m):
    """
    Firma RSA -> r^d mod n=f . Guarda la firma en un fichero
    
    Entrada:
        priv: nombre del fichero de la clave privada en string (d y n)
        m: nombre del fichero del mensaje a firmar en string
    Salida:
        f: firma del resumen del mensaje
    """
    #Abrimos el fichero de mensaje
    myfile = open(m)
    #Lo guardamos en una variable como string
    m = myfile.read()    
    #Calculamos un resumen del mensaje
    r = sha224(m).hexdigest()
    #Convertimos de hexadecimal a entero base 10 para poder operar con el resumen
    r = int("0x"+r,0)
    
    #Leemos la clave del fichero
    fpriv = open(priv)
    clave = fpriv.read().split(" ")
    d = int(clave[0])
    n = int(clave[1])
    
    
    #firma del resumen:
    f = expmod(r,d,n)
    
    ffirma = open("firma","w")
    ffirma.write(str(f))
    
    return f
#*****************************************************************************
def verificacionRSA(pub,m,f):
    """
    Verificación de firma RSA-> f^e mod n=resumen mod n
    
    Entrada:
        pub: nombre del fichero de la clave publica en string (e y n)
        m: nombre del fichero del mensaje a verificar en string
        f: nombre del fichero de firma en string
    
    Salida:
        True: si la firma es correcta
        False si no
    """
    #Abrimos el fichero de mensaje
    myfile = open(m)
    #Lo guardamos en una variable como string
    m = myfile.read()
    #Calculamos un resumen del mensaje
    r=sha224(m).hexdigest()
    #Convertimos de hexadecimal a base 10 para poder comparar con v
    r = int("0x"+r,0)
    
    
    #Leemos la clave del fichero
    fpub = open(pub)
    clave = fpub.read().split(" ")
    e = int(clave[0])
    n = int(clave[1])
    
    #Leemos el fichero con la firma
    ffirma = open("firma")
    f = int(ffirma.read())
    
    #verificacion
    v = expmod(f,e,n)

    
    if(v==r%n): #si la verificacion coincide con el resumen mod n->True
        return True
    else:
        return False

#*****************************************************************************
clavesRSA(1081298104698286063813737967304568031406522676857739555339880517562925221530558524296599584286163751908713364829390795648074146197550782524900963175263757603219
,204616454475328391399619135615615385636808455963116802820729927402260635621645177248364272093977747839601125961863785073671961509749189348777945177811)

m = 'mensaje' #el nombre del fichero mensaje, para abrirlo después
priv = "priv" #el nombre del fichero de clave privada
pub = "pub" #el nombre del fichero de clave publica
f = "firma" #el nombre del fichero de la firma
firmaRSA(priv,m)
print verificacionRSA(pub,m,f)

    
