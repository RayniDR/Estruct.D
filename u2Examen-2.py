def potencia(n):
	if n==0:
		return 1
	else:
		return 2* (potencia(n-1))

selec=int(input("Ingrese la potencia a la que desea elevar el 2 :"))
print"El resultado es: " +str(potencia(selec))
