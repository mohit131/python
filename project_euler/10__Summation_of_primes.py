'''The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.'''

number=2000000

from sympy import primerange

prime_numbers=list(primerange(1,number))
print(sum(prime_numbers))