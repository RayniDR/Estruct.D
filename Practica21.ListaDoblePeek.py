class Nodo:# clase que sirve de base para crear los nodos de la lista
	def __init__(self,dato):
		self.dato=dato# guarda el dato y el puntero al nodo anterior y siguiente
		self.next=None
		self.prev=None

class ListaDoble: #clase para enlazar y crear los nodos
	def __init__(self):
		self.root=None
	def push(self,dato):# funcion para agregar y enlazar nodos
		if self.root is None:# caso para crear la raiz
			new_nodo=Nodo(dato)# se almacenan los datos en una variable temporal
			new_nodo.prev=None# el puntero al prev va a None porque es la raiz
			self.root=new_nodo# se asigna a la raiz esos datos
		else:# caso para cuando no es la raiz
			new_nodo=Nodo(dato)
			puntero=self.root# se pone un puntero en la raiz
			while  puntero.next:# mientras aun haya nodos por recorrer
				puntero=puntero.next# mueve el puntero al siguiente nodo
			puntero.next=new_nodo# cuando acaba de recorrer pone al ultimo puntero .next el nuevo nodo, con lo que lo enlaza tambien
			new_nodo.prev=puntero# al nuevo nodo le pone un puntero al nodo anterior
			new_nodo.next=None#  el .next va a None porque es el ultimo nodo de la lista
	def peek(self,selec):
		cont=0
		actual=self.root
		if selec==1:#condicion para imprimir toda la lista
			self.impresion=[]
			actual=self.root
			while actual:
				self.impresion.append(actual.dato)
				actual=actual.next
			print(self.impresion)
		elif selec==2:# condicion para imprimir la raiz de la lista
			print("La raiz es "+ str (self.root.dato))
		elif selec==3:# condicion para imprimir el ultimo elemento de la lista
			while actual.next:
				actual=actual.next
			print("El ultimo elemento es "+str(actual.dato))
		elif selec==4:# condicion para imprimir el indice de un elemento
			cont=0# se crea un contador que es el que guarda el # de indice
			num=int(input("Ingrese el elemento a buscar "))# se pide el numero a buscar
			while actual:# mientras aun existan nodos
			
				if actual.dato==num:# si el dato del nodo actual es igual al dato que se busca, imprime el contador
					print("El nodo del elemento ")+str(num)+(" es: ")+str(cont)
				
				
					actual=None
				elif actual.next==None:# si ya no hay nodos, imprime que no existe el elemento en la lista
					print("El elemento ")+str(num)+(" no se encuentra en ningun nodo")
					actual=None
				else:# si aun hay nodos solo pasa al siguiente nodo y aumenta el contador
					actual=actual.next
					cont+=1


lista=ListaDoble()

while  True:
	print("*****************\nMenu Lista Doblemente enlazada")
	print("1-Ingresar un nuevo nodo\n2-Metodo Peek\n3-Salir del programa")
	selec=int(input("Por favor ingrese su selccion: "))
	if selec==1:
		elem=int(input("Ingrese el elemento: "))
		lista.push(elem)# se le mande el elemento que el usuario ingresa
	if selec==2:
		print("1-Imprimir toda la lista\n2-Imprimir la raiz de la lista\n3-Imprimir el ultimo elemento\n4-Buscar el indice de un elemento")
		opc=int(input("Por favor ingrese su seleccion: "))
		if opc==1 or opc==2 or opc==3 or opc==4:
			lista.peek(opc)
		else:
			print("Opcion no valida")
	if selec==3:
		break
		