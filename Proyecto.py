import random
from time import time
timeburf=0# variables para almacenar el tiempo total de cada uno
contf=0
timeQSf=0
timeShellf=0
timeMergef=0
timesortf=0
def burbuja(lista1):
	i=0
	while i<len(lista1)-1:# mientras i sea menor al largo de la lista -1
		if lista1[i]>lista1[i+1]:# si el dato actual es mayor que el dato siguiente

			x=lista1[i]# guarda el dato actual
			lista1[i]=lista1[i+1]#guarda el dato siguiente en el indice anterior
			lista1[i+1]=x# guarda el dato anterior en el indice siguiente
			i=0
			continue
		else:# si el dato actual no es mayor que el siguiente no los intercamia
			i+=1
	return lista1
def quicksort(lista):
    
    if lista: # si existe la lista con elementos
        pivot = lista[0]# elije elemento 0 como pivote
        menores = [i for i in lista[1:] if i < pivot] # cada elemento en la lista menor al pivote ira a esa lista
        mayores = [i for i in lista[1:] if i >= pivot]# cada elemento mayor o igual ira a esta
        return quicksort(menores) + [pivot] + quicksort(mayores)# concatena las listas que mediante recursividad realiza el mismo proceso en cada una de ellas y asi hasta finalizar
    else: 
        return lista # lista vacia
def shellSort(arr): 
  
    n = len(arr) 
    gap = n//2# dara saltos con el tamano de la mitad de la lista
  
   
    while gap > 0: # mientras gap no llegue a 0, osea aun haya comparaciones por hacer
  
        for i in range(gap,n): # para cada elemento entre gap y el largo total
  
 
            #agrega [i]a los elemtos que han sido acomodados
            temp = arr[i] # guarda el elemento actual
  
            # Busca la correcta posicion para [i]
            j = i # copia ese elemento
            while  j >= gap and arr[j-gap] >temp: 
                arr[j] = arr[j-gap] 
                j -= gap 
  
            
            arr[j] = temp # pone al elemento guardado en su posicion correcta
        gap //= 2# reduce gap a la mitad
def mergeSort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2 # mitad de la lista
        L = arr[:mid] # crea la lista en dos mitades diferentes, izquierda y derecha
        R = arr[mid:] 
  
        mergeSort(L) # vuelve a llamar la funcion para cada una de las partes hasta que queden solo listas de 1 elemento
        mergeSort(R) 
  
        i = j = k = 0# variables auxiliares
          
        # Copia los datos en listas temporales
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: # verifica cual de las dos listas tiene el elemento menor en esa posicion y ese es el que agrega 
                arr[k] = L[i] # de esa forma los elementos entran ordenados a la lista de mayor tamano
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
          
        # ultima pasada
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1

for i in range(0,30):
	lista=[random.randint(0,200) for num in range(200)]
	#ejecuciones y medidores BurbleS
	t0bur=time()
	burbuja(lista)
	t2bur=time()
	timebur=t2bur-t0bur
	timeburf+=timebur
	# ejecuciones y medidores QS
	t0QS=time()
	quicksort(lista)
	t1QS=time()
	timeQS=t1QS-t0QS
	timeQSf+=timeQS
	# Ejecuciones y Medidores Shell
	t0Shell=time()
	shellSort(lista)
	t1Shell=time()
	timeShell=t1Shell-t0Shell
	timeShellf+=timeShell
	# Ejecuciones y mediciones Merge
	t0Merge=time()
	mergeSort(lista)
	t1Merge=time()
	timeMerge=t1Merge-t0Merge
	timeMergef+=timeMerge
	# ejecucion sort python
	t0sort=time()
	lista.sort()
	t1sort=time()
	timesort=t1sort-t0sort
	timesortf+=timesort
promQS=timeQSf/30
promBur=timeburf/30
promSh=timeShellf/30
promMe=timeMergef/30
promS=timesortf/30

print("El tiempo de ejecucion para el Quicksort fue:  "+str(promQS))
print("El tiempo de ejecucion para el Burblesort fue: "+str(promBur))
print("El tiempo de ejecucion para el shellSort fue:  "+str(promSh))
print("El tiempo de ejecucion para el MergeSort fue:  "+str(promMe))
print("El tiempo de ejecucion para la funcion sort fue: "+str(timesortf))
print("******************************")
print("Las mediciones se realizaron con 30 arreglos diferentes, cada uno en los diferentes algoritmos.\nSe toma el promedio de las 30 ejecuciones")
print("Arreglos con 200 elementos cada uno, todos generados aleatoriamente")




