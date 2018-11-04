class Nodo:
	def __init__(self,dato):
		self.dato=dato
		self.left=None
		self.rigth=None
class ArbolBi:
	def __init__(self):
		self.root=None
		self.P1=None
		self.P2=None
	def push(self,dato):
		flag=True
		if self.root==None:
			New_nodo=Nodo(dato)
			self.root=New_nodo
			self.p1=New_nodo

		else:
			while  flag==True:
				
			
				if  self.p1.left==None and self.p1.rigth==None:
					print("Izquierda y derecha estan disponibles")
				elif   self.p1.left!=None and self.p1.rigth==None:
					print("Izquierda ocupado  con "+str(self.p1.left.dato)+","+" derecha libre")
				elif self.p1.left==None and self.p1.rigth!=None:
					print("Izquierda libre, derecha ocupado con "+str(self.p1.rigth.dato))
				elif self.p1.left!=None and self.p1.rigth!=None:
					print("Izquierda y derecha estan ocupados con "+str(self.p1.left.dato)+" y "+str(self.p1.rigth.dato))
			
				
				
				camino=int(input("1-Ingresar a la izquierda\n2-Ingresar a la derecha: "))
				if camino==1 and self.p1.left==None:
					New_nodo=Nodo(dato)
					self.p1.left=New_nodo
					self.p1=self.root
					flag=False

				elif camino==1:
					self.p1=self.p1.left

				if camino==2 and self.p1.rigth==None:
					New_nodo=Nodo(dato)
					self.p1.rigth=New_nodo
					self.p1=self.root
					flag=False
				elif camino==2:
					self.p1=self.p1.rigth
	def impr(self,tipo):
		wea=self.root
		if tipo== "I":
			print(self.Inorden(wea,""))
		if tipo=="Pre":
			print(self.Preorden(wea))
	def Inorden(self,nodo,string):
		
		if nodo :
			self.Inorden(nodo.left,string)
			print((nodo.dato))

			self.Inorden(nodo.rigth,string)
	def Preorden(self,nodo):
		if nodo: # si el nodo actual es diferente de null
			print(nodo.dato)# comienza imprimiendo la raiz
			self.Preorden(nodo.left)# recorre el lado izquierdo usando la recursividad
			self.Preorden(nodo.rigth)# recorre el lado derecho

					

Arbol=ArbolBi()


while  True:
	print("********************************************************\nMenu Arbol")
	print("1-Ingresar un nuevo nodo\n2-Impresion en Inorden\n3-Impresion en Preorden\n4-Salir del programa")
	selec=int(input("Por favor ingrese su seleccion: "))
	
	if selec==1:
		dato=int(input("Ingrese el dato a ingresar: "))
		Arbol.push(dato)
		
	if selec==2:
		Arbol.impr("I")
	if selec==3:
		Arbol.impr("Pre")
	if selec==4:
		break
	