class Cola:
	def __init__(self,maxT):# constructor de la clase, crea la cola en 0 segun el tamano del usuario
		self.cola=[]
		self.rear=0
		self.maxT=maxT
		for i in range(0,self.maxT):# ciclo para llenar la cola con 0
			self.cola.append(0)
		
		
	def push(self, elemento):# funcion para agreagar elementos
		if self.cola[self.maxT-1]==0:# verifica que el el ultimo indice sea igual a 0
			self.cola[self.rear]=elemento# agrega el elemento en el rear
			print("Ha ingresado "+str(elemento))
			print(self.cola)
			self.rear =self.rear+1# aumenta el rear en 1
		else:# si la cola esta llena solo imprime algo
			print("La cola esta llena")

tam=int(input("Ingrese el tamano de la cola "))	
cola=Cola(int(tam))# creacion de objeto de la clase Cola con parametro
while True:# ciclo para ejecutar el menu
	print("*****************")
	print("Menu Cola")
	print("1-Agregar un elemento a la cola")
	print("2-Salir del programa")
	selec=int(input("Por favor, ingrese su seleccion "))
	if selec==1:
		elemento=int(input("Ingrese el elemento a agregar "))
		cola.push(elemento)# le manda el elemento a la funcion push
	if selec==2:
		break
	
	
