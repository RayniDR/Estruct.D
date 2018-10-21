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

tam=int(input("Ingrese el tamano de la cola circular "))	
cola=ColaCircular(int(tam))	# creacion del objeto cola con asignacion de parametro
cola.crear(int(tam))	
while True:# se inicia el menu
	print("*************")
	print("1-Agregar un elemento a la cola")
	print("2-Salir del programa")
	opc=int(input("Por favor ingrese su seleccion "))
	if opc==1:
		ele=int(input("Ingrese el numero a agregar "))
		cola.encolar(ele)# se manda el elemento como parametro mediante la instancia de objeto
	elif opc==2:
		break	# opcion para salir del programa
