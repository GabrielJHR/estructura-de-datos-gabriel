class NodoListaDoble(object):
	def __init__(self):
		self.info = None
		self.ant = None
		self.sig = None

class ListaDoble(object):
    def __init__(self):
        self.tamanio = 0
        self.inicio = None
        self.fin = self.inicio

# Agrega elementos en forma ordenada
def insertar(lista, dato, campo=None):
    nodo = NodoListaDoble()
    nodo.info = dato
    if(lista.inicio is None or criterio(lista.inicio.info,campo)>criterio(nodo.info,campo)):
        nodo.sig = lista.inicio
        lista.inicio = nodo
        if lista.inicio.sig is not None:
           lista.inicio.sig.ant = nodo

    else:
        act = lista.inicio.sig
        ant = lista.inicio
        while(act is not None and criterio(act.info,campo)<criterio(nodo.info,campo)):
            act = act.sig
            ant = ant.sig

        nodo.sig = act
        ant.sig = nodo
        nodo.ant = ant

        if act is not None:
            act.ant = nodo
    
    if nodo.sig is None:
        lista.fin = nodo

    lista.tamanio += 1 

def insertarAlFinal(lista, dato):
    nodo = NodoListaDoble()
    nodo.info = dato
    
    if lista.inicio is None:
        lista.fin = nodo
        lista.inicio = nodo
    else:
        nodo.ant = lista.fin
        lista.fin.sig = nodo
        lista.fin = nodo

def barrido(lista):
    aux = lista.inicio
    while(aux is not None):
        print(aux.info)
        aux = aux.sig

def criterio(dato, campo=None):
    """Determina el campo por el cual se debe comparar el dato."""
    dic = {}
    if(hasattr(dato, '__dict__')):
        dic = dato.__dict__
    if campo is None or campo not in dic:
        return dato
    else:
        return dic[campo]