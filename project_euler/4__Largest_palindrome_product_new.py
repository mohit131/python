'''A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.'''

#function to reverse a number
def revers(x):
	b=str(x)[::-1]
	return int(b) 
	
	
import numpy
import time

t1=time.time()
a=numpy.arange(100,1000) # range of numbers from 100 to 999
#print(a)
b=numpy.array([a])
c=b.T # transpose of vector a
#print(c)
product_matrix=a*c # this is the product of numbers from 100 to 999 in matrix form
#print(product_matrix)
product_array=product_matrix.reshape(1,product_matrix.shape[0]*product_matrix.shape[1]) #reshaping matrix into a vector

product_array=product_array[0] # vector from previous step is in form [[]], this will convert it to list []
product_array=list(product_array)
with open('product_array.txt','w') as tasks:
	print(product_array,file=tasks)

t2=time.time()

# loop to check if number and its reverse are same
reverse_num=list(map(revers,product_array))

with open('reverse.txt','w') as tasks:
	print(reverse_num,file=tasks)
#print(reverse_num)
rev=sorted(list(set(product_array).intersection(set(reverse_num))))
with open('reverse_intersection.txt','w') as tasks:
	print(rev,file=tasks)

# reverse_num: list of palindrome numbers
#reverse_num.sort()
t3=time.time()
print(rev[-1])
print(t2-t1)
print(t3-t1)