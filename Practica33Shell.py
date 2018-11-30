import random
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
wea=[random.randint(0,50) for num in range(50)]
print("lista sin ordenar\n "+str(wea))

shellSort(wea)
print("lista ordenada\n "+str(wea))