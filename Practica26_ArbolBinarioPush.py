class Nodo:# crecion de la clase nodo para que sirva de base
	def __init__(self,dato):
		self.dato=dato# almacena el dato que ingresa el usuario
		self.left=None#punteros a la izquierda y derecha
		self.rigth=None
class ArbolBi:# Clase arbol 
	def __init__(self):# constructor que declara la raiz y otro puntero
		self.root=None
		self.P1=None
		
	def push(self,dato):#  funcion para agregar nodos al arbol
		flag=True# bandera para saber cuando ya se agrego el nodo
		if self.root==None:# caso para cuando se agrega la raiz
			New_nodo=Nodo(dato)# instancia a la clase nodo
			self.root=New_nodo# se iguala la raiz al nuevo nodo creado
			self.p1=New_nodo# se pone el puntero en el nuevo nodo creado

		else:# caso para cuando el nuevo nodo no sera la raiz
			while  flag==True:# mientras no se haya agregado el nodo, la condicion se cumple y seguira recorriendo nodos
				
			
				if  self.p1.left==None and self.p1.rigth==None:# Se verifica el nodo actual y sus apuntadores a ambos lados para decirle el estado al usuario
					print("Izquierda y derecha estan disponibles")
				elif   self.p1.left!=None and self.p1.rigth==None:
					print("Izquierda ocupado  con "+str(self.p1.left.dato)+","+" derecha libre")
				elif self.p1.left==None and self.p1.rigth!=None:
					print("Izquierda libre, derecha ocupado con "+str(self.p1.rigth.dato))
				elif self.p1.left!=None and self.p1.rigth!=None:
					print("Izquierda y derecha estan ocupados con "+str(self.p1.left.dato)+" y "+str(self.p1.rigth.dato))
			
				
				
				camino=int(input("1-Ingresar a la izquierda\n2-Ingresar a la derecha: "))# se le pide al usuario hacia que lado ingresar el nodo
				if camino==1 and self.p1.left==None:# Si se elige la izquierda y hay espacion a la izquierda, se agrega el nuevo nodo
					New_nodo=Nodo(dato)
					self.p1.left=New_nodo# se agrega a la izquierda el nodo
					self.p1=self.root# se regresa el puntero a la raiz
					flag=False# se pasa la bandera a false para que pare el ciclo

				elif camino==1:# si se elige la izquierda y no hay espacio, el puntero avanza
					self.p1=self.p1.left

				if camino==2 and self.p1.rigth==None:# Se hace lo mismo pero para el lado derecho
					New_nodo=Nodo(dato)
					self.p1.rigth=New_nodo
					self.p1=self.root
					flag=False
				elif camino==2:
					self.p1=self.p1.rigth
				

				

Arbol=ArbolBi()# instancia de clase arbol

while  True:
	print("********************************************************\nMenu Arbol")
	print("1-Ingresar un nuevo nodo\n2-Salir del programa")
	selec=int(input("Por favor ingrese su seleccion: "))
	if selec==1:
		dato=int(input("Ingrese el dato a ingresar: "))
		Arbol.push(dato)# se manda el dato que el usuario ingrese como parametro
	if selec==2:
		break
	