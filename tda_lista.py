import random


class nodoLista(object):

    def __init__(self):
        self.info = None
        self.sig = None
        

class Lista(object):

    def __init__(self):
        self.inicio = None
        self.tamanio = 0


def insertar(lista, dato, campo=None):
    nodo = nodoLista()
    nodo.info = dato
    if(lista.inicio is None or criterio(lista.inicio.info,campo)>criterio(nodo.info,campo)):
        nodo.sig = lista.inicio
        lista.inicio = nodo
    else:
        act = lista.inicio.sig
        ant = lista.inicio
        while(act is not None and criterio(act.info,campo)<criterio(nodo.info,campo)):
            act = act.sig
            ant = ant.sig

        nodo.sig = act
        ant.sig = nodo

    lista.tamanio += 1    

def insertarDesc(lista, dato, campo=None):
    nodo = nodoLista()
    nodo.info = dato
    if(lista.inicio is None or criterio(lista.inicio.info,campo)<criterio(nodo.info,campo)):
        nodo.sig = lista.inicio
        lista.inicio = nodo
    else:
        act = lista.inicio.sig
        ant = lista.inicio
        while(act is not None and criterio(act.info,campo)>criterio(nodo.info,campo)):
            act = act.sig
            ant = ant.sig

        nodo.sig = act
        ant.sig = nodo

    lista.tamanio += 1

def eliminar(lista, clave, campo=None):
    dato = None
    if(criterio(lista.inicio.info,campo) == clave):
        dato = lista.inicio
        lista.inicio = lista.inicio.sig
        lista.tamanio -= 1
    else:
        act = lista.inicio.sig
        ant = lista.inicio
        while(act is not None and criterio(act.info,campo) != clave):
            act = act.sig
            ant = ant.sig
        
        if(act is not None):
            dato = act
            ant.sig = act.sig
            lista.tamanio -= 1

    return dato



def busqueda(lista, clave, campo=None):
    aux = lista.inicio
    while(aux is not None and criterio(aux.info, campo) != clave):
        aux = aux.sig
    return aux


def barrido(lista):
    aux = lista.inicio
    while(aux is not None):
        print(aux.info)
        aux = aux.sig
    
def barridoObjeto(lista):
    aux = lista.inicio
    while(aux is not None):
        print(aux.info.__dict__)
        print()
        aux = aux.sig

def tamanio(lista):
    return lista.tamanio


def lista_vacia(lista):
    return lista.inicio is None


def criterio(dato, campo=None):
    """Determina el campo por el cual se debe comparar el dato."""
    dic = {}
    if(hasattr(dato, '__dict__')):
        dic = dato.__dict__
    if campo is None or campo not in dic:
        return dato
    else:
        return dic[campo]


# from random import randint
# lista1 = Lista()
# lista2 = Lista()
# listaaux = Lista()


# for i in range (10):
#     insertar(lista1, randint(0,20))
#     insertar(lista2, randint(0,20))

# print('lista 1')
# barrido(lista1)
# print('lista 2')
# barrido(lista2)

# repetidos = 0
# aux = lista2.inicio
# while(aux is not None):
#     pos = busqueda(lista1, aux.info)
#     if(pos is None):
#         insertar(lista1, aux.info)
#     else:
#         repetidos += 1
#     aux = aux.sig

# print('cantidad de repetidos', repetidos)
# print('lista concatenadas')
# barrido(lista1)





'''
aux = lista1.inicio
while(aux.sig is not None):
    aux = aux.sig

aux.sig = lista2.inicio

print('lista concatenadas')
barrido(lista1)
'''