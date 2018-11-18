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
lista=ListaCircular()
while  True:
	print("**************************\nMenu ListaCircular")
	print("1-Agregar un nuevo nodo\n2-Salir del programa")
	selec=int(input("Por favor ingrese su seleccion: "))
	if selec==1:
		dato=int(input("Ingrese el elemento a agregar: "))
		lista.push(dato)
	if selec==2:
		break