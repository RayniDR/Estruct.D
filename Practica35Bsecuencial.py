import random
def sec(arr,elem):
	cont=0
	a=len(arr)
	flag=False
	for num in range(0,a):
		if elem==arr[num]:
			print("El elemento "+str(elem) +" esta en el indice "+str(cont))
			flag=True
		cont+=1
	if flag==False:
		print("El elemento "+str(elem) +" no se encuentra en la lista")


wea=[random.randint(0,10) for num in range(10)]
print("lista "+str(wea))
elem=int(input("Ingrese el elemento a buscar: "))
sec(wea,elem)
