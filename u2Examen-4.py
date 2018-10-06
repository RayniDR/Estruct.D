import os
class Cola(object): #clase base para crear colas
	def __init__(self):
		self.cola1=[]# el programa solo requiere una lista para la cola
	def encolar(self, dato):# recie el numero del cliente como parametro
		if len (self.cola1)<=4:# antes de agregar datos verifico que no tenga mas de 5 elementos
			self.cola1.append(dato)
		else:
			
			print("La fila ya tiene 5 personas")
	def cola_vacia(self): # metodo en caso de que la fila este vacia y se quiera sacar un cliente
		
		if len(self.cola1)==0:
			print"La fila ya esta vacia"
			return True
		else:
			return False
	def desencolar(self):# metodo para sacar un cliente
		if self.cola_vacia():
			return True
		else:
			print("El cliente "+str( self.cola1.pop(0))+ " fue atendido")
	def revisar(self):# metodo para imprimir cuantos clientes hay y su numero
		print"Hay " + str((len(self.cola1)))+ " clientes formados"
		print"Sus numeros son "+str((self.cola1))
contador=0
contador2=0	
fila=Cola()	# instancia a la clase-creacion de objeto		
while True:# condicion para ejecutar siempre el menu, hasta que el usuario quiera salir
	
	print"Menu fila Oxxo de hasta 5 personas"
	print"1-Formar un cliente"
	print"2-Atender un cliente"
	print"3-Revisar el estado de la fila"
	print"4-Salir del programa"
	opc=int(input("Ingrese su seleccion "))
	if opc==1:#Dependiendo la seleccion se realiza la la llamada a los metodos mediante el objeto fila
		contador+=1
		os.system('clear')
		fila.encolar(contador)
	elif opc==2:
		os.system('clear')
		fila.desencolar()
	elif opc==3:
		os.system('clear')
		fila.revisar()
	elif opc==4:
		break
	
