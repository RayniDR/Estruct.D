
num=0
def pri(numero):
		 
	 if numero<=100:
	   
	   numero+1
	   print(numero)
	   pri(numero+1)
	 else:
		 print("Fin")


def fact(num):
	if num==1:
		return 1
		
	else:
		        return num*fact(num-1)
def fibo(num) :
	if num<=1 :
		
		return 1
	else:
			return (fibo(num-1) +fibo(num-2))

def menu(op):
	if op==1:
		pri(0)
	elif op==2:
		num=int(input("Numero a calcular el factorial: "))
		print(fact(num))	
	elif op==3:
		numero= int(input("Numero limite para la serie: "))
		for i in range(numero):
			print fibo(i)
	else:
		opc=int(input(" 1 para imprimir 100 primeros numeros, 2 para factorial, 3 fibonachi: " ))
		menu(opc)
		
opc=int(input(" 1 para imprimir 100 primeros numeros, 2 para factorial, 3 fibonachi" ))
menu(opc)
