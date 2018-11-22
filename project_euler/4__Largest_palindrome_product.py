'''A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.'''

#function to reverse a number
def reverse_number(x):
	Number=x
	a=Number
	Reverse=0
	while(Number>0):
		Reminder=Number % 10
		Reverse = (Reverse*10) + Reminder
		Number= Number//10
	return Reverse 
	
	
import numpy
a=numpy.arange(100,1000) # range of numbers from 100 to 999
b=numpy.array([a])
c=b.T # transpose of vector a
product_matrix=a*c # this is the product of numbers from 100 to 999 in matrix form
product_array=product_matrix.reshape(1,product_matrix.shape[0]*product_matrix.shape[1]) #reshaping matrix into a vector

product_array=product_array[0] # vector from previous step is in form [[]], this will convert it to list []
reverse_num=[]

# loop to check if number and its reverse are same
for i in product_array:
	if i==reverse_number(i):
		reverse_num.append(i)

# reverse_num: list of palindrome numbers
reverse_num.sort()
print(reverse_num[-1])	