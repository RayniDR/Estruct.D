import random
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
wea=[random.randint(0,50) for num in range(50)]
print("Original\n"+str(wea))
mergeSort(wea)
print("Ordenado\n "+str(wea))