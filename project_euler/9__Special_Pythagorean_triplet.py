'''A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.'''


for m in range(1,5000):
	for n in range(1,500):
		if m>n:
			a=m*m - n*n
			b= 2 * m * n
			c=m*m + n*n
			sum_ab=a*a + b*b
			sum_c=c*c
			if sum_ab == sum_c:
				if a+b+c==1000:
					print(a,b,c,a+b+c,a*b*c)
		else:
			break