'''The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?'''

n=600851475143
#n=20
list=[0,1]
i=2
while i*i < n:
	if n%i==0:
		list.append(i)
		n=n/i
	i=i+1
list.append(n)
print("Prime factors of 600851475143 are ",list)
print("Largest prime factor is",list[-1])