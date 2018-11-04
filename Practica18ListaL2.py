class Nodo(object):# creacion de la clase base para todos los nodos
	def __init__(self, dato=None):
		self.dato=dato
		self.next=None

class ListaLigada(object):#Creacion de la clase para la lista ligada
	def __init__(self,dato):# constructor que crea un nodo raiz usando la instancia de la clase anterior
		self.root=Nodo(dato)#Se le agrega el primer dato a la raiz
		

	def push(self,dato):# funcion para anexar un nuevo nodo junto con su elemento
		new_Nodo=Nodo(dato)# Crea un nuevo nodo y le manda el dato que el usuario ingrese
		actual=self.root# Variable para ayudar a recorrer la lista
		
		while  actual.next!=None: # cuando actual.next!=None significa que aun hay nodos por recorrer
			actual=actual.next
		actual.next=new_Nodo# una vez que se llega al ultimo elemento de la lista agregamos un nuevo nodo

	def peek(self,sp):
		if sp==1:# condicion para imprimir toda la lista
			listPrint=[]# crea una lista para guardar los datos e imprimirlos ahi
			actual=self.root#pone un puntero en la raiz
			listPrint.append(actual.dato)# agrega a la lista donde este el puntero, que es en la raiz
			while  actual.next!=None:# ciclo que se ejecuta hasta que no haya mas nodos
				actual=actual.next#pone el puntero en el siguiente nodo
				listPrint.append(actual.dato)#agrega a la lista donde este el puntero
				
			return listPrint#regresa la lista
		if sp==2:# condicion para imprimir la raiz
			listPrint=[]#crea una lista para guardar el elemento
			actual=self.root#Pone un puntero en la raiz
			listPrint.append(actual.dato)#agrega el elemento a la lista
			return listPrint# regresa la lista
		if sp==3:
			listPrint=[]# crea una lista para guardar el elemento
			actual=self.root# pone un puntero en la raiz
			while  actual.next!=None:# recorre los nodos hasta llegar al final
				actual=actual.next
			listPrint.append(actual.dato)# una vez que esta en el ultimo nodo, lo agrega a la lista
			return listPrint# retorna la lista
		if sp==4:
			listPrint=[]# crea una lista para guardar todos los elementos
			actual=self.root# Pone un puntero en la raiz
			listPrint.append(actual.dato)# agrega el elemento de la raiz a la lista
			while actual.next!=None:# se ejecuta hasta recorrer todos los nodos
				actual=actual.next# avanza el puntero
				listPrint.append(actual.dato)# agrega el elemento del puntero a la lista
			num=int(input("Ingrese el elemento a buscar: "))
			print([i for i, x in enumerate(listPrint)if x==num])# imprime el indice del elemento que busca el usuario



dato=int(input("Ingrese el primer dato de la lista "))
Lista1=ListaLigada(int(dato))
while True :
 	print("Menu Lista Ligada\n1-Anexar un nuevo nodo\n2-Metodo peek\n3-Salir ")
 	opc=int(input("Por favor ingrese su seleccion "))
 	if opc==1:
 		elem=int(input("Ingrese el elemento a anexar "))
 		Lista1.push(elem)
 	if opc==2:
 		print("Menu peek\n1-Imprimir toda la lista\n2-Imprimir la raiz o primer elemento\n3-Imprimir el ultimo elemento\n4-Buscar el indice de un elemento\n5-Salir")
 		sp=int(input("Por favor ingrese su seleccion: "))
 		if sp!=4:
 			print (Lista1.peek(sp))
 		
 		if sp==4:
 			Lista1.peek(sp)

 	if opc==5:
 		break
 	
