def fibo(num) :
	if num<=1 :
		
		return 1
	else:
			return (fibo(num-1) +fibo(num-2))
			
			
			
		
numero= int(input("Numero limite para la serie: "))
for i in range(numero):
	print fibo(i)

