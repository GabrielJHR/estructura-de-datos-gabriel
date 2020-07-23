import random
import pilas
import tp01


def Buscar(vector, elemento):
	if(vector == []):
		return 0
	else:
		num = vector[-1]
		
		if(num == elemento):
			return 1
		else:
			return Buscar(vector[0:-1] , elemento)


def OrdenarPila(pila): 
    pAux = pilas.Pila() 
    while(pila.pilaVacia() == 0): 
        
        num = pila.desapilar() 
        
        while(pAux.pilaVacia() == 0 and pAux.pila[-1] < num):
            
            pila.apilar(pAux.desapilar())
  
        pAux.apilar(num) 
    
    pAux.vaciarPila(pila)
    return pila

def Promedio(pila):
	pAux = pilas.Pila()
	longitud = len(pila.pila)
	promedio = 0

	while pila.pilaVacia() == 0:
		pAux.apilar(pila.desapilar())
		promedio = promedio + (pAux.pila[-1] / longitud)

	pAux.vaciarPila(pila)
	return promedio


pilaNumeros = pilas.Pila()
pilaNumeros.llenarPila(0,15,15)


#Ejercicio 1
'''pAux = pilas.Pila()

print(pilaNumeros.pila)

while pilaNumeros.pilaVacia() == 0:
	num = pilaNumeros.pila[-1]
	contador = 0
	while pilaNumeros.pilaVacia() == 0:
		if pilaNumeros.pila[-1] == num:
			contador = contador + 1
			pilaNumeros.desapilar()
		else:
			pAux.apilar(pilaNumeros.desapilar())

	print(f"Cantidad de ocurrencias del elemento '{num}': {contador}")
	pAux.vaciarPila(pilaNumeros)
'''


#Ejercicio 2
'''pares = pilas.Pila()

while pilaNumeros.pila != []:
	num = pilaNumeros.desapilar()
	
	if(num % 2 == 0):
		pares.apilar(num)

while pares.pila != []:
	pilaNumeros.apilar(pares.desapilar())

print(pilaNumeros.pila)'''





#Ejercicio 3
'''pAux = pilas.Pila();

while pilaNumeros.pila != []:
	n = pilaNumeros.desapilar();

	if(Buscar(pAux.pila, n) == 0):
		pAux.apilar(n)
	else:
		pilaNumeros.apilar(random.randint(0,15))

pilaNumeros.apilarVector(pAux.pila)

print(pilaNumeros.pila)'''





#Ejercicio 4
'''print(pilaNumeros.pila)
pAux = pilas.Pila()

pilaNumeros = pilaNumeros.vaciarPila(pAux)

print(pilaNumeros.pila)
'''



#Ejercicio 5
'''cadena = "neuquen"
pString = pilas.Pila()
pStringAux = pilas.Pila()

pString.apilarCadena(cadena)

while cadena != "":
	pStringAux.apilar(cadena[-1])
	cadena = cadena[0:-1]

print(pStringAux.pila == pString.pila)'''





#Ejercicio 6
'''cadena = "Esto es una cadena."
cadenaInversa = ""

pString = pilas.Pila()

pString.apilarCadena(cadena)

while pString.pila != []:
	cadenaInversa = cadenaInversa + pString.desapilar()

print(cadenaInversa)'''




#Ejercicio 7
'''i_esimo = 12

pAux = pilas.Pila()
print("Pila original: ", pilaNumeros.pila)
print(f"Pila sin el elemento {pilaNumeros.pila[-i_esimo]}: ")

while i_esimo >= 0 :
	
	i_esimo = i_esimo-1
	
	if i_esimo != 0:
		pAux.apilar(pilaNumeros.desapilar())
	else:
		pilaNumeros.desapilar()

pilaNumeros.apilarVector(pAux.pila)

print(pilaNumeros.pila)'''




#Ejercicio 8
'''def ordenarCartas(mazo):
	mazoAux = pilas.Pila()
	mazoAux2 = pilas.Pila()

	for i in range(1,13):
		while mazo.pilaVacia() == 0:
			carta = mazo.desapilar();
			if(carta[0] == i):
				mazoAux.apilar(carta)
			else:
				mazoAux2.apilar(carta)
		mazo.apilarVector(mazoAux2.pila)
		mazo.apilarVector(mazoAux.pila)
		mazoAux.vaciarPila();
		mazoAux2.vaciarPila();

	return mazo

#main

mazo = pilas.Pila()
mazoOro = pilas.Pila()
mazoEspada = pilas.Pila()
mazoCopas = pilas.Pila()
mazoBasto = pilas.Pila()

palos = ["Espada", "Copa", "Basto", "Oro"]
carta = ( 0 , "palo")

i = 0

for i in range(48):
	carta = (random.randint(1,12), random.choice(palos))

	if(Buscar(mazo.pila, carta) == 0):
		mazo.apilar(carta)

while mazo.pilaVacia() == 0:
	carta = mazo.desapilar()

	if carta[1] == "Oro":
		mazoOro.apilar(carta)
	elif carta[1] == "Espada":
		mazoEspada.apilar(carta)
	elif carta[1] == "Copas":
		mazoCopas.apilar(carta)
	elif carta[1] == "Basto":
		mazoBasto.apilar(carta)

print(mazoOro.pila)
print(ordenarCartas(mazoOro).pila)
'''



#Ejercicio 9
'''pFactorial = pilas.Pila()
factorial = 1;
num = 4

for i in range(num):
	pFactorial.apilar(num - i)

while pFactorial.pilaVacia() == 0:
	factorial = factorial * pFactorial.desapilar()

print(factorial)'''




#Ejercicio 10
'''dioses = ["Afrodita", "Apolo", "Ares", "Artemisa", "Dionisio", "Hefesto", "Hera", "Hermes", "Hades", "Poseidón", "Zeus"]

pDioses = pilas.Pila()
pAux = pilas.Pila()

pDioses.apilarVector(dioses)

n_esima = 8

while n_esima - 1 > 0:
	n_esima = n_esima - 1
	pAux.apilar(pDioses.desapilar())


pDioses.apilar("Atenea")

pDioses.apilarVector(pAux.pila)
pAux.vaciarPila()

print(pDioses.pila)'''



#Ejercicio 11
'''cadena = input("Ingresar frase: ")
pString = pilas.Pila()
vocales = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
cVocales = 0

pString.apilarCadena(cadena)

while pString.pilaVacia() == 0:
	letra = pString.desapilar()

	if(Buscar(vocales, letra)):
		cVocales = cVocales + 1

print(f"La cantidad de vocales que tiene la frase '{cadena}' es {cVocales}")'''




#Ejercicio 12
'''def buscarPersonaje(personajes, personaje):
	pAux = pilas.Pila()
	
	while personajes.pilaVacia() == 0:
		elemento = personajes.desapilar()
		if elemento == personaje:
			pAux.vaciarPila(personajes)
			return True

	pAux.vaciarPila(personajes)
	return False


personajes = pilas.Pila()
personajes.apilarVector(["Darth Vader", "Chewbacca", "Yoda", "R2-D2", "Luke Skywalker", "C3PO", "Anakin Skywalker", "Obi-Wan Kenobi", "Han Solo", "Leia Organa", "Jabba the Hutt"])

if(buscarPersonaje(personajes, "Leia Organa") == True) or (buscarPersonaje(personajes, "Boba Fett") == True):
	print("Leia Organa o Boba Fett se encuentran dentro de la lista de personajes de Star Wars.")
else:
	print("Leia Organa o Boba Fett se encuentran dentro de la lista de personajes de Star Wars.")'''



#Ejercicio 13
'''
print(pilaNumeros.pila)

OrdenarPila(pilaNumeros)

print(pilaNumeros.pila)
'''


#Ejercicio 14
'''def quicksort_pila(pila):
	pila_izq = pilas.Pila()
	pila_der = pilas.Pila()

	if len(pila) <= 1:
		return pila
	else:
		pivote = pila.desapilar()
		for i in range(len(pila)):
			comparar = pila.desapilar()
			if comparar <= pivote:
				pila_izq.apilar(comparar)
			else:
				pila_der.apilar(comparar)

	izq = quicksort_pila(pila_izq)
	der = quicksort_pila(pila_der)
	izq.apilar(pivote)
	aux = pilas.Pila()

	for i in range(len(der)):
		aux.apilar(der.desapilar())
	
	for i in range(len(aux)):
		izq.apilar(aux.desapilar())

	return izq

print("Desordenado:")
print(pilaNumeros)
print("Ordenado:")
print(quicksort_pila(pilaNumeros))
'''


#Ejercicio 15
'''def interseccion(pila1, pila2):
	p1_aux = pilas.Pila()
	p2_aux = pilas.Pila()
	p_interseccion = pilas.Pila()

	while pila1.pilaVacia() == 0:
		while pila2.pilaVacia() == 0:
			if pila1.cima() == pila2.cima():
				p_interseccion.apilar(pila1.cima())

			p2_aux.apilar(pila2.desapilar())

		while p2_aux.pilaVacia() == 0:
			pila2.apilar(p2_aux.desapilar())

		p1_aux.apilar(pila1.desapilar())
	while p1_aux.pilaVacia() == 0:
		pila1.apilar(p1_aux.desapilar())

	return p_interseccion


pilaPersonajesV = pilas.Pila()
pilaPersonajesVII = pilas.Pila()

while True:
	personaje = input("Ingresar personaje de Star Wars episodio V: ")
	if personaje == '':
		break
	pilaPersonajesV.apilar(personaje)

while True:
	personaje = input("Ingresar personaje de Star Wars episodio VII: ")
	if personaje == '':
		break
	pilaPersonajesVII.apilar(personaje)

print("\nPersonajes que estan en los dos episodios: ")
print(interseccion(pilaPersonajesV, pilaPersonajesVII))'''





#Ejercicio 16
'''
def is_a_number(val):
	try:
		int(val)
	except ValueError:
		return 0

	return 1

pString = pilas.Pila()
pVocales = pilas.Pila()
pConsonantes = pilas.Pila()
pSimbolos = pilas.Pila()

cadena = input("Ingrese una frase: ")
pString.apilarCadena(cadena)
vocales = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
consonantes = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z", "b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]


cEspacio = 0
cNumero = 0
z = 0

print(cadena)

while pString.pilaVacia() == 0:
	caracter = pString.desapilar()
	if(Buscar(vocales, caracter) == 1):
		pVocales.apilar(caracter)
	elif(Buscar(consonantes, caracter) == 1):
		if caracter == "z" or caracter == "Z":
			z = 1
		pConsonantes.apilar(caracter)
	else:
		pSimbolos.apilar(caracter)
		if(caracter == " "):
			cEspacio = cEspacio + 1
		elif(is_a_number(caracter) == 1):
			cNumero = cNumero + 1

if z > 0:
	print("La frase contiene al menos una 'z'.")
else:
	print("La frase no contiene ninguna 'z'.")

print(f"La cantidad de vocales es {len(pVocales.pila)}, de consonantes {len(pConsonantes.pila)} y otros {len(pSimbolos.pila)}.")
print(f"La cantidad de numeros es {cNumero}.")
if len(pVocales.pila) == len(pSimbolos.pila):
	print("El numero de vocales es igual al numero de otros caracteres.")
else:
	print("El numero de vocales es distinto al de otros caracteres.")

print("El porcentaje de vocales con respecto a cosonantes es ", len(pVocales.pila) / (len(pVocales.pila) + len(pConsonantes.pila)) * 100 ,"%")
'''

#Ejercicio 17
'''def ordenarPeso(pila):
	menor = pila.cima()[1]
	auxPila = pilas.Pila()
	pilaOrdenada = pilas.Pila()
		
	while pila.pilaVacia() == 0:
		menor = pila.cima()[1]
		while pila.pilaVacia() == 0:
			if pila.cima()[1] <= menor:
				menor = pila.cima()[1]
			auxPila.apilar(pila.desapilar())

		while auxPila.pilaVacia() == 0:
			if auxPila.cima()[1] == menor:
				pilaOrdenada.apilar(auxPila.desapilar())
			else:
				pila.apilar(auxPila.desapilar())
	
	return pilaOrdenada

pilaOficina = pilas.Pila()

pilaOficina.apilar(("Objeto 1", 1.5))
pilaOficina.apilar(("Objeto 2", 2.5))
pilaOficina.apilar(("Objeto 3", 0.5))
pilaOficina.apilar(("Objeto 4", 4.5))
pilaOficina.apilar(("Objeto 5", 3.35))
pilaOficina.apilar(("Objeto 6", 3.10))
pilaOficina.apilar(("Objeto 7", 1.9))

print("Objetos desordenados")
print(pilaOficina)
print("Objetos ordenados")
print(ordenarPeso(pilaOficina))'''








#Ejercicio 18
'''class Pelicula(object):
	def __init__(self, titulo, estudio, anio):
		self.titulo = titulo
		self.estudio = estudio
		self.anio = anio

	def __str__(self):
		return "Titulo: " + self.titulo + "\n"\
		"Estudio: " + self.estudio + "\n"\
		"Anio: " + str(self.anio) + "\n"


def filtrarAnioEstreno(pila, anio):
	pilaAux = pilas.Pila()
	resultado = pilas.Pila()

	while pila.pilaVacia() == 0:
		pelicula = pila.desapilar()
		if pelicula.anio == anio:
			resultado.apilar(pelicula)
		pilaAux.apilar(pelicula)
		

	while pilaAux.pilaVacia() == 0:
		pila.apilar(pilaAux.desapilar())

	return resultado

def filtrarEstudio(pila, estudio):
	pilaAux = pilas.Pila()
	resultado = pilas.Pila()

	while pila.pilaVacia() == 0:
		pelicula = pila.desapilar()
		if pelicula.estudio == estudio:
			resultado.apilar(pelicula)
		pilaAux.apilar(pelicula)
		

	while pilaAux.pilaVacia() == 0:
		pila.apilar(pilaAux.desapilar())

	return resultado

pilaPeliculas = pilas.Pila()

while True:
	print("Agregar una pelicula:")
	titulo = input("Titulo: ")
	if titulo == '':
		break
	estudio = input("Estudio: ")
	anio = int(input("Anio: "))
	pilaPeliculas.apilar(Pelicula(titulo, estudio, anio))

print("Peliculas estrenadas en 2014:")
print(filtrarAnioEstreno(pilaPeliculas, 2014))
print("Cantidad de peliculas estrenadas en 2018:")
print(len(filtrarAnioEstreno(pilaPeliculas, 2018)))
print("Peliculas estrenadas en 2016 que pertenecen a Marvel Studios:")
print(filtrarEstudio(filtrarAnioEstreno(pilaPeliculas, 2016), "Marvel Studios"))
'''





#Ejercicio 19
'''
direcciones = ["N", "S", "E", "O", "NE", "SE", "NO", "SO"]
direccion = ""

def movInverso(direccion):
	if(direccion == "N"):
		return "S"
	elif(direccion == "NE"):
		return "SO"
	elif(direccion == "E"):
		return "O"
	elif(direccion == "SE"):
		return "NO"
	elif(direccion == "S"):
		return "N"
	elif(direccion == "SO"):
		return "NE"
	elif(direccion == "O"):
		return "E"
	else:
		return "SE"

movimientosRobot = pilas.Pila()
movimientosRobotInversos = pilas.Pila()

while 0 == 0:
	direccion = input("Ingresar una dirección: ")
	if(direccion == ""):
		break
	elif(Buscar(direcciones, direccion) == 1):
		movimientosRobot.apilar(direccion)
			
print("Movimientos del robot: " , movimientosRobot.pila)

while movimientosRobot.pilaVacia() == 0:
	direccion = movimientosRobot.desapilar()
	movimientosRobotInversos.apilar(movInverso(direccion))

print("Movimientos del robot para volver: ", movimientosRobotInversos.pila)'''




#Ejercicio 20
'''
def Fibonacci(sucesion, posicion):
	pAux = pilas.Pila()
	if posicion > 0: 
		if(posicion == 2):
			return sucesion
		if(posicion == 1):
			sucesion.desapilar()
			return sucesion
		if(posicion > 2):
			ultimo = sucesion.desapilar()
			penultimo = sucesion.desapilar()
			pAux.apilar(penultimo + ultimo)
			pAux.apilar(ultimo)
			pAux.apilar(penultimo)
			pAux.vaciarPila(sucesion)
			Fibonacci(sucesion, posicion - 1)




pFibonacci = pilas.Pila()
pFibonacci.apilarVector([1,0])

pos = input("Ingresar la posicion en la Serie de Fibonacci: ")

Fibonacci(pFibonacci, int(pos))

print(pFibonacci.pila)'''

'''def Ordenar(pila):
	pAux = pilas.Pila()

	while pila.pilaVacia() == 0:
		
		aux = pila.desapilar()	

		while pAux.pilaVacia() == 0 and pAux.pila[-1] < aux:

			pila.apilar(pAux)'''


#Ejercicio 21
'''pAux = pilas.Pila()
temperaturas = pilas.Pila()
temperaturas.llenarPila(11,29,31)

print("Temperaturas: ",temperaturas.pila)

OrdenarPila(temperaturas)

promedio = Promedio(temperaturas)

inferior = 0
superior = 0

while temperaturas.pilaVacia() == 0:
	num = temperaturas.desapilar()
	if num<promedio:
		inferior = inferior + 1
	else:
		superior = superior + 1

	pAux.apilar(num)

pAux.vaciarPila(temperaturas)

Max = temperaturas.pila[-1]
Min = temperaturas.pila[0]

rango = Max - Min

print("Temperatura máxima: ", Max)
print("Temperatura mínima: ", Min)
print("Promedio: ", promedio)
print("Cantidad de temperaturas inferiores al promedio: ", inferior)
print("Cantidad de temperaturas superiores al promedio: ", superior)'''







#22
'''class Personaje(object):
	def __init__(self, nombre, cantidad):
		self.nombre = nombre
		self.cantidad = cantidad

	def __str__(self):
		return "Nombre: " + self.nombre + "\n"\
		"Cantidad: " + str(self.cantidad) + "\n"

def ubicacionPersonaje(pila, nombre):
	pilaAux = pilas.Pila()
	pos = 0

	while pila.pilaVacia() == 0:
		if pila.cima().nombre == nombre:
			break
		else:
			pilaAux.apilar(pila.desapilar())
		pos += 1

	while pilaAux.pilaVacia() == 0:
		pila.apilar(pilaAux.desapilar())

	if pos == len(pila):
		return 0
	else:
		return pos +1

pilaPersonajes = pilas.Pila()

pilaPersonajes.apilar(Personaje("asd", 40))
pilaPersonajes.apilar(Personaje("Groot", 7))
pilaPersonajes.apilar(Personaje("Rocket Raccooon", 4))
pilaPersonajes.apilar(Personaje("Viuda Negra", 40))


#A
print(f"Posicion en la que se encuentra Rocket Raccoon: {ubicacionPersonaje(pilaPersonajes, 'Rocket Raccoon')}")
print(f"Posicion en la que se encuentra Rocket Raccoon: {ubicacionPersonaje(pilaPersonajes, 'Groot')}")

#B
pila = pilaPersonajes
pilaAux = pilas.Pila()

print("Personajes con mas de 5 apariciones: ")
while pila.pilaVacia() == 0:
	if pila.cima().cantidad > 5:
		print(pila.cima())
	pilaAux.apilar(pila.desapilar())

while pilaAux.pilaVacia() == 0:
	pila.apilar(pilaAux.desapilar())
#C
while pila.pilaVacia() == 0:
	if pila.cima().nombre == "Viuda Negra":
		print(f"La cantidad de peliculas en la que participo La viuda negra es: {pila.cima().cantidad}")
	pilaAux.apilar(pila.desapilar())

while pilaAux.pilaVacia() == 0:
	pila.apilar(pilaAux.desapilar())

#D
print("Personajes cuyos nombres comienzan con 'C', 'D', 'G'")
letras = ['C', 'D', 'G']
while pila.pilaVacia() == 0:
	if pila.cima().nombre[0] in letras:
		print(pila.cima())
	pilaAux.apilar(pila.desapilar())

while pilaAux.pilaVacia() == 0:
	pila.apilar(pilaAux.desapilar())'''