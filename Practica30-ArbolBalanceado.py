class Nodo():# clase que sirve como base para cada nodo
	def __init__(self,dato):
		self.dato=dato# se crea el espacio para el daro y para el puntero a izquierda y derecha
		self.left=None
		self.rigth=None

class Arbol_Balanceado():# clase pare crear y enlazar cada uno de los nodos
	def __init__(self):# constructor que crea el puntero para la raiz y otro mas
		self.root=None
		self.p=None

	def push(self,dato):# funcion para crear nuevos nodos y enlazarlos
		flag=True# bandera para saber cuando ya ha insertado un nuevo nodo
		if self.root==None:# caso para cuando se cree la raiz
			New_Nodo=Nodo(dato)# se crea una instancia de la clase nodo, ya con el dato que ingreso el usuario
			self.root=New_Nodo# se iguala la raiz a esa instancia
			self.p=New_Nodo# se pone el puntero en esa innstacia, que es la raiz
		else:
			while flag==True:#MIentras no se haya creado el nuevo nodo
				if dato<self.p.dato and self.p.left==None:# si el dato es menor al dato actual y hay espacio en el puntero de la izq ahi lo guarda
					New_Nodo=Nodo(dato)
					self.p.left=New_Nodo
					self.p=self.root
					flag=False

				elif dato<self.p.dato and self.p.left!=None:# si el dato es menor pero no hay espacio solo mueve el puntero a la izquierda
					self.p=self.p.left

				elif dato>=self.p.dato and self.p.rigth==None:# si el dato es mayor o igual, hace lo mismo pero hacia el lado izquiero
					New_Nodo=Nodo(dato)
					self.p.rigth=New_Nodo
					self.p=self.root
					flag=False

				elif dato >= self.p.dato and self.p.rigth!=None:
					self.p=self.p.rigth
					
	def impr(self,tipo):# funcion de apoyo solamente para facilitar el pase de parametros a los recorridos
		wea=self.root# se iguala una variable a la raiz
		if tipo== "I":
			print(self.Inorden(wea))
		if tipo=="Pre":
			print(self.Preorden(wea))
		if tipo=="Pos":
			print(self.Postorden(wea))
	def Inorden(self,nodo):
		
		if nodo :# si el nodo actual existe usara la recursividad para recorrer los nodos en el orden correcto, dependiendo del tipo de recorrido
			self.Inorden(nodo.left)
			print((nodo.dato))

			self.Inorden(nodo.rigth)
	def Preorden(self,nodo):
		if nodo:
			print(nodo.dato)
			self.Preorden(nodo.left)
			self.Preorden(nodo.rigth)
	def Postorden(self,nodo):
		if nodo:
			self.Postorden(nodo.left)
			self.Postorden(nodo.rigth)
			print(nodo.dato)

Arbolito=Arbol_Balanceado()

while True:
	print("****************************\nMenu Arbol Balanceado")
	print("1-Ingresar un nuevo nodo\n2-Impresion en Inorden\n3-Impresion en Preorden\n4-Impresion en Postorden\n5-Salir del programa")
	selec=int(input("Por favor ingrese su seleccion: "))
	if selec==1:
		elem=int(input("Ingrese el numero para agregar: "))
		Arbolito.push(elem)# se pasa el numero que ingreso el usuario como parametro
	if selec==2:# se manda llamar a la funcion de apoyo para la impresion, y se indica cual de los recorridos hara
		Arbolito.impr("I")
	if selec==3:
		Arbolito.impr("Pre")
	if selec==4:
		Arbolito.impr("Pos")
	if selec==5:
		break