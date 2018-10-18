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
            
	def pop(self):# funcion para sacar elementos
		if self.cola[0]!=0:# verifica que el indice 0 no sea 0, o sea no este vacia la cola
			print("Ha salido "+str(self.cola[0]))# imprime el elemento que sacara
			for i in range(0,self.maxT-1):# ciclo para recorrer los elemento 1 indice
				self.cola[i]=self.cola[i+1]
			self.cola[self.maxT-1]=0#
			self.rear=self.rear-1
		else:
			print("La cola ya esta vacia")
			self.rear=0
	def peek(self,selec):
		if selec== 1:
			print(self.cola)# imprime toda la cola
		elif selec==2:
			print(self.cola[self.rear-1])# imprime el ultimo elemento, uso -1 porque el rear ya aumento antes para poder asignar un nuevo elemento
		elif selec==3:
			print(self.cola[0])# imprime el primer elemento que entro
		elif selec==4:
			num=int(input("Ingrese el numero a buscar "))
			#[i for i,x in enumerate([1,2,3,2]) if x==2] # => [1, 3]
			print([i for i, x in enumerate(self.cola) if x==num])# busca el indice de el elemento que el usuario pida

tam=int(input("Ingrese el tamano de la cola "))	
cola=Cola(int(tam))# creacion de objeto de la clase Cola con parametro
while True:# ciclo para ejecutar el menu
	print("*****************")
	print("Menu Cola")
	print("1-Agregar un elemento a la cola")
	print("2-Sacar un elemento")
	print("3-Ejecutar metodo Peek")
	print("4-Salir del programa")
	selec=int(input("Por favor, ingrese su seleccion "))
	if selec==1:
		elemento=int(input("Ingrese el elemento a agregar "))
		cola.push(elemento)# le manda el elemento a la funcion push
	if selec==2:
		cola.pop()
		
	if selec==3:
		print("************************************")
		print("Menu Peek")
		print("1-imprimir toda la cola")
		print("2- Imprimmir el ultimo elemento")
		print("3-imprimir el primer elemento")
		print("4-buscar el indice de un elemento")
		opc=int(input("Por favor ingrese su seleccion "))
		cola.peek(opc)
	if selec==4:
		break
	
	
