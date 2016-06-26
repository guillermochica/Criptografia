# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 19:39:59 2016

@author: guillermo
"""
from test_primalidad import esprimo
from raices_modulares import jacobi
from logaritmo_discreto import petitpasgrandpas

#*****************************************************************************
def primitivo(fecha):
    """
    Función que, dada la función Zp->Zp x->a^x,
    calcula el inverso de mi fecha de nacimiento
    
    Entrada:
        fecha: El valor de la fecha de nacimiento en formato AAAMMDD
    
    Salida: El inverso de la fecha de nacimiento
    """
    #Encuentra un elemento primitivo alfa de Zp
    #n es fecha de nacimiento
    
    #Buscamos un pseudoprimo mayor o igual que mi DNI
    p = 77378395
    
    primo = False
    while not primo:
        if (esprimo(p,10) and esprimo((p-1)/2,10) ):
            primo = True
        else:
            p = p+2
    
    #Búsqueda del elemento primitivo    
    primitivo = False
    alfa = 2
    while not primitivo:
        if (jacobi(alfa,p) == -1):
            primitivo = True
        else:
            alfa = alfa +1
    #La inversa de la función es el logaritmo discreto
    inv = petitpasgrandpas(alfa,fecha,p)
    return inv
    print expmod(alfa,inv,p)
#*****************************************************************************
fecha = 19930530
print primitivo(fecha)