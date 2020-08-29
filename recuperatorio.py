import tda_lista as li
import tda_cola as c
import tda_tabla_hash as t

#Ejercicio 1
def contador_palabras(pos, palabras, palabra):
	if pos < len(palabras):
		if palabras[pos] == palabra:
			return 1 + contador_palabras(pos + 1, palabras, palabra)
		else:
			return contador_palabras(pos + 1, palabras, palabra)
	else:
		return 0

palabras = ["asd", "avs", "ddd", "asd", "asd"]

print(contador_palabras(0, palabras, "asd"))



#Ejercicio 2
class Personaje(object):
	"""docstring for Personaje"""
	def __init__(self, nombre_s, anio, nombre_p = "",grupo = "" ):
		self.nombre_p = nombre_p
		self.nombre_s = nombre_s
		self.anio = anio
		self.grupo = grupo

p1 = Personaje("Capitana Marvel", 1992, "", "Guardianes de la galaxia")
p2 = Personaje("Vlanck Widow", 1961, "asd", "Guardianes de la galaxia")


listaPersonajes = li.Lista()

li.insertar(listaPersonajes, p1, 'nombre_s')
li.insertar(listaPersonajes, p2, 'nombre_s')

#A
if li.busqueda(listaPersonajes, 'Capitana Marvel', 'nombre_s'):
	print("Capitana Marvel esta en la lista")
else:
	print("Capitana Marvel no esta en la lista")

#B
colaGuardianes = c.Cola()
nPersonaje = listaPersonajes.inicio
while nPersonaje is not None:
	if nPersonaje.info.grupo == 'Guardianes de la galaxia':
		c.arribo(colaGuardianes, nPersonaje.info)
	nPersonaje = nPersonaje.sig

print(colaGuardianes.tamanio)

#D
listaAnio = li.Lista()

nPersonaje = listaPersonajes.inicio
while nPersonaje is not None:
	if nPersonaje.info.anio > 1960 and nPersonaje.info.nombre_p != "":
		li.insertar(listaAnio, nPersonaje, 'nombre_s')
	nPersonaje = nPersonaje.sig

#E
if li.eliminar(listaPersonajes, "Vlanck Widow", 'nombre_s'):
	li.insertar(listaPersonajes, Personaje("Black Widow", 1961, "asd", "Guardianes de la galaxia"), 'nombre_s')


#Ejercicio 3
#A
def bernstein_libro(dato, tabla):
    """Función hash de Bernstein para cadenas."""
    h = 0
    for caracter in dato.titulo:
        h = h * 33 + ord(caracter)
    return h % len(tabla)

class Libro(object):
	def __init__(self, titulo, editorial, paginas):
		self.titulo = titulo
		self.editorial = editorial
		self.paginas = paginas

tablaLibros = t.crear_tabla(9)

#C
lib1 = Libro("asd", "tyuiow", 158)
t.agregar_ta(tablaLibros, bernstein_libro, lib1, 'titulo')
lib2 = Libro("asdw", "iow", 256)
t.agregar_ta(tablaLibros, bernstein_libro, lib2, 'titulo')
lib3 = Libro("aasdw", "tyow", 514)
t.agregar_ta(tablaLibros, bernstein_libro, lib3, 'titulo')
t.agregar_ta(tablaLibros, bernstein_libro, Libro("wdwdp", "qwert", 355), 'titulo')
t.agregar_ta(tablaLibros, bernstein_libro, Libro("xcvbn", "qwerecxt", 3658), 'titulo')
t.agregar_ta(tablaLibros, bernstein_libro, Libro("jksdl", "qwdwweert", 220), 'titulo')
t.agregar_ta(tablaLibros, bernstein_libro, Libro("asdwd", "qwert", 360), 'titulo')
t.agregar_ta(tablaLibros, bernstein_libro, Libro("12331w31", "qwert", 144), 'titulo')
t.agregar_ta(tablaLibros, bernstein_libro, Libro("wp", "qaswert", 785), 'titulo')
t.agregar_ta(tablaLibros, bernstein_libro, Libro("wdwdp", "qwert", 763), 'titulo')

#B
print(f"El libro Los 100 estara ubicado en la posicion {bernstein_libro(Libro('Los 100', '', 0), tablaLibros)} de la tabla")

#D
for i in range(len(tablaLibros)):
	if tablaLibros[i]:
		print(f"Cantidad de libros en la sublista {i+1}: {tablaLibros[i].tamanio}")