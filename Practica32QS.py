import random
def quicksort(lista):
    
    if lista: # si existe la lista con elementos
        pivot = lista[0]# elije elemento 0 como pivote
        menores = [i for i in lista[1:] if i < pivot] # cada elemento en la lista menor al pivote ira a esa lista
        mayores = [i for i in lista[1:] if i >= pivot]# cada elemento mayor o igual ira a esta
        return quicksort(menores) + [pivot] + quicksort(mayores)# concatena las listas que mediante recursividad realiza el mismo proceso en cada una de ellas y asi hasta finalizar
    else: 
        return lista # lista vacia

wea=[random.randint(0,50) for num in range(50)]
print("lista sin ordenar\n "+str(wea))


print("lista ordenada\n "+str(quicksort(wea)))