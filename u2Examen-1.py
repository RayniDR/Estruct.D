def suma(num):
	if num==0:
		return 0
	else:
		return num+ suma(num-1)

print"La suma de los numeros del 1 al 9 es:"+ str(suma(9))
