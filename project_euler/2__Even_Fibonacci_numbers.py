'''Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.'''

def fibonaci(n):
	if n==1:
		return 1
	if n==2:
		return 2		
	else:
		return fibonaci(n-2)+fibonaci(n-1)

n=1
Sum=0
while Sum<4000000:
	if fibonaci(n)%2==0:
		Sum=Sum+fibonaci(n)
	n+=1
print(Sum)