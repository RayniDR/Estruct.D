class Nodo(object):# creacion de la clase base para todos los nodos
	def __init__(self, dato=None):
		self.dato=dato
		self.next=None

class ListaLigada(object):#Creacion de la clase para la lista ligada
	def __init__(self):# constructor que crea un nodo raiz usando la instancia de la clase anterior
		self.root=Nodo()

	def push(self,dato):# funcion para anexar un nuevo nodo junto con su elemento
		new_Nodo=Nodo(dato)# Crea un nuevo nodo y le manda el dato que el usuario ingrese
		actual=self.root# Variable para ayudar a recorrer la lista
		while  actual.next!=None:# cuando actual.next!=None significa que aun hay nodos por recorrer
			actual=actual.next
		actual.next=new_Nodo# una vez que se llega al ultimo elemento de la lista agregamos un nuevo nodo

Lista1=ListaLigada()
while True :
 	print("Menu Lista Ligada\n1-Anexar un nuevo nodo\n2-Salir ")
 	opc=int(input("Por favor ingrese su seleccion "))
 	if opc==1:
 		elem=int(input("Ingrese el elemento a anexar "))
 		Lista1.push(elem)
 	if opc==2:
 		break
 	