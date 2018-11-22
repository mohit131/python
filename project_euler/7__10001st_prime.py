'''By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?'''
from math import sqrt,floor, ceil

def check_prime(num):
	for i in range(2,floor(sqrt(num))+1):
		if num % i  == 0:
			#print('not prime')
			return False
	return True

a=2	
prime_list=[]
while len(prime_list)<10001:
	check=check_prime(a)
	if check==True:
		prime_list.append(a)
	a+=1
print(prime_list[-1])