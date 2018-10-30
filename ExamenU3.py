class Nodo:
	def __init__(self,dato):
		self.dato=dato
		self.next=None
		self.next=None

class ListaDoble:
	def __init__(self):
		self.root=None
	def push(self,dato):
		if self.root is None:
			new_nodo=Nodo(dato)
			new_nodo.prev=None
			self.root=new_nodo
		else:
			new_nodo=Nodo(dato)
			puntero=self.root
			while  puntero.next:
				puntero=puntero.next
			puntero.next=new_nodo
			new_nodo.prev=puntero
			new_nodo.next=None

	def leerIzq(self):
		self.listP=[]
		actual=self.root
		while actual:
			
			self.listP.append(actual.dato)
			actual=actual.next
			
		print(self.listP)
	def leerDer(self):
		lisD=[]
		act2=None
		actual=self.root
		while  actual:
			act2=actual
			actual=actual.next
		while act2:
			
			lisD.append(act2.dato)
			act2=act2.prev
		print(lisD)
	def borrar(self,elem):
		actual=self.root
		while  actual:
			if actual.dato==elem and actual==self.root:
				if actual.next:
					Ntemporal=actual.next
					actual.next=None
					Ntemporal.prev=None
					
					self.root=Ntemporal
			elif actual.dato==elem:
				if actual.next:
					Ntemporal=actual.next
					prev=actual.prev
					prev.next=Ntemporal
					Ntemporal.prev=prev
					actual.next=None
					actual.prev=None
					
				
			actual=actual.next
	def raiz(self):
		actual=self.root
		print("La raiz es: "+ str(actual.dato))

	def extremos(self):
		actual=self.root
		print("El extremo izquiero es : "+ str(actual.dato))
		while actual.next:
			actual=actual.next
		print("El extremo derecho es: ")+str(actual.dato)
	def buscar(self,elem):
		actual=self.root
		cont=0
		while actual:
			
			if actual.dato==elem:
				print("El nodo del elemento ")+str(elem)+(" es: ")+str(cont)
				
				
				actual=None
			elif actual.next==None:
				print("El elemento ")+str(elem)+(" no se encuentra en ningun nodo")
				actual=None
			else:
				actual=actual.next
				cont+=1
			



				
				
							
					

lista=ListaDoble()
lista.push(1)
lista.push(2)
lista.push(3)
lista.push(4)
lista.push(5)
lista.push(6)
lista.push(7)
lista.push(8)
lista.push(9)
lista.leerIzq()
lista.leerDer()
lista.push(10)
lista.push(11)
lista.push(13)
lista.borrar(1)
lista.borrar(8)
lista.leerIzq()
lista.raiz()
lista.extremos()
lista.buscar(7)
lista.buscar(0)
lista.buscar(8)
lista.buscar(1)
