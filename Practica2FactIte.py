def fact(n):
    factorial_total = 1
    while n > 1:
        factorial_total *= n
        n -= 1
    return factorial_total
num=int(input("Numero a calcular el factorial: "))	
print fact(num)
