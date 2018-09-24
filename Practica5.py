index=0
pila=[]
num=0
opc=0

def push(index, num):
    if 0<=index<=len(pila):
       
        pila.append(num)
        
        return index+1
    else:
	   print("No se pueden agregar mas datos")
	
def peek():
	
    opc=int(input("Ingrese el indice a imprimir: "))
    print(pila[opc])
        
    
        
while index>=0 and index<5:
	
	num=int(input("Ingrese un numero "))
	index=push(index,num)
    
print (pila)
peek()
