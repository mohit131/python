'''The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.'''

import numpy

a=numpy.arange(1,101)
sum_a=numpy.sum(a)
b=list(map(lambda x: x*x, a))
sum_b=numpy.sum(b)
print((sum_a * sum_a) - sum_b) 