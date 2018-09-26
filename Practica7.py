index=0
pila=[]
num=0
opc=0
sele=0
opc2=0

def push(index, num):
    if 0<=index<=len(pila):
       
        pila.append(num)
        
        return index+1
    else:
	   print("No se pueden agregar mas datos")
	
def peek():
	opc2=int(input("Ingrese 1 para imprimir toda la pila \n 2 para buscar un elemento \n 3 para el elemento acutal: "))
	if opc2==1:
		print(pila)
	elif opc2==2:
		opc=int(input("Ingrese el numero a buscar: "))
		
		print(pila.index(opc))
	elif opc2==3:
		print(pila[-1])
	
 
def pop():
	if len(pila)>0:
	
		print (pila.pop())
		print(pila)
	else:
		  print("La pila esta vacia")
	
    
      
while index>=0 and index<5:
	
	
	num=int(input("Ingrese un numero "))
	index=push(index,num)
	

def menu(opc):
	if opc==1:
		print (pila)
	elif opc==2:
		peek()
	elif opc==3:
		pop()
while sele!=4:
	sele=int(input(" Ingerese 2 para el metodo peek \n 3 para el metodo pop \n 4 para salir: "))
	menu(sele)
	
