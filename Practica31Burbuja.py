
import random
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


lista=[random.randint(0,20)for i in range(20)]
print("Lista original:\n "+str(lista))
burbuja(lista)
print("Lista ordenada: \n"+str(lista))
