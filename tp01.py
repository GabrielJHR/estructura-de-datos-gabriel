#Ejercicio 1
def Fibonacci(pos):
	#Caso Base
	if (pos <= 0):
		return 0
	if (pos == 1):
		return 1

	#Recursividad
	if (pos > 1):
		return Fibonacci(pos-1)+Fibonacci(pos-2)



#Ejercicio 2
def SumatoriaEnteros(num):
	if(num <= 0):
		return 0
	else:
		return num + SumatoriaEnteros(num-1)



#Ejercicio 3
def Producto(factor1, factor2):
	#Caso base
	if(factor2 < 0):
		return(Producto(factor2,factor1))

	if(factor2 == 1):
		return factor1

	if(factor1 == 0 or factor2 == 0):
		return 0

	#Recursividad
	return factor1 + Producto(factor1, factor2 - 1)


#Ejercicio 4
def Potencia(base, exp):
	if(exp >= 0):
		#Caso base
		if(exp == 1):
			return base
		if(exp == 0):
			return 1
		
		#Recursividad
		return base * Potencia(base, exp - 1) 


#Ejercicio 5
def CadenaInvertida(cadena):
	if(cadena == ""):
		return ""	
	else:
		return cadena[-1] + CadenaInvertida(cadena[0:-1])

#Ejercicio 6
def SerieH(n):
	if(n>0):
		if(n == 1):
			return 1
		else:
			return (1/n) + SerieH(n-1)


#Ejercicio 7
def Binario(num):

	if(num == 1):
		return 1
	elif (num == 0):
		return 0
	else:
		return str(Binario(num // 2)) + str(num%2)

#Ejercicio 8
def Logaritmo(base, argumento):
	if(argumento<base):
		return 0
	else:
		return 1 + Logaritmo(base, (argumento//base))

#Ejercicio 9
def Digitos(num):
	if(num > -10 and num < 10):
		return 1
	else: 
		return 1 + Digitos(num/10)


#Ejercicio 10
def InvertirNumero(num):
	if(num > -10 and num < 10):
		return num
	else:
		return (num%10) * pow(10,Digitos(num)-1) + InvertirNumero(num//10)

#Ejercicio 11
def MCD(num1, num2):
	if(num1%num2 == 0):
		return num2
	else:
		return MCD(num2, (num1%num2))

#Ejercicio 12

#Ejercicio 13
def SumatoriaDigitos(num):
	if(num > -10 and num < 10):
		return num
	else:
		return (num%10) + SumatoriaDigitos(num//10)

#Ejercicio 14
def RCAux(radicando, i):
	if(radicando>=(i*i)):
		return RCAux(radicando, i+1)
	else:
		return i-1

def RaizCuadrada(radicando):
	if(radicando >= 0):
		return RCAux(radicando, 0)

#Ejercicio 15
def A(n):
	if(n>=1):
		if(n == 1):
			print(2)
			return 2
		else:
			print(2*(-3)**(n-1))
			return A(n-1)*(-3)

#Ejercicio 16
def VectorInverso(vector):
	if(vector != ""):
		if(len(vector) != 1):
			print(vector[-1])
			VectorInverso(vector[0:-1])
		else:
			print(vector[0])

#Ejercicio 17
def Matriz(matriz, i, j):
	if(len(matriz)== i):
		print("")
	else:
		if(len(matriz[i]) == j):
			print("")
			Matriz(matriz, i + 1, 0)
		else:
			print(matriz[i][j])
			Matriz(matriz, i , j + 1)

#Ejercicio 18
def Funcion(n):
	if(n == 1):
		return 2
	elif(n >= 2):
		return 1/(n + (Funcion(n - 1)))

#Ejercicio 19
def CentinelaAux(vector):
	if(vector[0]==vector[-1]):
		return 1
	else:
		return 1 + CentinelaAux(vector[1:len(vector)])

def Centinela(vector, centinela):
	
	vector.append(centinela)
	pos = CentinelaAux(vector)

	if(pos == len(vector)):
		return -1
	else:
		return pos

#Ejercicio 20
def Binaria(vector, elemento):
	i = len(vector)//2
	j = len(vector)

	if(j==1):
		if(vector[0] == elemento):
			return 1
		else:
			return 0
	else:
		if(elemento < vector[i]):
			return Binaria(vector[0:i], elemento)
		elif(elemento > vector[i]):
			return Binaria(vector[i:j], elemento)
		else:
			return 1

#Ejercicio 21
def Revision(vector):
	if(len(vector) != 0):
		if(vector[-1][2] == 'true'):
			return Revision(vector[0:-1]) + 1
		else:
			return Revision(vector[0:-1]) + 0
	else:
		return 0

#Ejercicio 23
def Hanoi(discos,a1,a2,a3):
	if(discos == 1):
		print(f"{a1} -> {a3}")
	else:
		Hanoi(discos-1,a1, a3, a2)
		print(f"{a1} -> {a3}")
		Hanoi(discos-1, a2, a1, a3)

#Ejercicio 24
def GeometricaI(An):
	if(An >= 5.25):
		print(An)
		GeometricaI(An/4)
		
#Ejercicio 25
def Sucesion25(n):
	if(n >= 1):
		if(n == 1):
			return 3
		else:
			return Sucesion25(n-1)+(2*n)

#Ejercicio 26
def g(x):
	return (x**2) + 2*x -2

def Biseccion(a,b):
	x = (a+b)/2
	y = g(x)

	if(y<0):
		return Biseccion(x , b)
	elif(y>0):
		return Biseccion(a , x)
	else:
		return x

#Ejercicio 27
def MetodoSecante(x0,x1,iteraciones):
	if(iteraciones == 0):
		return x1
	else:
		x2 = x1 - ((g(x1)*(x0-x1))/(g(x0)-g(x1)))
		return MetodoSecante(x1, x2, iteraciones - 1)

#Ejercicio 28
def DerivadaEnUnPunto(punto, aproximacion):#aproximacion
	return (g(punto+aproximacion)-g(punto))/((punto+aproximacion)-punto)

def MetodoNewtonRaphson(aproximacion):
	x = aproximacion - (g(aproximacion)/DerivadaEnUnPunto(aproximacion, 0.000000001))
	if(g(x)==0):
		return x
	else:
		return MetodoNewtonRaphson(x)

