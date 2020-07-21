class Cola(object):
	"""docstring for cola"""
	def __init__(self):
		self.items = []

	def vacia(self):
		if self.items == []:
			return True
		else:
			return False

	def insertar(self, elemento):
		self.items.append(elemento)

	def eliminar(self):
		if not self.vacia():
			return self.items.pop(0)

	def cabeza(self):
		if not self.vacia():
			return self.items[0]

	def lista(self):
		return self.items

	def __len__(self):
		return len(self.items)

	def __str__(self):
		cadena = ""
		for i in range(len(self.items) - 1):
			cadena = cadena + str(self.items[i])  + ", "
		cadena = cadena + str(self.items[-1])

		return cadena