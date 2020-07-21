import colas
import pilas
import random
import colas_dinamicas as ca

def llenarAleatoria(rand0, randf, n, cola):
    for i in range(n):
        cola.insertar(random.randint(rand0, randf))
    
    return cola

def llenarAleatoriaCaracteres(rand0, randf, n, cola):
    for i in range(n):
        cola.insertar(chr(random.randint(rand0, randf)))
    
    return cola

def vaciarCola(cola):
    for i in range(len(cola)):
        cola.eliminar()

def nPrimo(num):
    for i in range(2,num):
        if(num%i == 0):
            return False
    
    return True

def agregarListaCola(lista, cola):
    while lista != []:
        cola.insertar(lista.pop(0))

def esNumero(caracter):
    try:
        int(caracter)
        return True
    except ValueError:
        try:
            float(caracter)
            return True
        except ValueError:
            return False

colaAleatoria = ca.Cola()
llenarAleatoria(0,32,15,colaAleatoria)

#Ejercicio 1
'''
def quitarVocales(cola):
    tamanio = len(cola)
    vocales = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    for i in range(tamanio):
        if(cola.cabeza() in vocales):
            cola.eliminar()
        else:
            cola.insertar(cola.eliminar())

colaCaracteres = ca.Cola()

for i in range(50):
    colaCaracteres.insertar(chr(random.randint(65,122)))

print(colaCaracteres.lista())

quitarVocales(colaCaracteres)

print(colaCaracteres.lista())
'''

#Ejercicio 2
'''
pilaAux = pilas.Pila()

print(colaAleatoria.items)

while colaAleatoria.vacia() == False:
    pilaAux.apilar(colaAleatoria.eliminar())

while pilaAux.pilaVacia() == 0:
    colaAleatoria.insertar(pilaAux.desapilar())

print(colaAleatoria.items)
'''

#Ejercicio 3
'''
cadena = input("Ingresar frase: ")
pString = pilas.Pila()
colaString = colas.Cola()

pString.apilarCadena(cadena)
print(pString.pila)

while pString.pilaVacia() == 0:
    colaString.insertar(pString.desapilar())
'''

#Ejercicio 4
'''
print("Cola:")
print(colaAleatoria.lista())

for i in range(colaAleatoria.tamanio):
    if nPrimo(colaAleatoria.cabeza()):
        colaAleatoria.insertar(colaAleatoria.eliminar())
    else:
        colaAleatoria.eliminar()

print(colaAleatoria.lista())
'''


#Ejercicio 5
'''p1 = pilas.Pila()
c1 = colas.Cola()

p1.llenarPila(0,15,15)

print(p1)

for i in range(len(p1)):
    c1.insertar(p1.desapilar())

print(c1)
'''


#Ejercicio 6
'''
print(colaAleatoria)

num = int(input("Ingresa un numero: "))
contador = 0

for i in range(len(colaAleatoria)):
    if colaAleatoria.cabeza() == num:
        contador += 1
    
    colaAleatoria.insertar(colaAleatoria.eliminar())

print(f"El elemento {num} tiene {contador} ocurrencia/s en la lista anterior.")
'''


#Ejercicio 7
'''
print(colaAleatoria)

i_esimo = int(input("Ingresar la posicion del elemento sin contar el primero: "))

if(i_esimo < len(colaAleatoria)):
    colaAleatoria.insertar(colaAleatoria.eliminar())
    for i in range(len(colaAleatoria) - 2):
        if(i + 1 == i_esimo):
            colaAleatoria.eliminar()
        else:
            colaAleatoria.insertar(colaAleatoria.eliminar())

print(colaAleatoria)
'''
#Ejercicio 8

#Ejercicio 9
'''
vaciarCola(colaAleatoria)
llenarAleatoria(-15,15,15,colaAleatoria)
print(colaAleatoria)

negativos = 0
minimo = None
maximo = None

for i in range(len(colaAleatoria)):
    num = colaAleatoria.cabeza()
    if i == 0:
        minimo = num
        maximo = num
    elif((num < minimo) or (num > maximo)):
        if num < minimo:
            minimo = num
        else: 
            maximo = num

    if num < 0:
        negativos += 1

    colaAleatoria.insertar(colaAleatoria.eliminar())

print(f"La cola tiene {negativos} elemento/s negativo/s.")
print(f"El rango de la cola es: {maximo - minimo} ")
'''

#Ejercicio 10


#Ejercicio 11
'''
cO1 = colas.Cola()
cO2 = colas.Cola()
cOrdenada = colas.Cola()

listaO1 = [0,2,4,8,9,16]
listaO2 = [1,4,7,8,9,15,16]

agregarListaCola(listaO1, cO1)
agregarListaCola(listaO2, cO2)

print(f"Lista ordenada 1: {cO1}")
print(f"Lista ordenada 2: {cO2}")

while not cO1.vacia() or not cO2.vacia():
    if(cO1.vacia()):
        cOrdenada.insertar(cO2.eliminar())
    elif (cO2.vacia()):
        cOrdenada.insertar(cO2.eliminar())
    elif(cO1.cabeza()<=cO2.cabeza()):
        cOrdenada.insertar(cO1.eliminar())
    else:
        cOrdenada.insertar(cO2.eliminar()) 

print(f"Lista ordenada resultante: {cOrdenada}")
'''

#Ejercicio 12
colaChar = colas.Cola()
digitos = colas.Cola()
otros = colas.Cola()

char1 = False
char2 = False

caracteres = 0
letras = 0

llenarAleatoriaCaracteres(33,128,50000,colaChar)

while not colaChar.vacia():
    if esNumero(colaChar.cabeza()):
        digitos.insertar(colaChar.eliminar())
    else:
        otros.insertar(colaChar.eliminar())

for i in range(len(otros)):
    if(otros.cabeza().isalpha()):
        letras += 1
    
    if char1 == False or char2 == False:
        if otros.cabeza() == '?':
            char1 = True
        elif(otros.cabeza() == '#'):
            char2 = True

    caracteres += 1
    otros.insertar(otros.eliminar())



print(f"En la cola hay {letras} letras")
print(f"El caracter '?' esta en la cola: {char1}")
print(f"El caracter '#' esta en la cola: {char2}")

