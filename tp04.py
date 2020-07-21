import tda_lista as li
import tda_lista_doble as ld
import tda_lista_lista as ll
import random
from datetime import date, datetime, timedelta, time

oListaAleatoria = li.Lista()
for i in range(30):
	li.insertar(oListaAleatoria, random.randint(0,50))

oListaAleatoria2 = li.Lista()
for i in range(30):
	li.insertar(oListaAleatoria2, random.randint(0,50))




#Ejercicio 1
'''def tamanioLista(oLista):
	actual = oLista.inicio
	tamanio = 0

	while actual is not None:
		actual = actual.sig
		tamanio += 1
	return tamanio

print(tamanioLista(oListaAleatoria))'''

#Ejercicio 2
'''vocales = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
oLista = li.Lista()


for i in range(30):
	li.insertar(oLista, chr(random.randint(65,122)))

print('Con vocales: ')
li.barrido(oLista)

for i in vocales:
	while li.busqueda(oLista, i) != None:
		li.eliminar(oLista, i)

print('Sin vocales')
li.barrido(oLista)'''





#Ejercicio 3
def eliminarPrimero(oLista):
	if oLista.inicio is not None:
		num = oLista.inicio.info
		oLista.inicio = oLista.inicio.sig
		oLista.tamanio -= 1
		return num
	else:
		return None
'''
oListaPar = li.Lista()
oListaImpar = li.Lista()

while oListaAleatoria.inicio is not None:
	num = eliminarPrimero(oListaAleatoria)
	if num % 2 == 0:
		li.insertar(oListaPar,num)
	else:
		li.insertar(oListaImpar, num)

print("Numeros Pares: ")
li.barrido(oListaPar)
print("Numeros Impares: ")
li.barrido(oListaImpar)'''




#Ejercicio 4
def insertarNodoPos(oLista, pos, nodo):
	if pos == 1:
		nodo.sig = oLista.inicio
		oLista.inicio = nodo
	elif oLista.inicio is not None:
		actual = oLista.inicio
		anterior = None

		for i in range(pos - 1):
			anterior = actual
			actual = actual.sig

		anterior.sig = nodo
		nodo.sig = actual

'''li.barrido(oListaAleatoria)

pos = int(input('Ingresar la posicion para insertar un nodo: '))

nodo = li.nodoLista()
nodo.info = (input('ingresar un dato: '))

insertarNodoPos(oListaAleatoria, pos, nodo)

li.barrido(oListaAleatoria)'''







#Ejercicio 5
def primo(num):
	for i in range(2,num):
		if num%i == 0:
			return False
	return True

'''print('Con numeros primos')
li.barrido(oListaAleatoria)

oLista = li.Lista()

while oListaAleatoria.inicio is not None:
	num = eliminarPrimero(oListaAleatoria)
	if not primo(num):
		li.insertar(oLista, num)

while oLista.inicio is not None:
	li.insertar(oListaAleatoria, eliminarPrimero(oLista))

print('Sin numeros primos')
li.barrido(oListaAleatoria)'''





#Ejercicio 6
class Superheroe(object):
	def __init__(self, nombre, anioAparicion, casa, biografia):
		self.nombre = nombre
		self.anioAparicion = anioAparicion
		self.casa = casa
		self.biografia = biografia

	def __str__(self):
		cadena = 	"Nombre: " + self.nombre + "\n"\
					"Año de aparicion: " + str(self.anioAparicion) + "\n"\
					"Casa: " + self.casa + "\n"\
					"Biografia: " + self.biografia + "\n"\
					""
		return cadena

oSuperheroe1 = Superheroe('Linterna Verde', 1940, 'DC', 'Linterna Verde (en inglés: Green Lantern) es el alias de varios superhéroes de la ficción del Universo DC, los cuales se caracterizan por un anillo de poder y la capacidad de crear manifestaciones de luz sólida con los susodichos anillos.')
oSuperheroe2 = Superheroe('Wolverine', 1974, 'Marvel', 'Wolverine, cuyo nombre de nacimiento es James Howlett (también conocido como James Logan o simplemente Logan es un superhéroe que aparece en los cómics estadounidenses publicado por Marvel Comics, principalmente en asociación con los X-Men.')
oSuperheroe3 = Superheroe('Doctor Strange', 1963, 'DC', 'La historia de origen del personaje relata que una vez fue un cirujano brillante pero egoísta. Después de que un accidente automovilístico dañara gravemente sus manos y obstaculiza su capacidad para realizar una cirugía, busca una forma de repararlas encontrándose con el Anciano. Después de convertirse en uno de los alumnos del Hechicero Supremo, se convierte en un practicante tanto de las artes místicas como de las artes marciales. Además de conocer muchos hechizos poderosos, tiene un traje con dos objetos místicos: la Capa de Levitación y el Ojo de Agamotto, que le otorgan poderes adicionales. Strange es ayudado en el camino por su amigo y sirviente, Wong, y una gran variedad de objetos místicos. Toma residencia en una mansión llamada Sanctum Sanctorum, ubicado en la ciudad de Nueva York. Más tarde, Strange toma el título de Hechicero Supremo.')
oSuperheroe4 = Superheroe('Capitana Marvel', 1970, 'Marvel', 'Carol Susan Jane Danvers es una superheroína ficticia que aparece en cómics estadounidenses publicados por Marvel Comics. Fue creada por el escritor Roy Thomas y el artista Gene Colan, Danvers apareció por primera vez como oficial de la Fuerza Aérea de los Estados Unidos y colega del superhéroe Kree, Mar-Vell en Marvel Super-Heroes # 13 (marzo de 1968). Danvers más tarde se convirtió en la primera encarnación de Ms. Marvel en Ms. Marvel #1 (enero de 1977) después de que su ADN se fusionara con el de Mar-Vell durante una explosión, otorgándole poderes sobrehumanos. Debutando en la Edad de Plata de los Cómics, el personaje apareció en una serie homónima en la década de 1970 antes de ser asociada con los equipos de superhéroes de Los Vengadores y los X-Men. El personaje también ha sido conocido como Binaria, Warbird, y Capitana Marvel en varios puntos de su historia.')
oSuperheroe5 = Superheroe('Mujer Maravilla', 1941, 'DC', 'La Mujer Maravilla (en inglés: Wonder Woman) es una superheroína ficticia creada por William Moulton Marston para la editorial DC Comics. Es una princesa guerrera de las Amazonas, pueblo ficticio basado en el de las amazonas de la mitología griega. En su tierra natal es conocida como la princesa Diana de Temiscira pero fuera de esta utiliza laa identidad secreta de Diana Prince. Está dotada de una amplia gama de poderes superhumanos y habilidades de combate de batalla superiores, gracias a sus dones obtenidos de los dioses y su amplio entrenamiento. Ella posee un gran arsenal de armas, incluyendo entre las principales el Lazo de la Verdad, un par de brazaletes mágicos indestructibles, su tiara, que sirve como arma, y en algunos relatos, en la edad de oro, tuvo un avión invisible. Pero más adelante, se le fue mostrando con la capacidad de volar cada vez con mayor frecuencia por lo que el avión invisible fue dejando de utilizarse.')
oSuperheroe6 = Superheroe('Flash', 1940, 'Marvel', 'Flash (conocido también como The Flash) es el nombre de varios superhéroes ficticios que aparecen en los cómics estadounidenses publicados por DC Comics. Creado por el escritor Gardner Fox y el artista Harry Lampert, el "Flash" original apareció por primera vez en Flash Comics #1 (fecha de portada de enero de 1940 / mes de noviembre de 1939)). Apodado el "Corredor Escarlata", todas las encarnaciones del Flash poseen "súper velocidad", que incluye la capacidad de correr, moverse y pensar extremadamente rápido, también puede atravesar la materia sólida, usar reflejos sobrehumanos y aparentemente violar ciertas leyes de la física, como superar la velocidad de la luz.')
oSuperheroe7 = Superheroe('Star-Lord', 1976, 'Marvel', 'Star-Lord (Peter Jason Quill) es un personaje ficticio que aparece en los cómics estadounidenses publicados por Marvel Comics. El personaje, creado por Steve Englehart y Steve Gan, apareció por primera vez en Marvel Preview #4 (enero de 1976). Es hijo de la humana Meredith Quill y del Spartoi Json, Peter Quill asume el manto de Star-Lord, un policía interplanetario.')
oSuperheroe8 = Superheroe('Spider-Man', 1962, 'Marvel', 'Spider-Man (llamado Hombre Arana en muchas de las traducciones al español) es un superhéroe ficticio creado por los escritores y editores Stan Lee y Steve Ditko. Apareció por primera vez en el cómic de antología Amazing Fantasy # 15 (10 de agosto de 1962), en la Edad de Plata de los cómics. Aparece en los cómics estadounidenses publicados por Marvel Comics, así como en varias películas, programas de televisión y adaptaciones de videojuegos ambientadas en el Universo Marvel. En las historias, Spider-Man es el alias de Peter Parker, un huérfano criado por su tía May y su tío Ben en la Ciudad de Nueva York después de que sus padres Richard y Mary Parker murieron en un accidente aéreo. Lee y Ditko tuvieron que lidiar con los problemas de la adolescencia y los problemas financieros, y lo acompañaron con muchos personajes de apoyo, como J. Jonah Jameson, Flash Thompson, Harry Osborn, los intereses románticos, Gwen Stacy y Mary Jane Watson, y enemigos como el Doctor Octopus, Kingpin, Duende Verde y Venom. Su historia de origen lo tiene adquiriendo habilidades relacionadas con la araña después de un mordisco de una araña radioactiva; estos incluyen aferrarse a las superficies, disparar telarañas desde dispositivos montados en la muñeca y detectar el peligro con su "sentido arácnido".')
oSuperheroe9 = Superheroe('Aquaman', 1941, 'DC', 'Aquaman (Arthur Curry) es un superhéroe que aparece en los cómics estadounidenses publicados por DC Comics. Creado por el artista Paul Norris y el escritor Mort Weisinger, el personaje debutó en More Fun Comics # 73 (noviembre de 1941). Inicialmente, una característica de respaldo en los títulos de antología de DC, Aquaman más tarde protagonizó varios volúmenes de una serie de cómics en solitario. Durante los últimos años de la década de 1950 y 1960, el período de recuperación de superhéroes conocido como la Edad de Plata, fue miembro fundador de la Liga de la Justicia. En la Edad Moderna de la década de 1990, los escritores interpretaron el personaje de Aquaman más seriamente, con historias que representan el peso de su papel como rey de la Atlántida.')

superheroes = [oSuperheroe1, oSuperheroe2, oSuperheroe3, oSuperheroe4 ,oSuperheroe5, oSuperheroe6, oSuperheroe7, oSuperheroe8, oSuperheroe9]

listaSuperheroes = li.Lista()

for superheroe in superheroes:
	li.insertar(listaSuperheroes, superheroe, 'anioAparicion')


#A
#Eliminar Linterna verde
#li.eliminar(listaSuperheroes, 'Linterna Verde', 'nombre')

#B
#resultado = li.busqueda(listaSuperheroes, 'Wolverine', 'nombre')
#print(f'El anio en que wolverine apareció fue: {resultado.anioAparicion}')

#C
#resultado = li.eliminar(listaSuperheroes, 'Doctor Strange', 'nombre').info
#print(f'Nombre: {resultado.nombre}, Casa: {resultado.casa}')
#resultado.casa = 'Marvel'

#li.insertar(listaSuperheroes, resultado, 'anioAparicion')

#resultado = li.busqueda(listaSuperheroes, 'Doctor Strange', 'nombre')
#print(f'Nombre: {resultado.info.nombre}, Casa: {resultado.info.casa}')


#D
#listaAux = li.Lista()

#while listaSuperheroes.inicio is not None:
#	superheroe = eliminarPrimero(listaSuperheroes)
#	li.insertar(listaAux,superheroe, 'nombre')
#	if 'traje' in superheroe.biografia or 'armadura' in superheroe.biografia:
#		print(f"El superheroe '{superheroe.nombre}' contiene en su biografia la palabra 'armadura' o 'traje'")

#while listaAux.inicio is not None:
#	li.insertar(listaSuperheroes, eliminarPrimero(listaAux), 'anioAparicion')

#E
'''def anterioresA1963(lista):
	actual = lista.inicio
	while actual is not None:
		superheroe = actual.info

		if superheroe.anioAparicion < 1963:
			print(f"Nombre: {superheroe.nombre} \nCasa: {superheroe.casa}")

		actual = actual.sig

anterioresA1963(listaSuperheroes)
'''

#F
'''resultado = li.busqueda(listaSuperheroes, 'Capitana Marvel', 'nombre')
print(f"Nombre: {resultado.info.nombre} \nCasa: {resultado.info.casa}\n ")
resultado = li.busqueda(listaSuperheroes, 'Mujer Maravilla', 'nombre')
print(f"Nombre: {resultado.info.nombre} \nCasa: {resultado.info.casa}\n ")'''

#G
#resultado = li.busqueda(listaSuperheroes, 'Flash', 'nombre')
#print(resultado.info)
#resultado = li.busqueda(listaSuperheroes, 'Star-Lord', 'nombre')
#print(resultado.info)

#H
'''def inicialNombre(lista, letras):
	actual = lista.inicio
	listaAux = li.Lista()

	for letra in letras:
		while actual is not None:
			if actual.info.nombre[0] == letra:
				li.insertar(listaAux, actual.info, "nombre")

			actual = actual.sig
		actual = lista.inicio

	return listaAux


letras = ["B", "M", "S"]

resultado = inicialNombre(listaSuperheroes, letras)

li.barrido(resultado)'''

#I
'''def casaSuperheroe(lista):
	actual = lista.inicio
	contador_DC = 0
	contador_marvel = 0

	while actual is not None:
		if actual.info.casa == "DC":
			contador_DC += 1
		else:
			contador_marvel += 1
		actual = actual.sig

	print(f"Cantidad de supeheroes de DC: {contador_DC} \nCantidad de supeheroes de Marvel: {contador_marvel}")

casaSuperheroe(listaSuperheroes)'''





#7
#A
def concatenarListas(lista1, lista2):
	listaAux = li.Lista()
	listaAux = lista1
	actual = listaAux.inicio

	while actual.sig is not None:
		actual = actual.sig

	actual.sig = lista2.inicio

	return listaAux


'''
lista1 = oListaAleatoria
lista2 = listaSuperheroes

resultado = concatenarListas(lista1, lista2)

li.barrido(resultado)'''

#B
def interseccion(lista1, lista2):
	pLista1 = lista1.inicio
	pLista2 = lista2.inicio
	contador = 0

	while pLista1 is not None:
		while pLista2 is not None:
			if pLista1.info == pLista2.info:
				contador += 1

			pLista2 = pLista2.sig

		pLista2 = lista2.inicio
		pLista1 = pLista1.sig

	return contador

#print(f"La cantidad de elementos repetidos es: {interseccion(oListaAleatoria, oListaAleatoria2)}")

#B
'''def concatenarOrdenado(lista1, lista2, criterio = None):
	listaAux = li.Lista()
	actual = lista1.inicio
	
	while actual.sig is not None:
		if li.busqueda(listaAux, actual.info, criterio) is None:
			li.insertar(listaAux, actual.info, criterio)

		actual = actual.sig

	if li.busqueda(listaAux, actual.info, criterio) is None:
		li.insertar(listaAux, actual.info, criterio)

	actual.sig = lista2.inicio

	while actual.sig is not None:
		if li.busqueda(listaAux, actual.info, criterio) is None:
			li.insertar(listaAux, actual.info, criterio)

		actual = actual.sig

	if li.busqueda(listaAux, actual.info, criterio) is None:
		li.insertar(listaAux, actual.info, criterio)	

	return listaAux

li.barrido(concatenarOrdenado(oListaAleatoria, oListaAleatoria2))'''


#D
'''while oListaAleatoria.inicio is not None:
	print(eliminarPrimero(oListaAleatoria))'''


#8
'''
def palindromoLista(lista):
	palabra = ""
	palabraAlReves = ""

	actual = lista.inicio
	while actual is not None:
		palabra += actual.info
		actual = actual.sig

	actual = lista.fin
	while actual is not None:
		palabraAlReves += actual.info
		actual = actual.ant

	if palabra == palabraAlReves:
		return True
	else:
		return False


lista = ld.ListaDoble()
letra = 'a'
while letra != '':
	letra = input("Ingresar una letra: ")
	ld.insertarAlFinal(lista, letra)

if palindromoLista(lista):
	print("La palabra es un palindromo: ")
else:
	print("La palabra no es un palindromo: ")
'''








#9
'''
class Alumno(object):
	def __init__(self, nombre, apellido, legajo):
		self.nombre = nombre
		self.apellido = apellido
		self.legajo = legajo

	def __str__(self):
		return 	"\n" + "Nombre: " + self.nombre + "\n"\
				"Apellido: " + self.apellido + "\n"\
				"Legajo: " + str(self.legajo) 

class Parcial(object):
	def __init__(self, materia, nota, fecha):
		self.materia = materia
		self.nota = nota
		self.fecha = fecha

	def __str__(self):
		return 	"\n" + "Materia: " + self.materia + "\n"\
				"Nota: " + str(self.nota) + "\n"\
				"Fecha: " + self.fecha		

alumno1 = Alumno('Gabriel', 'Ramos', 1551512341)
alumno2 = Alumno('Walter', 'Bel', 12215874555)

lista = ll.Lista()

ll.insertar(lista, alumno1, 'nombre')
ll.insertar(lista, alumno2, 'nombre')
'''

def ordenarPor(lista, campo):
	actual= lista.inicio
	listaAux = ll.Lista()

	while actual is not None:
		ll.insertar(listaAux, actual.info, campo)	
		actual = actual.sig

	return listaAux
'''
while True:
	nombre = input("Insertar nombre del alumno: ")
	if nombre == "":
		break
	apellido = input("Insertar apellido: ")
	legajo = int(input("Insertar numero de legajo: "))
	ll.insertar(lista, Alumno(nombre, apellido, legajo), 'nombre')

actual = lista.inicio
while actual is not None:
	while True:
		print(f"Agregar parcial para {actual.info.nombre} {actual.info.apellido}")
		materia = input("Ingresar la materia: ")
		if materia == '':
			break
		nota = float(input("Ingresar la nota: "))
		fecha = input("Ingresar la fecha: ")
		ll.insertar(actual.sublista, Parcial(materia, nota, fecha), 'fecha')

	actual = actual.sig

alumno = lista.inicio
'''
#A
#ll.barrido(ordenarPor(lista, 'apellido'))

#B
'''print("Los alumnos que no desaprobaron ningun parcial son: ")
while alumno is not None:
	parcial = alumno.sublista.inicio
	while parcial is not None:
		if parcial.info.nota < 4:
			break
		parcial = parcial.sig
	if parcial is None:
		print(f"{alumno.info.apellido} {alumno.info.nombre}")

	alumno = alumno.sig
'''

#C
'''print("Los alumnos con promedio mayor a 8.89 son: ")
while alumno is not None:
	parcial = alumno.sublista.inicio
	promedio = 0
	while parcial is not None:
		promedio += parcial.info.nota / alumno.sublista.tamanio 
		parcial = parcial.sig
	if promedio > 8.89 and promedio != 0:
		print(f"{alumno.info.apellido} {alumno.info.nombre}")

	alumno = alumno.sig
'''

#D
'''print("Los alumnos cuyos apellidos comienzan co la letra 'L' son: ")
while alumno is not None:
	if alumno.info.apellido[0] == 'L':
		print(alumno.info)

	alumno = alumno.sig'''

#E
'''while alumno is not None:
	parcial = alumno.sublista.inicio
	promedio = 0
	while parcial is not None:
		promedio += parcial.info.nota / alumno.sublista.tamanio 
		parcial = parcial.sig
	print(alumno.info)
	print("Promedio: " + str(promedio))

	alumno = alumno.sig
'''








#10

class Cancion(object):
	def __init__(self, nombre, artista, duracion, reproducciones):
		self.nombre = nombre
		self.artista = artista
		self.duracion = duracion
		self.reproducciones = reproducciones

	def __str__(self):
		cadena = 	"Nombre: " + self.nombre + "\n"\
					"Artista: " + self.artista + "\n"\
					"Duracion: " + self.duracion + "\n"\
					"Reproducciones: " + str(self.reproducciones) + "\n"

		return cadena

canciones = [
	Cancion('Knee Socks', 'Artic Monkeys', '4:17', 136971594), 
	Cancion('Poles Apart', 'Pink Floyd', '7:03', 15736752),
	Cancion('Song 2', 'Blur', '2:01', 343102347)
]

playlist = ld.ListaDoble()

for cancion in canciones:
	ld.insertar(playlist, cancion, 'reproducciones')
#A
def dobleOrdenarPor(lista, campo):
	actual= lista.inicio
	listaAux = ld.ListaDoble()

	while actual is not None:
		ld.insertar(listaAux, actual.info, campo)	
		actual = actual.sig

	return listaAux

'''print("Cancion mas larga: ")
print(dobleOrdenarPor(playlist, 'duracion').fin.info)'''


#B
'''
top = dobleOrdenarPor(playlist, 'reproducciones')

print("TOP 5 CANCIONES MAS ESCUCHADAS")

actual = top.fin
for i in range(5):
	print("PUESTO N° " + str(i + 1))
	print(actual.info)
	actual = actual.ant

print("TOP 10 CANCIONES MAS ESCUCHADAS")

actual = top.fin
for i in range(10):
	print("PUESTO N° " + str(i + 1))
	print(actual.info)
	actual = actual.ant

print("TOP 40 CANCIONES MAS ESCUCHADAS")

actual = top.fin
for i in range(40):
	print("PUESTO N° " + str(i + 1))
	print(actual.info)
	actual = actual.ant
'''

#C
cancion = playlist.inicio
'''playlistAux = ld.ListaDoble()
while cancion is not None:
	if cancion.info.artista == 'Artic Monkeys':
		ld.insertar(playlistAux, cancion.info, 'nombre')
	cancion = cancion.sig

print('Canciones de Artic Monkeys')
ld.barrido(playlistAux)
'''

#D
'''dobleOrdenarPor(playlist, 'artista')

print('Nombre de las bandas que solo son de una palabra')
while cancion is not None:
	if cancion.ant is None:
		if not ' ' in cancion.info.artista:
			print(cancion.info.artista)
	elif cancion.ant.info.artista != cancion.info.artista:
		if not ' ' in cancion.info.artista:
			print(cancion.info.artista)

	cancion = cancion.sig
'''


#11






#12
#A li.barrido(oListaAleatoria)
def eliminarAnteultimoSimple(lista):
	actual = lista.inicio

	if lista.tamanio >= 2:
		if lista.tamanio == 2:
			lista.inicio = lista.inicio.sig
		else:
			while actual.sig.sig.sig is not None:
				actual = actual.sig
			
			actual.sig = actual.sig.sig

def eliminarAnteultimoDoble(lista):
	if lista.tamanio >= 2:
		if lista.tamanio == 2:
			lista.fin.ant = None
			lista.inicio = lista.fin
		else:
			lista.fin.ant = lista.fin.ant.ant
			lista.fin.ant.sig = lista.fin



'''li.barrido(oListaAleatoria)
print('Lista sin elemento')
eliminarAnteultimoSimple(oListaAleatoria)
li.barrido(oListaAleatoria)
'''
listaAleatoriaD = ld.ListaDoble()
for i in range(10):
	ld.insertar(listaAleatoriaD, random.randint(0,50))

'''ld.barrido(listaAleatoriaD);
eliminarAnteultimoDoble(listaAleatoriaD)
print('')
ld.barrido(listaAleatoriaD)'''










#13
def barridoAsc(lista):
	actual = lista.inicio

	while actual is not None:
		print(actual.info)
		actual = actual.sig

def barridoDesc(lista):
	actual = lista.fin

	while actual is not None:
		print(actual.info)
		actual = actual.ant

'''print("Ascendente")
barridoAsc(listaAleatoriaD)
print("Descendente")
barridoDesc(listaAleatoriaD)
'''








#15
class Entrenador(object):
	def __init__(self, nombre, torneosGanados, batallasPerdidas, batallasGanadas):
		self.nombre = nombre
		self.torneosGanados = torneosGanados
		self.batallasGanadas = batallasGanadas
		self.batallasPerdidas = batallasPerdidas

	def __str__(self):
		return "\nNombre: " + self.nombre + "\n"\
				"Torneos Ganados: " + str(self.torneosGanados) + "\n"\
				"Batallas Perdidas: " + str(self.batallasPerdidas) + "\n"\
				"Batallas Ganadas: " + str(self.batallasGanadas) + "\n"

class Pokemon(object):
	def __init__(self, nombre, nivel, tipo, subtipo):
		self.nombre = nombre
		self.nivel = nivel
		self.tipo = tipo
		self.subtipo = subtipo

	def __str__(self):
		return "\nNombre: " + self.nombre + "\n"\
				"Nivel: " + str(self.nivel) + "\n"\
				"Tipo: " + self.tipo + "\n"\
				"Subtipo: " + self.subtipo + "\n"


'''while True:
	print("\nIngresar entrenador")
	nombre = input("Nombre: ")
	if nombre == '':
		break
	tganados = int(input("Torneos Ganados: "))
	bperdidas = int(input("Batallas Perdidas: "))
	bganadas = int(input("Batallas Ganadas: "))

	ll.insertar(listaEntrenadores, Entrenador(nombre, tganados, bperdidas, bganadas))

entrenador = listaEntrenadores.inicio

while entrenador is not None:
	while True:
		print(f"\n Ingresar pokemon para {entrenador.info.nombre}")
		nombre = input("Nombre: ")
		if nombre == '':
			break

		nivel = int(input("Nivel: "))
		tipo = input("Tipo: ")
		sub = input("Subtipo: ")

		ll.insertar(entrenador.sublista, Pokemon(nombre, nivel, tipo, sub), 'nombre')

	entrenador = entrenador.sig
'''
#A
'''entrenador = listaEntrenadores.inicio
print("Cantidad de Pokemons")
while entrenador is not None:
	print(f"{entrenador.info.nombre}: {entrenador.sublista.tamanio}")
	entrenador = entrenador.sig'''

#B
'''listaAux = ll.Lista()

entrenador = listaEntrenadores.inicio
while entrenador is not None:
	if entrenador.info.torneosGanados > 3:
		ll.insertar(listaAux, entrenador.info, 'nombre')
	entrenador = entrenador.sig
'''
#C
#Ordenar los entrenadores de forma ascendente por torneos ganados y recorrer la lista hasta encontrar el que gano mas torneos
'''resultado = ordenarPor(listaEntrenadores, 'torneosGanados')

entrenador = resultado.inicio

while entrenador.sig is not None:
	entrenador = entrenador.sig

entrenador = ll.busqueda(listaEntrenadores,entrenador.info.nombre, 'nombre')

resultado = ordenarPor(entrenador.sublista, 'nivel')

pokemon = resultado.inicio

while pokemon.sig is not None:
	pokemon = pokemon.sig

print(entrenador.info)
print(pokemon.info)'''

#D
'''nombre = input("Ingresar nombre del entrenador: ")

resultado = ll.busqueda(listaEntrenadores, nombre, 'nombre')

print(resultado.info)

pokemon = resultado.sublista.inicio

while pokemon is not None:
	print(pokemon.info)
	pokemon = pokemon.sig
'''

#E
'''
entrenador = listaEntrenadores.inicio
while entrenador is not None:
	bg = entrenador.info.batallasGanadas
	bp = entrenador.info.batallasPerdidas
	if bg + bp != 0:
		porcentaje = bg/(bg + bp)*100
		if porcentaje > 79:
			print(entrenador.info)
			print(f"Porcentaje de batallas ganadas = {porcentaje}%")
	entrenador = entrenador.sig
'''

#F
'''entrenador = listaEntrenadores.inicio

while entrenador is not None:
	pokemon = entrenador.sublista.inicio
	while pokemon is not None:
		if (pokemon.info.tipo == 'fuego' and pokemon.info.subtipo == 'planta') or (pokemon.info.tipo == 'agua' and pokemon.info.subtipo == 'volador'):
			print(entrenador.info)
			break
		pokemon = pokemon.sig

	entrenador = entrenador.sig'''

#G
'''
entrenador = input("Ingresar el nombre de un entrenador para calcular el promedio de nivel de sus pokemons: ")

entrenador = ll.busqueda(listaEntrenadores, entrenador, 'nombre')

pokemon = entrenador.sublista.inicio

promedio = 0
while pokemon is not None:
	promedio += (pokemon.info.nivel / entrenador.sublista.tamanio)
	pokemon = pokemon.sig

print(f"El promedio de los pokemons de {entrenador.info.nombre} es {promedio}")
'''

#H
'''pokemon = input("Ingresar el nombre de un pokemon: ")

entrenador = listaEntrenadores.inicio

contador = 0

while entrenador is not None:
	if ll.busqueda(entrenador.sublista, pokemon, 'nombre') is not None:
		contador += 1
	entrenador = entrenador.sig

print(f"La cantidad de entrenadores que tienen al pokemon '{pokemon}' son {contador}")

'''

#I
'''entrenador = listaEntrenadores.inicio

print("Entrenadores que tienen algun pokemon repetido:")
while entrenador is not None:
	listaAux = ll.Lista()
	pokemon = entrenador.sublista.inicio
	while pokemon is not None:
		if ll.busqueda(listaAux, pokemon.info.nombre, 'nombre') == None:
			ll.insertar(listaAux, pokemon.info.nombre, 'nombre')
		else:
			print(f"El entrenador {entrenador.info.nombre} tiene repetido al pokemon {pokemon.info.nombre}")
			break
		pokemon = pokemon.sig
	entrenador = entrenador.sig
'''

#J
'''pokemons = ['Tyrantrum', 'Terrakion', 'Wingull']

entrenador = listaEntrenadores.inicio

while entrenador is not None:
	for pokemon in pokemons:
		if ll.busqueda(entrenador.sublista, pokemon, 'nombre'):
			print(f"El entrenador {entrenador.info.nombre} tiene al pokemon {pokemon}")
			break
	entrenador = entrenador.sig
'''

#K
'''
iEntrenador = input("Ingresar el nombre del entrenador: ")

entrenador = ll.busqueda(listaEntrenadores, iEntrenador, 'nombre')

iPokemon = input("Ingresar el nombre de un pokemon: ")

resultado = ll.busqueda(entrenador.sublista, iPokemon, 'nombre')

if resultado != None:
	print(entrenador.info)
	print(resultado.info)
else:
	print(f"El entrenador {iEntrenador} tiene al pokemon {iPokemon}")
'''









#16
class Actividad(object):
	def __init__(self, costo, tiempoEjecucion, fechaInicio, fechaFinEstimada, fechaFinEfectiva, persona):
		self.costo = costo
		self.tiempoEjecucion = datetime.strptime(tiempoEjecucion, "%H:%M:%S")
		self.fechaInicio = datetime.strptime(fechaInicio, "%d-%m-%Y")
		self.fechaFinEstimada = datetime.strptime(fechaFinEstimada, "%d-%m-%Y")
		self.fechaFinEfectiva = datetime.strptime(fechaFinEfectiva, "%d-%m-%Y")
		self.persona = persona

	def __str__(self):
		return "\n" + "Costo: " + str(self.costo) + "\n"\
				"Tiempo ejecucion: " + self.tiempoEjecucion.strftime("%H:%M:%S") + "\n"\
				"Fecha inicio: " + self.fechaInicio.strftime("%d-%m-%Y") + "\n"\
				"Fecha de fin estimada: " + self.fechaFinEstimada.strftime("%d-%m-%Y") + "\n"\
				"Fecha de fin efectiva: " + self.fechaFinEfectiva.strftime("%d-%m-%Y") + "\n"\
				"Persona: " + self.persona

def tiempo_a_segundos(tiempo):
	resultado = (tiempo.hour * 3600) + (tiempo.minute * 60) + (tiempo.second)
	return resultado

def seg_a_tiempo(seg):
	resultado = datetime.strptime(str(seg//3600)+":"+str((seg%3600)//60)+":"+str(((seg%3600)%60)), "%H:%M:%S")
	return resultado 

proyecto = [
	Actividad(150.5, "02:20:40", "01-01-2020", "14-02-2020", "01-01-0001", "Ramos Gabriel" ),
	Actividad(170.25, "09:32:05", "10-01-2020", "15-01-2020", "14-01-2020", "Ramos Gabriel"),
	Actividad(130.75, "04:05:20", "16-02-2020", "18-03-2020", "19-04-2020", "Ramos Gabriel") 
]

listaProyecto = li.Lista()

for actividad in proyecto:
	li.insertar(listaProyecto, actividad, 'fechaFinEstimada')

'''actividad = listaProyecto.inicio

#A y #B
tiempo_promedio = 0
costo = 0

print("C")
persona = input("Ingresar el nombre de una persona: ")
print(f"Actividades en la que esta {persona}")
while actividad is not None:
	tiempo_promedio += tiempo_a_segundos(actividad.info.tiempoEjecucion) / listaProyecto.tamanio
	costo += actividad.info.costo
	if actividad.info.persona == persona:
		print(actividad.info)

	actividad = actividad.sig

print("A y B")
print(f"El costo total del proyecto es: ${costo}")
print(f"El promedio de tiempo de las actividades es: {seg_a_tiempo(round(tiempo_promedio)).strftime('%H:%M:%S')}")
'''

#D
'''print("Ingresar el rango de fechas")
fechaA = datetime.strptime(input("Ingresar una fecha en formato dd-mm-yyyy: "),"%d-%m-%Y")
fechaB = datetime.strptime(input("Ingresar una fecha en formato dd-mm-yyyy: "),"%d-%m-%Y")

actividad = listaProyecto.inicio

while actividad is not None:
	if (actividad.info.fechaFinEstimada > fechaA) and (actividad.info.fechaInicio < fechaB):
		print(actividad.info)
	actividad = actividad.sig'''

#E y F
'''
actividad = listaProyecto.inicio
tareasATiempo = li.Lista()
tareasFuera = li.Lista()
tareasPendientes = li.Lista()

persona = input("Ingresar el nombre de una persona: ")

while actividad is not None:
	if (actividad.info.fechaFinEfectiva != datetime.strptime("01-01-0001", "%d-%m-%Y")):
		if (actividad.info.fechaFinEstimada < actividad.info.fechaFinEfectiva):
			li.insertar(tareasFuera,actividad.info,'fechaInicio')
		else:
			li.insertar(tareasATiempo, actividad.info, 'fechaInicio')
	else:
		if persona == actividad.info.persona:
			li.insertar(tareasPendientes, actividad.info, 'fechaInicio')

	actividad = actividad.sig

print("\nActividades terminadas a tiempo: ")
li.barrido(tareasATiempo)
print("\nActividades terminadas fuera de tiempo: ")
li.barrido(tareasFuera)
print(f"\nActividades pendientes de {persona}: ")
li.barrido(tareasPendientes)'''


#17
class Vuelo(object):
	def __init__(self, empresa, numeroVuelo, asientos, fechaSalida, destino, km, asientos_primera, asientos_turista, 
		asientos_primera_ocupados, asientos_turista_ocupados):

		self.empresa = empresa
		self.numeroVuelo = numeroVuelo
		self.asientos = asientos
		self.fechaSalida = datetime.strptime(fechaSalida,"%d-%m-%Y")
		self.destino = destino
		self.km = km
		self.asientos_primera = asientos_primera
		self.asientos_turista = asientos_turista
		self.asientos_turista_ocupados = asientos_turista_ocupados
		self.asientos_primera_ocupados = asientos_primera_ocupados

	def __str__(self):
		return "\n" + "Empresa: " + self.empresa + "\n"\
				"Numero de vuelo: " + str(self.numeroVuelo) + "\n"\
				"Asientos del avion: " + str(self.asientos) + "\n"\
				"Fecha de salida: " + self.fechaSalida.strftime("%d-%m-%Y") + "\n"\
				"Destino: : " + self.destino + "\n"\
				"Kilometros de vuelo: " + str(self.km) + "\n"\
				"Asientos de primera clase totales: " + str(self.asientos_primera) + "\n"\
				"Asientos de clase turista totales: " + str(self.asientos_turista) + "\n"\
				"Asientos de primera clase ocupados: " + str(self.asientos_primera_ocupados) + "\n"\
				"Asientos de clase turista ocupados: " + str(self.asientos_turista_ocupados)


vuelos = [
	Vuelo("Latam", 550, 120, "12-01-2020", "Atenas", 4320, 30, 90, 18,61),
	Vuelo("American Airline", 590, 120, "12-02-2020", "Rio de Janeiro", 920, 30, 90, 18,90),
	Vuelo("Aerolineas Argentinas", 650, 120, "05-12-2020", "Madrid", 5120, 30, 90, 30,61)
]

listaVuelos = li.Lista()

def asientos_disponibles(vuelo, clase):
	if clase == 'turista':
		if vuelo.asientos_turista - vuelo.asientos_turista_ocupados > 0:
			return True
		else:
			return False
	elif(clase == 'primera'):
		if vuelo.asientos_primera - vuelo.asientos_primera_ocupados > 0:
			return True
		else:
			return False 
	else:
		print("La clase ingresada no es correcta.")

def vender_boleto(listaVuelos, nroVuelo, clase):
	vuelo = li.busqueda(listaVuelos,nroVuelo,'numeroVuelo')
	if vuelo is not None:
		if clase == 'turista':
			if asientos_disponibles(vuelo.info, 'turista'):
				vuelo.info.asientos_turista_ocupados += 1
				print(f"Pasaje vendido: asientos disponibles en clase turista {vuelo.info.asientos_turista - vuelo.info.asientos_turista_ocupados} ")
			else:
				print("No hay asientos disponibles en esta clase")
		elif clase == 'primera':
			if asientos_disponibles(vuelo.info, 'primera'):
				vuelo.info.asientos_primera_ocupados += 1
				print(f"Pasaje vendido: asientos disponibles en primera clase {vuelo.info.asientos_primera - vuelo.info.asientos_primera_ocupados }")
			else:
				print("No hay asientos disponibles en esta clase")
		else:
			print("La clase ingresada no es correcta.")
	else:
		print("El numero de vuelo es incorrecto")

def recaudacion(vuelo):
	clase_turista = vuelo.asientos_turista_ocupados * vuelo.km * 75
	clase_primera = vuelo.asientos_primera_ocupados * vuelo.km * 203
	return clase_primera + clase_turista

def eliminar_vuelo(listaVuelos, numeroVuelo):
	eliminado = li.eliminar(listaVuelos, numeroVuelo, 'numeroVuelo')

	if eliminado is not None:
		print(f"Cantidad de dinero a devolver: ${recaudacion(eliminado.info)}")
		return recaudacion(eliminado.info)
	else:
		print("No se encontro el vuelo.")

def vuelos_fecha(listaVuelos, fecha):
	vuelo = listaVuelos.inicio

	while vuelo is not None:
		if vuelo.info.fechaSalida == fecha:
			print(vuelo.info)
		vuelo = vuelo.sig

for vuelo in vuelos:
	li.insertar(listaVuelos, vuelo, 'fechaSalida')

def buscar_destino(listaVuelos, destino):
	vuelo = listaVuelos.inicio

	while vuelo is not None:
		if vuelo.info.destino == destino:
			print(vuelo.info)
		vuelo = vuelo.sig	

#A
'''
destinos = ['Atenas', 'Miconos', 'Rodas']

for destino in destinos:
	print(f"Vuelos Con destino a {destino}")
	buscar_destino(listaVuelos, destino)
'''
#B
'''print("Vuelos con asientos disponibles: ")
vuelo = listaVuelos.inicio

while vuelo is not None:
	if asientos_disponibles(vuelo.info, 'turista'):
		print(vuelo.info)

	vuelo = vuelo.sig
'''

#C
'''vuelo = listaVuelos.inicio
while vuelo is not None:
	print(vuelo.info)
	print(f"Total recaudado: ${recaudacion(vuelo.info)}")
	vuelo = vuelo.sig'''

#D
'''fecha = input("Ingresar fecha de vuelo en formato dd-mm-yyyy: ")
vuelos_fecha(listaVuelos, datetime.strptime(fecha, "%d-%m-%Y"))'''


#E
'''print("Vender asiento")
nroVuelo = int(input("Ingresar numero de vuelo: "))
clase = input("Ingresar clase: ")

vender_boleto(listaVuelos, nroVuelo, clase)'''

#F
'''nroVuelo = int(input("Ingresar el numero de vuelo para eliminarlo: ")
eliminar_vuelo(listaVuelos, nroVuelo)'''




#18
'''class Usuario(object):
	def __init__(self, nombre):
		self.nombre = nombre

	def __str__(self):
		return self.nombre

class Commit(object):
	def __init__(self, timestamp, mensaje, archivo, lineasAgregadas):
		self.timestamp = datetime.strptime(timestamp, "%d-%m-%Y %H:%M")
		self.mensaje = mensaje
		self.archivo = archivo
		self.lineasAgregadas = lineasAgregadas

	def __str__(self):
		return "Timestamp: " + self.timestamp.strftime("%d-%m-%Y %H:%M") + "\n"\
				"Mensaje: " + self.mensaje + "\n"\
				"Archivo: " + self.archivo + "\n"\
				"Lineas agregadas: " + str(self.lineasAgregadas) + "\n"

usuarios = [
	Usuario("Ramos Gabriel"),
	Usuario("Walter Bel")
]

commits = [
	Commit("01-01-2020 05:20", "Primer commit", "test.py", 40),
	Commit("05-02-2020 07:20", "Otro commit", "app.py", 38),
	Commit("04-01-2020 19:45", "Segunda version", "tda_lista.py", -15),
	Commit("05-02-2020 17:51", "Algun commit", "app.py", 0),
	Commit("11-02-2020 10:20", "Segundo commit", "app.py", 4),
	Commit("11-02-2020 08:20", "tp04", "hash.py", -9)
]

listaUsuarios = ll.Lista()

for usuario in usuarios:
	ll.insertar(listaUsuarios, usuario, 'nombre')

usuario = listaUsuarios.inicio
while usuario is not None:
	for i in range(random.randint(1,3)):
		ll.insertar(usuario.sublista, commits[random.randint(0,len(commits)-1)], 'timestamp')
	usuario = usuario.sig'''

#ll.barrido_con_sublista(listaUsuarios)

#A
'''
print("\nUsuario/s que hicieron mas commits:")
mayor = 0
usuario = listaUsuarios.inicio
while usuario is not None:
	if usuario.sublista.tamanio > mayor:
		mayor = usuario.sublista.tamanio
	usuario = usuario.sig


usuario = listaUsuarios.inicio
while usuario is not None:
	if usuario.sublista.tamanio == mayor:
		print(usuario.info)
	usuario = usuario.sig
'''


#B
'''usuario = listaUsuarios.inicio
mayor = None
menor = None

while usuario is not None:
	commit = usuario.sublista.inicio
	aux = 0 
	while commit is not None:
		aux += commit.info.lineasAgregadas
		commit = commit.sig
	if mayor is None and menor is None:
		mayor = aux
		menor = aux
	else:
		if aux > mayor:
			mayor = aux
		if aux < menor:
			menor = aux
	usuario = usuario.sig

print("\nUsuario/s con mas lineas de codigo agregadas: ")
usuario = listaUsuarios.inicio
while usuario is not None:
	commit = usuario.sublista.inicio
	aux = 0
	while commit is not None:
		aux += commit.info.lineasAgregadas
		commit = commit.sig
	if aux == mayor:
		print(str(usuario.info) + ": " + str(mayor) + " lineas agregadas.")
	usuario = usuario.sig

print("\nUsuario/s con menos lineas de codigo agregadas: ")
usuario = listaUsuarios.inicio
while usuario is not None:
	commit = usuario.sublista.inicio
	aux = 0
	while commit is not None:
		aux += commit.info.lineasAgregadas
		commit = commit.sig
	if aux == menor:
		print(str(usuario.info) + ": " + str(menor) + " lineas agregadas.")
	usuario = usuario.sig
'''

#D
'''print("\nUsuarios que han realizado al menos un commit con 0 lineas modificadas: ")
usuario = listaUsuarios.inicio

while usuario is not None:
	if ll.busqueda(usuario.sublista, 0, 'lineasAgregadas'):
		print(usuario.info)
	usuario = usuario.sig'''

#E
'''ultimoUsuario = None
ultimoCommit = None
usuario = listaUsuarios.inicio

while usuario is not None:
	commit = usuario.sublista.inicio
	while commit is not None:
		if commit.info.archivo == 'app.py':
			if ultimoUsuario is None:
				ultimoUsuario = usuario
				ultimoCommit = commit
			elif(commit.info.timestamp > ultimoCommit.info.timestamp):
				ultimoUsuario = usuario
				ultimoCommit = commit
		commit = commit.sig
	usuario = usuario.sig
if ultimoUsuario is not None:
	print("\nUltimo usuario que modifico el archivo app.py: ")
	print(ultimoUsuario.info)
	print(ultimoCommit.info)
else:
	print("\nNingun usuario modifico el archivo app.py")
'''






#20
'''class Estacion(object):
	def __init__(self, pais, coordenadas):
		self.pais = pais
		self.coordenadas = coordenadas

	def __str__(self):
		return "Pais: " + self.pais + "\n"\
				"Coordenadas: (" + str(self.coordenadas[0]) + "," + str(self.coordenadas[1]) + "," + str(self.coordenadas[2]) + ")\n"

class Medicion(object):
	def __init__(self, temperatura, presion, humedad, estado, fechaHora):
		self.temperatura = temperatura
		self.presion = presion
		self.humedad = humedad
		self.estado = estado
		self.fechaHora = datetime.strptime(fechaHora, "%d-%m-%Y %H:%M")

	def __str__(self):
		return "Temperatura: " + str(self.temperatura) + "°C" + "\n"\
				"Presion: " + str(self.presion) + "mbar" + "\n"\
				"Humedad: " + str(self.humedad) + "%" + "\n"\
				"Estado: " + self.estado + "\n"\
				"Fecha y hora: " + self.fechaHora.strftime("%d-%m-%Y %H:%M") + "\n"

estaciones = [
	Estacion("Argentina", (20.5,-51.9,0.1)),
	Estacion("Espania", (120.74,-10.3,0.13)),
	Estacion("Japon", (-45.84,-1.52,0.45))
]

listaEstaciones = ll.Lista()

for estacion in estaciones:
	ll.insertar(listaEstaciones, estacion, 'pais')

for i in range(40):
	temperatura = random.randint(5,17)
	presion = random.randint(200,1000)
	humedad = random.randint(0,100)
	estado = random.choice(['lloviendo', 'nublado', 'soleado', 'parcialmente nublado', 'tormenta electrica'])
	fecha = (datetime.strptime("01-03-2020 12:00", "%d-%m-%Y %H:%M") + timedelta(days = (3 * i))).strftime("%d-%m-%Y %H:%M")
	med = Medicion(temperatura, presion, humedad, estado, fecha)
	ll.insertar(ll.busqueda(listaEstaciones, "Argentina", "pais").sublista, med, 'fechaHora')

for i in range(40):
	temperatura = random.randint(15,30)
	presion = random.randint(200,1000)
	humedad = random.randint(0,100)
	estado = random.choice(['lloviendo', 'nublado', 'soleado', 'parcialmente nublado', 'tormenta electrica', 'huracan'])
	fecha = (datetime.strptime("01-03-2020 16:00", "%d-%m-%Y %H:%M") + timedelta(days = (3 * i))).strftime("%d-%m-%Y %H:%M")
	med = Medicion(temperatura, presion, humedad, estado, fecha)
	ll.insertar(ll.busqueda(listaEstaciones, "Espania", "pais").sublista, med, 'fechaHora')

for i in range(40):
	temperatura = random.randint(12,22)
	presion = random.randint(200,1000)
	humedad = random.randint(0,100)
	estado = random.choice(['lloviendo', 'nublado', 'soleado', 'parcialmente nublado', 'tormenta electrica', ''])
	fecha = (datetime.strptime("01-03-2020 23:00", "%d-%m-%Y %H:%M") + timedelta(days = (3 * i))).strftime("%d-%m-%Y %H:%M")
	med = Medicion(temperatura, presion, humedad, estado, fecha)
	ll.insertar(ll.busqueda(listaEstaciones, "Japon", "pais").sublista, med, 'fechaHora')
'''
#C
'''estacion = listaEstaciones.inicio
print("Promedio de temperatura en el mes de Mayo: ")
while estacion is not None:
	medicion = estacion.sublista.inicio
	suma_t = 0
	contador_d = 0
	while medicion is not None:
		if (medicion.info.fechaHora >= datetime.strptime("01-05-2020 00:00", "%d-%m-%Y %H:%M")) and (medicion.info.fechaHora < datetime.strptime("01-06-2020 00:00", "%d-%m-%Y %H:%M")):
			contador_d += 1
			suma_t += medicion.info.temperatura
		medicion = medicion.sig
	print(estacion.info)
	print(f"Promedio de temperatura: {suma_t / contador_d}\n")

	estacion = estacion.sig
'''

#E
'''estacion = listaEstaciones.inicio
print("Estaciones en donde se registraron tormentas electricas o huracanes")
while estacion is not None:
	if ll.busqueda(estacion.sublista, 'tormenta electrica', 'estado') or ll.busqueda(estacion.sublista, 'huracan', 'estado'):
		print(estacion.info)
	estacion = estacion.sig'''







#21
'''class Pelicula(object):
	def __init__(self, nombre, valoracion, anio, recaudacion):
		self.nombre = nombre
		self.valoracion = valoracion
		self.anio = anio
		self.recaudacion = recaudacion

	def __str__(self):
		return "Nombre: " + self.nombre + "\n"\
		"Valoracion: " + str(self.valoracion) + "\n"\
		"Anio: " + str(self.anio) + "\n"\
		"Recaudacion: " + str(self.recaudacion) + "\n"

listaPeliculas = li.Lista()

li.insertar(listaPeliculas, Pelicula('asdsdwdf', 10, 2020, 150000), 'anio')
li.insertar(listaPeliculas, Pelicula('bsdsdwdf', 9, 2017, 300000), 'anio')
li.insertar(listaPeliculas, Pelicula('csdsdwdf', 8, 2018, 450000), 'anio')
li.insertar(listaPeliculas, Pelicula('dsdsdwdf', 10, 2019, 50000), 'anio')
li.insertar(listaPeliculas, Pelicula('esdsdwdf', 7, 2017, 130000), 'anio')
li.insertar(listaPeliculas, Pelicula('fsdsdwdf', 6, 2018, 1000000), 'anio')
li.insertar(listaPeliculas, Pelicula('gsdsdwdf', 5, 2017, 1000000), 'anio')

while True:
	nombre = input("Ingresar el nombre de la pelicula: ")
	if nombre == '':
		break
	valoracion = int(input("Ingresar la valoracion (1-10): "))
	anio = int(input("Ingresar el anio: "))
	recaudacion = float(input("Ingresar recaudacion: "))
	li.insertar(listaPeliculas, Pelicula(nombre, valoracion,anio,recaudacion), 'anio')

def filtrar_anio(lista, anio):
	pelicula = lista.inicio

	while pelicula is not None:
		if pelicula.info.anio == anio:
			print(pelicula.info)
		pelicula = pelicula.sig

def mayor_recaudacion(lista):
	pelicula = lista.inicio
	mayor = 0
	
	while pelicula is not None:
		if pelicula.info.recaudacion > mayor:
			mayor = pelicula.info.recaudacion
		pelicula = pelicula.sig

	pelicula = lista.inicio
	while pelicula is not None:
		if pelicula.info.recaudacion == mayor:
			print(pelicula.info)
		pelicula = pelicula.sig

def mayor_valoracion(lista):
	pelicula = lista.inicio
	mayor = 0
	
	while pelicula is not None:
		if pelicula.info.valoracion > mayor:
			mayor = pelicula.info.valoracion
		pelicula = pelicula.sig

	pelicula = lista.inicio
	while pelicula is not None:
		if pelicula.info.valoracion == mayor:
			print(pelicula.info)
		pelicula = pelicula.sig
'''
#A
'''print("\nFiltrar por anio")
anio = int(input("Ingresar anio: "))
filtrar_anio(listaPeliculas, anio)'''

#B
'''print("\nPelicula/s con mayor recaudacion")
mayor_recaudacion(listaPeliculas)'''

#C
'''print("\nPelicula/s con mayor valoracion")
mayor_valoracion(listaPeliculas)'''

#D
'''li.barrido(ordenarPor(listaPeliculas, 'nombre'))
li.barrido(ordenarPor(listaPeliculas, 'recaudacion'))
li.barrido(ordenarPor(listaPeliculas, 'anio'))
li.barrido(ordenarPor(listaPeliculas, 'valoracion'))'''