class Pila(object): #clase base para crear pilas
	def __init__(self):
		self.pila1=[]# el programa solo requiere una lista para la pila
	def apilar(self, dato):# recibe el numero de version como parametro
		self.pila1.append(dato)
		
	def pila_vacia(self): # metodo en caso de que la pila este vacia y se quiera sacar otra version
		
		if len(self.pila1)==0:
			print"Ya no hay mas migraciones"
			return True
		else:
			return False
	def desapilar(self):# metodo para sacar una migracion
		if self.pila_vacia():
			return True
		else:
			print("La version "+str( self.pila1.pop())+ " ha salido")
contador=0
versiones=Pila()
while True:# condicion para ejecutar siempre el menu, hasta que el usuario quiera salir
	print "***********************************"
	print"Menu Versiones de proyecto"
	print"1-Ingresar una nueva version"
	print"2-Obtener las versiones"
	print"3-Salir del programa"
	opc=int(input("Ingrese su seleccion "))
	if opc==1:
		contador +=1
		versiones.apilar(contador)
	elif opc==2:
		versiones.desapilar()
	elif opc==3:
		break
	
