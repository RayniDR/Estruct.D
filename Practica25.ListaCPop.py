class Nodo():# clase que sirve de molde para cada nodo
	def __init__(self,dato):
		self.next=None
		self.dato=dato
class ListaCircular():# clase para crear y enlazar los nodos
	def __init__(self):# crea una raiz vacia
		self.root=None

	def push(self,dato):# funcion para agregar lo que recibe en sus parametros
		if not self.root:# si la raiz de la lista no existe
			self.root=Nodo(dato)# crea un nuevo nodo en la raiz
			self.root.next=self.root# pone el puntero siguiente hacia si mismo, por ser circular la lista y ser el unico nodo existente
		else:# si ya existe la raiz
			new_nodo=Nodo(dato)# variable que almacena el nuevo nodo a agregar
			actual=self.root# pone un puntero en la raiz
			while actual.next!=self.root:# mientras el next del puntero no apunte a la raiz, o sea no sea el ultimo nodo
				actual=actual.next# avanza en uno el punteor
			actual.next=new_nodo# cuando acaba de recorrer la lista pone el next del ultimo nodo al nuevo nodo
			new_nodo.next=self.root# pone el puntero del nuevo nodo a la raiz

	def peek(self,selec):
		cont=0
		actual=self.root
		if selec==1:#condicion para imprimir toda la lista
			self.impresion=[]
			actual=self.root
			while actual:
				self.impresion.append(actual.dato)
				actual=actual.next
				if actual==self.root:
					break
			print(self.impresion)
		elif selec==2:# condicion para imprimir la raiz de la lista
			print("La raiz es "+ str (self.root.dato))
		elif selec==3:# condicion para imprimir el ultimo elemento de la lista
			while actual.next:
				temp=actual# guarda el nodo antes de avanzar de nuevo a la raiz para poder imprimirlo
				actual=actual.next
				if actual==self.root:
					break
			print("El ultimo elemento es "+str(temp.dato))
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
	def pop(self,elem):# Funcion para borrar elementos recibe como parametro el elemento que el usuario elija borrar
		actual=self.root# pone un puntero en la raiz
		if self.root.dato==elem:# si el elemento a borrar es la raiz
			while actual.next!=self.root:# mientras el elemento siguiente no sea la raiz
				actual=actual.next# avanza un nodo
			actual.next=self.root.next# remplaza el puntero next del ultimo nodo, de la raiz al .next de la raiz
			self.root=self.root.next# remplaza la raiz por su elemento siguiente
			
		else:# si el nodo a borrar no es la raiz
			prev=None# variale auxiliar para guardar el nodo anterior
			while actual.next!=self.root:# mientras el nodo siguiente no sea la raiz
				prev=actual# guarda el nodo anterior
				actual=actual.next# avanza un nodo
				if actual.dato==elem:# si el nodo actual es el nodo a borrar
					prev.next=actual.next# el puntero .next del nodo anterior avanza un nodo
					actual=actual.next# el nodo actual pasa a ser el nodo siguiente
					break


		
lista=ListaCircular()
while  True:
	print("**************************\nMenu ListaCircular")
	print("1-Agregar un nuevo nodo\n2-Metodo Peek\n3-Borrar un elemento\n4-Salir del programa")
	selec=int(input("Por favor ingrese su seleccion: "))
	if selec==1:
		dato=int(input("Ingrese el elemento a agregar: "))
		lista.push(dato)
	if selec==2:
		print("1-Imprimir toda la lista\n2-Imprimir la raiz de la lista\n3-Imprimir el ultimo elemento\n4-Buscar el indice de un elemento")
		opc=int(input("Por favor ingrese su seleccion: "))
		if opc==1 or opc==2 or opc==3 or opc==4:
			lista.peek(opc)
		else:
			print("Opcion no valida")
	if selec==3:
		elem=int(input("Ingrese el elemento a borrar"))
		lista.pop(elem)

	if selec==4:
		break