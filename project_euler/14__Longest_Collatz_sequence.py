'''The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been 
proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.'''

def even(x):
	return(x/2)
def odd(x):
	return(3*x + 1)
def Collatz(a):
	b=[a]
	while (a != 1):
		if(a%2==0):
			b.append(even(a))
			a=even(a)
		else:
			b.append(odd(a))
			a=odd(a)
	return b

c=[]
lsize=[]
'''
for i in range(1,10000):
	c.append((Collatz(i)))
	lsize.append((len(c[i-1])))
	#lsize.append()
#print(c)
print(max(lsize))
'''
irange=range(1,1000000)
c=list(map(Collatz,irange))
lsize1=list(map(len,c))
print(max(lsize1))