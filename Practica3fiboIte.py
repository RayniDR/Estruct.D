def fib(n):
    a = 1
    b = 0
    for i in range(n):
        a, b = b, a + b
    return b  
		
numero= int(input("Numero limite para la serie: "))
for i in range(numero+1):
	print fib(i)

