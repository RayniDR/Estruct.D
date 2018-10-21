class ColaCircular:
	def __init__(self,maxT):#Constructor de la clase en la que se inicia la cola, su frente y final
		self.cola=[]
		self.front=0
		self.rear=0
		self.maxT=maxT# tambien se recibe el tamano max de la cola
		
	def crear(self,maxT):# funcion para llenar la cola con 0, segun el tamano ingresado
		for i in range(0,maxT):
			self.cola.append(0)
	
	def encolar(self,elemento):# funcion para agregar elementos a la cola
		if self.rear!=(self.front):# verifica que el frente no sea igual que el final
			self.cola[self.rear]=elemento# asigna el elemento al final de la cola
			print("Ha entrado "+str(self.cola[self.rear]))
			self.rear=(self.rear+1) % self.maxT# cambia el valor del final sumandole 1, y haciendo que al llegar a ser igual al maxT se regrese a 0		
		elif self.cola[self.rear]==0:# caso para que pueda ingresar un valor por primera vez
			self.cola[self.rear]=elemento
			print("Ha entrado "+str(self.cola[self.rear]))
			self.rear=(self.rear+1) %self.maxT
			
		else:# si la cola esta llena solo imprime algo
			print("La cola esta llena")
			
	def desencolar(self):# funcion para sacar elementos
		if self.cola[self.front]!=0:# verifica que la cola no este vacia ya
			print("Ha salido "+ str(self.cola[self.front]))# primero imprime el elemento que eliminara, que es el que esta en el front
			self.cola[self.front]=0# Ahora asigna el 0 al front
			self.front=(self.front+1)%self.maxT# aumenta el front en 1 posicion y cuando llegue a ser == a maxT la regresa a 0
		else:# si la cola esta vacia solo imprime algo
			print("La cola esta vacia")

tam=int(input("Ingrese el tamano de la cola "))	
cola=ColaCircular(int(tam))	# creacion del objeto cola con asignacion de parametro
cola.crear(int(tam))
while True:# se inicia el menu
	print("*************")
	print("1-Agregar un elemento a la cola")
	print("2-Sacar un elemento de la cola")
	print("3-Salir del programa")
	opc=int(input("Por favor ingrese su seleccion "))
	if opc==1:
		ele=int(input("Ingrese el numero a agregar "))
		cola.encolar(ele)# se manda el elemento como parametro mediante la instancia de objeto
	elif opc==2:
		cola.desencolar()
	elif opc==3:
		break	# opcion para salir del programa
