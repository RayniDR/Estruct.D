
def fact(num):
	if num==1:
		return 1
		
	else:
		        return num*fact(num-1)
			      
num=int(input("Numero a calcular el factorial: "))	
print(fact(num))	
