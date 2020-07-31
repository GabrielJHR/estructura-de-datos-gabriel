import tda_tabla_hash as t
import random
from datetime import date, datetime, timedelta, time
from tda_lista import *			
from math import *		

def rehashing_tc(tabla, tamanio, funcHash = None):
	nueva_tabla = t.crear_tabla(tamanio)
	if funcHash != None:
		for i in range(len(tabla)):
			elemento = tabla[i]
			if(elemento is not None):
				agregar_tc(nueva_tabla, funcHash, elemento)

	return nueva_tabla
def agregar_tc(tabla, hash, dato):
	#Las funciones del archivo tda_tabla_hash.py no me funcionaron a mi o yo las use mal
	pos = sondeo(tabla, hash, dato)
	tabla[pos] = dato

def sondeo(tabla, hash, dato):
	pos = hash(dato, tabla)
	posAux = pos
	if tabla[pos] == None:
		return pos
	else:
		pos = pos + 1
		if pos == len(tabla):
			pos = 0
		while tabla[pos] != None and pos != posAux:
			if pos + 1 == len(tabla):
				pos = -1
			pos += 1

		if pos == posAux:
			return None
		else:
			return pos

def busqueda_tc(tabla, hash, dato, campo = None):
	pos = hash(dato, tabla)
	if criterio(tabla[pos], campo) == criterio(dato, campo):
		return pos
	else:
		posAux = pos
		pos = pos + 1
		if pos == len(tabla):
			pos = 0
		while criterio(tabla[pos], campo)!= criterio(dato, campo) and pos != posAux:
			if pos + 1 == len(tabla):
				pos = -1
			pos += 1

		if pos == posAux:
			return None
		else:
			return pos

def buscar_ta(tabla, hash, dato, campo=None):
    posicion = hash(dato, tabla)
    if(tabla[posicion] is not None):
        return busqueda(tabla[posicion], criterio(dato, campo), campo)
    else:
        return None

def criterio(dato, campo=None):
    """Determina el campo por el cual se debe comparar el dato."""
    dic = {}
    if(hasattr(dato, '__dict__')):
        dic = dato.__dict__
    if campo is None or campo not in dic:
        return dato
    else:
        return dic[campo]

def barrido_ta(tabla):
	for i in range(len(tabla)):
		if tabla[i] is not None:
			print("Posicion "+ str(i+1))
			barrido(tabla[i])

def barrido_tc(tabla):
	for i in range(len(tabla)):
		if tabla[i] is not None:
			print("Posicion " + str(i))
			print(tabla[i])

#Ejercicio 1
'''class Palabra(object):
	def __init__(self, palabra, definicion):
		self.palabra = palabra
		self.definicion = definicion

	def __str__(self):
		return self.palabra + ": " + self.definicion + "\n"

diccionario = t.crear_tabla(28)
p1 = Palabra("lista", "Las listas en Python son un tipo contenedor, compuesto, que se usan para almacenar conjuntos de elementos relacionados del mismo tipo o de tipos distintos")
p2 = Palabra("diccionario", "Estos diccionarios nos permiten además identificar cada elemento por una clave (Key). Para definir un diccionario, se encierra el listado de valores entre llaves.")

t.agregar_ta(diccionario, t.hash_diccionario, p1, 'palabra')
t.agregar_ta(diccionario, t.hash_diccionario, p2, 'palabra')

while True:
	p = input("Ingresar una palabra: ")
	if p == '':
		break
	d = input("Ingresar una definicion: ")
	oPalabra = Palabra(p, d)
	t.agregar_ta(diccionario, t.hash_diccionario, oPalabra, 'palabra')

resultado = buscar_ta(diccionario, t.hash_diccionario, Palabra(input('Ingresar palabra para buscar: '),''), 'palabra')

if resultado is None:
	print("No se encontro la palabra")
else:
	print(resultado.info)

t.quitar_ta(diccionario, t.hash_diccionario, Palabra(input("Ingresar palabra para borrar del diccionario: "), ''), 'palabra' )

barrido_ta(diccionario)'''



#Ejercicio 2
'''class Contacto(object):
	def __init__(self, numeroTelefono, apellido, nombre, direccion):
		self.numeroTelefono = numeroTelefono
		self.apellido = apellido
		self.nombre = nombre
		self.direccion = direccion

	def __str__(self):
		return "Nombre: " + self.nombre + "\n"\
		"Apellido: " + self.apellido + "\n"


guiaTelefonica = t.crear_tabla(13)

while True:
	nombre = input("Nombre: ")
	if nombre == '':
		break
	apellido = input("Apellido: ")
	num = int(input("Numero: "))
	direccion = input("Direccion: ")

	oContacto = Contacto(num, apellido, nombre, direccion)

	t.agregar_ta(guiaTelefonica, t.hash_guia_telefono, oContacto, 'numeroTelefono')

print("Barrido")
barrido_ta(guiaTelefonica)
'''


#Ejercicio 3
'''class Catedra(object):
	def __init__(self, codigo, nombre, modalidad, horas):
		self.codigo = codigo
		self.nombre = nombre
		self.modalidad = modalidad
		self.horas = horas
		self.docentes = []

	def __str__(self):
		return "Codigo: " + self.codigo + "\n"\
		"Nombre: " + self.nombre + "\n"\
		"Modalidad: " + self.modalidad + "\n"\
		"Horas: " + str(self.horas) + "\n"\
		"Docentes: " + str(self.docentes) + "\n"

def hash_catedra(dato, tabla):
	return t.bernstein(dato.codigo, tabla)

tablaCatedras = t.crear_tabla(10)

catedra = Catedra('ALG_34211', 'algoritmos y estructuras de datos', 'anual', 4)
agregar_tc(tablaCatedras, hash_catedra, catedra)
catedra = Catedra('ALG_34212', 'programacion orientada a objetos', 'anual', 5)
agregar_tc(tablaCatedras, hash_catedra, catedra)
catedra = Catedra('ALG_34213', 'fundamentos de programacion', 'anual', 5)
agregar_tc(tablaCatedras, hash_catedra, catedra)
catedra = Catedra('ALG_34323', 'progrmacion avanzada', 'cuatrimestral', 4)
agregar_tc(tablaCatedras, hash_catedra, catedra)

pos = busqueda_tc(tablaCatedras, hash_catedra, Catedra('ALG_34323', '', '', 0), 'codigo')
tablaCatedras[pos].docentes.append("Walter")

pos = busqueda_tc(tablaCatedras, hash_catedra, Catedra('ALG_34212', '', '', 0), 'codigo')
if pos is not None:
	tablaCatedras[pos].docentes.append('Tito')

barrido_tc(tablaCatedras)
'''





#Ejercicio 4
'''pStarWars = t.crear_tabla(10)

while True:
	personaje = input("Ingresar el nombre de un personaje: ")
	if personaje == '':
		break

	factorCarga = t.cantidad_elementos_tc(pStarWars) / len(pStarWars)
	
	if factorCarga > 0.75:
		pStarWars = rehashing_tc(pStarWars, len(pStarWars) * 2 ,t.bernstein)

	agregar_tc(pStarWars, t.bernstein, personaje)

print(pStarWars)'''


#Ejercicio 5
'''class ContactoPersona(object):
	def __init__(self, nombre, apellido, email):
		self.nombre = nombre
		self.apellido = apellido
		self.email = email

	def __str__(self):
		return self.nombre + ", " + self.apellido + ", " + self.email + "\n"

def hash_contacto(dato, tabla):
	return t.bernstein((dato.nombre +' '+ dato.apellido), tabla)

tablaContactos = t.crear_tabla(1)

while True:
	nombre = input("Ingresar nombre: ")
	if nombre == '':
		break
	apellido = input("Ingresar apellido: ")
	email = input("Ingresar email: ")

	if len(tablaContactos) == t.cantidad_elementos_tc(tablaContactos):
		tablaContactos = rehashing_tc(tablaContactos, len(tablaContactos) * 2, hash_contacto)

	agregar_tc(tablaContactos, hash_contacto, ContactoPersona(nombre, apellido, email))

barrido_tc(tablaContactos)'''



#Ejercicio 6
'''class Stormtrooper(object):

    def __init__(self, legion, codigo):
        self.legion = legion
        self.codigo = codigo
    
    def __str__(self):
        return self.legion+' '+str(self.codigo)

def hash_cod_letras(dato, tabla):
	return t.bernstein(dato.legion, tabla)

def hash_cod_num(dato, tabla):
	return int(dato.codigo) % len(tabla)

letrasCodigos = ["FL", "TF", "TK", "CT", "FN", "FO"]

tablaCod_1 = t.crear_tabla(1000)
tablaCod_2 = t.crear_tabla(6)

for i in range(2000):
	st = Stormtrooper(random.choice(letrasCodigos), random.randint(1000,9999))

	t.agregar_ta(tablaCod_1,hash_cod_num,st,'codigo')
	t.agregar_ta(tablaCod_2,hash_cod_letras,st,'legion')

print("Los Stormtrooper terminados en 781 son: ")
resultado = tablaCod_1[hash_cod_num(Stormtrooper('', 781), tablaCod_1)]
if resultado is not None:
	barrido(resultado)
else:
	print("Ningun Stormtrooper tiene como codigo 781")

print("Los Stormtrooper terminados en 537 son: ")
resultado = tablaCod_1[hash_cod_num(Stormtrooper('', 537), tablaCod_1)]
if resultado is not None:
	barrido(resultado)
else:
	print("Ningun Stormtrooper tiene como codigo 537")

print("Los Stormtrooper de la legion CT son: ")
resultado = tablaCod_2[hash_cod_letras(Stormtrooper('CT', 0), tablaCod_2)]
if resultado is not None:
	stormtrooper = resultado.inicio

	while stormtrooper.sig is not None:
		if stormtrooper.info.legion == 'CT':
			print(stormtrooper.info)
		stormtrooper = stormtrooper.sig
else:
	print("La legion CT no tiene Stormtroopers")

print("Los Stormtrooper de la legion TF son: ")
resultado = tablaCod_2[hash_cod_letras(Stormtrooper('TF', 0), tablaCod_2)]
if resultado is not None:
	stormtrooper = resultado.inicio

	while stormtrooper.sig is not None:
		if stormtrooper.info.legion == 'TF':
			print(stormtrooper.info)
		stormtrooper = stormtrooper.sig
else:
	print("La legion TF no tiene Stormtroopers")
'''

#Ejercicio 7
'''class Pokemon(object):
	def __init__(self, nombre, tipo, num, nivel):
		self.nombre = nombre
		self.tipo = tipo
		self.num = num
		self.nivel = nivel

	def __str__(self):
		return "Nombre: " + self.nombre + "\n"\
		"Tipo: " + str(self.tipo) + "\n"
		"Numero: " + str(self.num) + "\n"\
		"Nivel: " + str(self.nivel) + "\n"

def hash_pokemon_tipo(dato, tabla):
	return t.bernstein(dato, tabla)

def hash_pokemon_num(dato, tabla):
	return dato.num % len(tabla)

tablaPokemons = t.crear_tabla(10)


while True:
	nombre = input("Ingresar nombre del Pokemon: ")
	if nombre == '':
		break
	
	listaTipos = []
	while True:
		tipo = input("Ingresar tipo de Pokemon: ")
		if tipo == '':
			break
		listaTipos.append(tipo) 
	num = int(input("Ingresar numero de Pokemon: "))
	nivel = int(input("Ingresar nivel: "))

	pokemon = Pokemon(nombre, listaTipos, num, nivel)


	for i in range(len(pokemon.tipo)): 
		pos = sondeo(tablaPokemons, hash_pokemon_tipo, pokemon.tipo[i])

		#si el tipo de pokemon no esta en la tabla principal crea una tabla secundaria en la posicion
		if pos != None:
			if tablaPokemons[pos] == None:
				tablaPokemons[pos] = t.crear_tabla(15)
			t.agregar_ta(tablaPokemons[pos], hash_pokemon_num, pokemon, 'num')


#Recorrer la tabla principal, en cada posicion de la tabla principal recorre
#la subtabla y en cada posicion de la tabla hace un barrido de las listas
for i in range(len(tablaPokemons)):
	if tablaPokemons[i]:
		for j in range(len(tablaPokemons[i])):
			if tablaPokemons[i][j] != None:
				barrido(tablaPokemons[i][j])
'''


#Ejercicio 8
class Caracter(object):
	def __init__(self, caracter, encriptado):
		self.caracter = caracter
		self.encriptado = encriptado

	def __str__(self):
		return self.caracter

def hash_encriptar(dato, tabla):
	return ord(dato.caracter) % len(tabla)

def hash_desencriptar(dato, tabla):
	return t.bernstein(dato.encriptado, tabla)

'''tablaEncriptar = t.crear_tabla(125 - 32)
tablaDesencriptar = t.crear_tabla(125 - 32)

for i in range(32,125):
	cod = ""
	for j in range(8):
		cod += chr(random.randint(32, 125))
	oCaracter = Caracter(chr(i), cod)

	agregar_tc(tablaEncriptar, hash_encriptar, oCaracter)
	agregar_tc(tablaDesencriptar, hash_desencriptar, oCaracter)

print("ENCRIPTAR MENSAJE")
mensaje = input("Escribir mensaje: ")

mensajeEncriptado = ""

for caracter in mensaje:
	pos = hash_encriptar(Caracter(caracter, ''), tablaEncriptar)
	mensajeEncriptado += tablaEncriptar[pos].encriptado


print("\nMensaje encriptado: [" + mensajeEncriptado + "]" )

mensajeDesencriptado = ''
posAux = 0
for i in range(0, len(mensajeEncriptado), 8):
	charEnc = mensajeEncriptado[posAux: i + 8]

	pos = busqueda_tc(tablaDesencriptar, hash_desencriptar, Caracter('',charEnc), 'encriptado')
	mensajeDesencriptado += tablaDesencriptar[pos].caracter
	posAux += 8

print("Mensaje desencriptado: " + mensajeDesencriptado + "\n")'''






'''#Ejercicio 9
valores = { "1" : "abd", "2" : "def", "3" : "ghi", "4" : "jkl", "5" : "mnñ", "6" : "opq", "7" : "rst", "8" : "uvw", "9" : "xyz", "0" : "#?&"}

#Crear la tabla
tablaCaracteres = t.crear_tabla(10)

mensaje = input("Ingresar un mensaje: ")
mensajeEncriptado = ""

#Convertir cada caracter en numeros y generar el codigo
#Despues agregarlo a una tabla abierta
for caracter in mensaje:
	nums = str(ord(caracter))
	cod = ""
	
	for num in nums:
		cod += valores[num]

	cod += "%"

	oCaracter = Caracter(caracter, cod)

	t.agregar_ta(tablaCaracteres, hash_desencriptar, oCaracter, 'encriptado')

	mensajeEncriptado += cod 

print("Mensaje encriptado: " + mensajeEncriptado)


#A cada caracter del mensaje encriptado agregarlo a la variable car hasta que encuentre un %
#a la variable mensajeDesencriptado añadirle el resultado de la busqueda en la tabla
mensajeDesencriptado = ""
car = ""
for i in mensajeEncriptado:
	car += i	
	if i == '%':
		mensajeDesencriptado += buscar_ta(tablaCaracteres, hash_desencriptar, Caracter('', car), 'encriptado').info.caracter
		car = ''

print("Mensaje desencriptado: " + mensajeDesencriptado)'''






#Ejercicio 10
'''def codificar(caracter):
	resultado = ""
	t_caracter = str(ord(caracter) * 37)

	if ord(caracter) <= 78:
		complemento = 79 + ord(caracter) - 32
	else:
		complemento = 32 + ord(caracter) - 79

	for i in t_caracter:
		resultado += chr((int(i) ** 2) + complemento)

	resultado += chr(complemento)

	return resultado

def decodificar(cadena):
	complemento = ord(cadena[-1])
	nums = ""
	for i in cadena[0:-1]:
		nums += str(int(sqrt(ord(i) - complemento)))

	return chr(int(nums) // 37)

tablaDesencriptar = t.crear_tabla(128)

def decodificar_mensaje(tabla, mensaje):
	mensajeDesencriptado = ""

	posAux = 0
	#Recorrer el mensaje extraido del archivo con paso 5 para cargar los caracteres a la tabla
	for i in range(0,len(mensaje),5):
		caracter = mensaje[posAux:i+5]
		oCaracter = Caracter(decodificar(caracter), caracter)

		resultado = busqueda_tc(tabla, hash_desencriptar, oCaracter, 'encriptado')
		if resultado is None:
			agregar_tc(tabla, hash_desencriptar, oCaracter)

		posAux += 5

	#Buscar los caracteres en la tabla y concatenarlos a la variable mensajeDesencriptado
	posAux = 0
	for i in range(0,len(mensaje),5):
		caracter = mensaje[posAux:i+5]
		oCaracter = Caracter('', caracter)

		resultado = busqueda_tc(tabla, hash_desencriptar, oCaracter, 'encriptado')
		if resultado is not None:
			mensajeDesencriptado += tabla[resultado].caracter

		posAux += 5

	return mensajeDesencriptado

#MENSAJE
f = open("mensaje_1.txt", "r", encoding = 'utf-8')
print("Mensaje 1: " + decodificar_mensaje(tablaDesencriptar,f.read()) + "\n")
f = open("mensaje_2.txt", "r", encoding = 'utf-8')
print("Mensaje 2: " +decodificar_mensaje(tablaDesencriptar,f.read()) + "\n")
f = open("mensaje_3.txt", "r", encoding = 'utf-8')
print("Mensaje 3: "+decodificar_mensaje(tablaDesencriptar,f.read()) + "\n")

f.close()
'''