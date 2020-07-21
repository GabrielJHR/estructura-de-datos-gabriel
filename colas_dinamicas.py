class Nodo(object):
	def __init__(self, dato):
		self.dato = dato
		self.siguiente = None

	def __str__(self):
		return str(self.dato)

class Cola(object):

	def __init__(self):
		self.primero = None
		self.tamanio = 0
		self.items = self.lista()

	def vacia(self):
		if(self.tamanio == 0):
			return True
		else:
			return False

	def insertar(self, dato):
		nodo = Nodo(dato)
		if self.vacia() == True:
			self.primero = nodo
		else:
			actual = self.primero
			while actual.siguiente != None:
				actual = actual.siguiente
			actual.siguiente = nodo

		self.tamanio += 1

	def eliminar(self):
		if not self.vacia():
			dato = self.primero.dato
			self.primero = self.primero.siguiente
			self.tamanio -= 1
			return dato

	def cabeza(self):
		if not self.vacia():
			return self.primero.dato

	def lista(self):
		lista = []
		actual = self.primero
		if self.vacia() == True:
			return lista
		else:
			while actual != None:
			 	lista.append(actual.dato)
			 	actual = actual.siguiente

		return lista

	def __len__(self):
		return self.tamanio

	def __str__(self):
		cadena = ""
		actual = self.primero
		if self.tamanio == 0:
			return "[]"
		elif(self.tamanio == 1):
			return str(self.primero.dato)
		else:
			cadena = ""
			actual = self.primero

			while actual.siguiente != None:
				cadena = cadena + str(actual.dato) + ", "
				actual = actual.siguiente
			cadena = cadena + str(actual.dato)

			return cadena