import colas
import pilas
import random
import colas_dinamicas as ca
import math as m
import time

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
def insertar_ordenado(cola, dato, campo = None):
    colaAux = colas.Cola()
        
    while cola.vacia() == False:
        if criterio(dato, campo) < criterio(cola.cabeza(), campo):
            colaAux.insertar(dato)
        else:
            colaAux.insertar(cola.eliminar())

    while not colaAux.vacia():
        cola.insertar(colaAux.eliminar())


def criterio(dato, campo=None):
    """Determina el campo por el cual se debe comparar el dato."""
    dic = {}
    if(hasattr(dato, '__dict__')):
        dic = dato.__dict__
    if campo is None or campo not in dic:
        return dato
    else:
        return dic[campo]

colaOrdenada = colas.Cola()
for i in range(10):
    insertar_ordenado(colaOrdenada, random.randint(0,20))


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
'''class Personaje(object):
    def __init__(self, nombre, origen):
        self.nombre = nombre
        self.origen = origen

    def __str__(self):
        return "Nombre: " + self.nombre + "\n" + "Planeta de origen: " + self.origen + "\n"
'''
def buscar(cola, dato, campo = None):
    resultado = None
    for i in range(len(cola)):
        elemento = cola.eliminar()
        if criterio(elemento, campo) == dato:
            resultado = elemento
        cola.insertar(elemento)
    return elemento

def mostrar(cola, valor, campo = None):
    for i in range(len(cola)):
        elemento = cola.eliminar()
        if criterio(elemento, campo) == valor:
            print(elemento)
        cola.insertar(elemento)

def insertar_antes(cola, dato, valor, campo = None):
    for i in range(len(cola)):
        elemento = cola.eliminar()
        if criterio(elemento, campo) == valor:
            cola.insertar(dato)
        cola.insertar(elemento)

def eliminar_despues(cola, valor, campo = None):
    colaAux = colas.Cola()
    while not cola.vacia():
        elemento = cola.eliminar()
        colaAux.insertar(elemento)
        if criterio(elemento, campo) == valor and not cola.vacia():
            resultado = cola.eliminar()

    return resultado
'''

colaPersonajes = colas.Cola()

colaPersonajes.insertar(Personaje("Luke Skywalker", "Alderaan"))
colaPersonajes.insertar(Personaje("Han Solo", "Endor"))
colaPersonajes.insertar(Personaje("Yoda", "Tatooine"))
colaPersonajes.insertar(Personaje("Jar Jar Binks", "Alderaan"))
colaPersonajes.insertar(Personaje("asd", "Tatooine"))
colaPersonajes.insertar(Personaje("asd", "ASD"))

print("Personajes del planeta Alderaan")
mostrar(colaPersonajes, 'Alderaan', 'origen')
print("\nPersonajes del planeta Endor")
mostrar(colaPersonajes, 'Endor', 'origen')
print("\nPersonajes del planeta Tatooine")
mostrar(colaPersonajes, 'Tatooine', 'origen')

print(f"El planeta de Luke Skywalker es {buscar(colaPersonajes, 'Luke Skywalker', 'nombre').origen}")
print(f"El planeta de Han Solo es {buscar(colaPersonajes, 'Han Solo', 'nombre').origen}")

nom = input("Nombre: ")
origen = input("Origen: ")

insertar_antes(colaPersonajes, Personaje(nom, origen), 'Jar Jar Binks', 'nombre')
print(colaPersonajes)'''






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
'''colaChar = colas.Cola()
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
'''


#13
'''
class Semaforo(object):
    def __init__(self,idSemaforo, amarillo, verde):
        self.idSemaforo = idSemaforo
        self.tiempoAmarillo = amarillo
        self.tiempoVerde = verde

    def funcionar(self):
        print(f"Semaforo nro {self.idSemaforo}")
        print(f"Encender luz amarilla durante {self.tiempoAmarillo} segundos")
        print(f"Encender luz verde durante {self.tiempoVerde} segundos")
        print(f"Encender luz amarilla durante {self.tiempoAmarillo} segundos")
        print(f"Encender luz Roja")

colaSemaforos = colas.Cola()

for i in range(4):
    colaSemaforos.insertar(Semaforo(i,2,30))

vueltas = 2

for i in range(vueltas):
    print(f"Vuelta {i+1}")
    for j in range(len(colaSemaforos)):
        oSemaforo = colaSemaforos.eliminar()
        oSemaforo.funcionar()
        colaSemaforos.insertar(oSemaforo)'''

#14 No se por que me tira math error
class Base(object):
    def __init__(self, nombre, flotaAerea, coordenadas):
        self.nombre = nombre
        self.flotaAerea = flotaAerea
        self.coordenadas = coordenadas

    def __str__(self):
        return "Nombre: " + self.nombre + "\n"\
            "Flota aerea: " + str(self.flotaAerea) + "\n"\
            "Coordenadas: " + "(" + str(self.coordenadas[0]) + "," + str(self.coordenadas[0]) + ")\n" 

def funcion_distancia(ubicacionBase, ubicacionActual):
    r = 6371000
    #latitud[A] longitud[B]
    Af = ubicacionBase[0]
    Bf = ubicacionBase[1]
    
    Ai = ubicacionActual[0]
    Bi = ubicacionActual[1] 

    #m.sin(m.pow((Ai - Af)/2 ,2))
    #m.sin(m.pow(((Bi - Bf)/2),2))
    
    return #2*r*m.asin(m.sqrt(m.sin(m.pow((Ai - Af)/2 ,2)) + (m.cos(Ai)* m.cos(Af) * m.sin(m.pow(((Bi - Bf)/2),2)))))

'''

bases = [
    Base("Base 1", 32, (15, 10)),
    Base("Base 2", 32, (20, 25)),
    Base("Base 3", 32, (55, 66)),
    Base("Base 4", 32, (72, 50))
]

colaBases = colas.Cola()

for base in bases:
    colaBases.insertar(base)

ubicacionActual = (20,10)

for i in range(len(colaBases)):
    base = colaBases.eliminar()
    print(funcion_distancia(base.coordenadas, ubicacionActual))'''



#Ejercicio 15

#Ejercicio 16
'''class Proceso(object):
    def __init__(self, idProceso, descripcion, tiempo):
        self.idProceso = idProceso
        self.descripcion = descripcion
        self.tiempo = tiempo

colaProcesos = colas.Cola()

colaProcesos.insertar(Proceso('1','copiando archivos', 2.7))
colaProcesos.insertar(Proceso('2','descomprimiendo archivos', 5))
colaProcesos.insertar(Proceso('4','terminando instalacion', 0.7))

#C
while colaProcesos.vacia() == False:
    proceso = colaProcesos.eliminar()

    print(f"Proceso. {proceso.descripcion} ({proceso.tiempo}s) ")
    if proceso.tiempo > 4.5:
        time.sleep(4.5)
        proceso.tiempo -= 4.5
        colaProcesos.insertar(proceso)
    else:
        time.sleep(proceso.tiempo)'''

#Ejercicio 17
'''colaTurnos = colas.Cola()

letras = ['A', 'B', 'C', 'D', 'E', 'F']

contadores = {
    "A" : 0,
    "B" : 0,
    "C" : 0,
    "D" : 0,
    "E" : 0,
    "F" : 0
}

cola_1 = colas.Cola()
cola_2 = colas.Cola()

for i in range(1000):
    codigo = random.choice(letras) + str(random.randint(0,999)).zfill(3)
    colaTurnos.insertar(codigo)

for i in range(len(colaTurnos)):
    turno = colaTurnos.eliminar()
    contadores[turno[0:1]] += 1
    if 'A' in turno or 'C' in turno or 'F' in turno:
        cola_1.insertar(turno)
    else:
        cola_2.insertar(turno)
    colaTurnos.insertar(turno)

if len(cola_1) > len(cola_2):
    print("La cola 1 tiene mayor cantidad de turnos")
    if contadores["A"] < contadores["C"]:
        if contadores["C"] < contadores["F"]:
            print("La letra F tiene mayor cantidad de turnos")
        else:
            print("La letra C tiene mayor cantidad de turnos")
    else:
        if contadores["A"] < contadores["F"]:
            print("La letra F tiene mayor cantidad de turnos")
        else:
            print("La letra A tiene mayor cantidad de turnos")
    print("Turnos cuyo numero es mayor a 506")
    for i in range(len(cola_2)):
        codigo = cola_2.eliminar()
        if int(codigo[1:]) > 506:
            print(codigo)
        cola_2.insertar(codigo)

else:
    print("La cola 2 tiene mayor cantidad de turnos")
    if contadores["B"] < contadores["D"]:
        if contadores["D"] < contadores["E"]:
            print("La letra E tiene mayor cantidad de turnos")
        else:
            print("La letra D tiene mayor cantidad de turnos")
    else:
        if contadores["B"] < contadores["E"]:
            print("La letra E tiene mayor cantidad de turnos")
        else:
            print("La letra B tiene mayor cantidad de turnos")
    print("Turnos cuyo numero es mayor a 506")
    for i in range(len(cola_1)):
        codigo = cola_1.eliminar()
        if int(codigo[1:]) > 506:
            print(codigo)
        cola_1.insertar(codigo) 
'''

#Ejercicio 19
'''class Vehiculo(object):
    def __init__(self, tupla):
        self.tipo = tupla[0]
        self.precio = tupla[1]

class Cabina(object):
    def __init__(self, vehiculos):
        self.vehiculos = vehiculos
        self.recaudacion = 0
        self.Autos = 0
        self.Camionetas = 0
        self.Camiones = 0
        self.Colectivos = 0
        self.calcular()

    def calcular(self):
        for i in range(len(self.vehiculos)):
            vehiculo = self.vehiculos.eliminar()
            if vehiculo.tipo == "automovil":
                self.Autos += 1
            elif vehiculo.tipo == "camion":
                self.Camiones += 1
            elif vehiculo.tipo == "camioneta":
                self.Camionetas += 1
            elif vehiculo.tipo == "colectivo":
                self.Colectivos += 1
    
            self.recaudacion += vehiculo.precio

            self.vehiculos.insertar(vehiculo)


tipos = [("automovil", 47), ("camioneta", 59), ("camion", 71), ("colectivo", 64)]

vehiculos_1 = colas.Cola()
vehiculos_2 = colas.Cola()
vehiculos_3 = colas.Cola()

for i in range(30):
    vehiculos_1.insertar(Vehiculo(random.choice(tipos)))
    vehiculos_2.insertar(Vehiculo(random.choice(tipos)))
    vehiculos_3.insertar(Vehiculo(random.choice(tipos)))

cabinas = [Cabina(vehiculos_1) ,Cabina(vehiculos_2), Cabina(vehiculos_3)]

if cabinas[0].recaudacion < cabinas[1].recaudacion:
    if cabinas[1].recaudacion < cabinas[2] .recaudacion:
        print("La cabina 3 es la que mas recaudo")
    else:
        print("La cabina 2 es la que mas recaudo")
else:
    if cabinas[0].recaudacion < cabinas[2] .recaudacion:
        print("La cabina 3 es la que mas recaudo")
    else:
        print("La cabina 1 es la que mas recaudo")

for cabina in cabinas:
    print("Los vehiculos que se atendireon en esta cabina son:")
    print(f"Automoviles: {cabina.Autos}")
    print(f"Camiones: {cabina.Camiones}")
    print(f"Camionetas: {cabina.Camionetas}")
    print(f"Colectivos: {cabina.Colectivos}")'''


#Ejercicio 20


#Ejercicio 21
class PersonajeMCU(object):
    def __init__(self, nombrePersonaje, nombreSuperheroe, genero):
        self.nombrePersonaje = nombrePersonaje
        self.nombreSuperheroe = nombreSuperheroe
        self.genero = genero

    def __str__(self):
        return "Nombre de personaje: " + self.nombrePersonaje + "\n"\
        "Nombre de personaje: " + self.nombreSuperheroe + "\n"\
        "Nombre de personaje: " + self.genero + "\n"

superheroes = colas.Cola()

superheroes.insertar(PersonajeMCU("asdgjllk", "Capitana Marvel", "F"))
superheroes.insertar(PersonajeMCU("Scott Lang", "asdsdw", "M"))
superheroes.insertar(PersonajeMCU("Carol Danvers", "ppoiui", "F"))
superheroes.insertar(PersonajeMCU("Vdsad", "asdsdw", "M"))
superheroes.insertar(PersonajeMCU("Tdsade", "Plsksf", "F"))

f = False

print("Nombre del personaje de Capitana Marvel")
for i in range(len(superheroes)):
    personaje = superheroes.eliminar()
    if personaje.nombreSuperheroe == "Capitana Marvel":
        print(personaje.nombrePersonaje)
    if personaje.nombrePersonaje == "Carol Danvers":
        f = True

    superheroes.insertar(personaje)

print("Nombre de los personajes Femeninos")
for i in range(len(superheroes)):
    personaje = superheroes.eliminar()
    if personaje.genero == "F":
        print(personaje.nombrePersonaje)
    superheroes.insertar(personaje)

print("Nombre de los personajes Masculino")
for i in range(len(superheroes)):
    personaje = superheroes.eliminar()
    if personaje.genero == "M":
        print(personaje.nombrePersonaje)
    superheroes.insertar(personaje)

print("Nombre del superheroes de Scott Lang")
for i in range(len(superheroes)):
    personaje = superheroes.eliminar()
    if personaje.nombrePersonaje == "Scott Lang":
        print(personaje.nombreSuperheroe)
    superheroes.insertar(personaje)

print("Personajes cuyo nombre o nombre de superheroe comienza con la letra S")
for i in range(len(superheroes)):
    personaje = superheroes.eliminar()
    if personaje.nombrePersonaje[0] == "S" or personaje.nombreSuperheroe[0] == "S":
        print(personaje)
    superheroes.insertar(personaje)

