import random

class Pila():

	def __init__(self):
		self.pila = []

	def apilar(self, dato):
		self.pila.append(dato)

	def desapilar(self):
		if(self.pilaVacia() == 0):
			return self.pila.pop()
		else:
			return  None

	def pilaVacia(self):
		if(self.pila == []):
			return 1
		else:
			return 0

	def llenarPila(self,inicio,fin):
		for i in range(fin):
			self.apilar(random.randint(inicio,fin))

	def llenarPila(self,inicio,fin,iteraciones):
		for i in range(iteraciones):
			self.apilar(random.randint(inicio,fin))		

	def apilarVector(self, vectorOrigen):
		while vectorOrigen != []:
			self.apilar(vectorOrigen.pop())

	def apilarCadena(self, cadena):
		vectorCadena = []
		while cadena != "":
			vectorCadena.append(cadena[-1])
			cadena = cadena[0:-1]

		while vectorCadena != []:
			self.apilar(vectorCadena.pop())

	def vaciarPila(self):
		while self.pilaVacia() == 0:
			self.desapilar()

	def vaciarPila(self, pila):
		while self.pilaVacia() == 0:
			pila.apilar(self.desapilar())
		return pila
