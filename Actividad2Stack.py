index=0
pila=[]
num=0
opc=0
sele=0

def push(index, num):
    if 0<=index<=len(pila):
       
        pila.append(num)
        
        return index+1
    else:
	   print("No se pueden agregar mas datos")
	
def peek():
	
    opc=int(input("Ingrese el indice a imprimir: "))
    print(pila[opc])
 
def pop():
	
	print (pila.pop())
	print(pila)
    
        
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
	sele=int(input(" Ingrese 1 para impriir la pila \n 2 para seleccionar un elemento \n 3 para pop \n 4 para salir: "))
	menu(sele)
	
