########### Problem 3 ############
import math
primes = [2]
prime_factors = []

#finds prime numbers
def prime(n):
  if n < 2:
    isPrime = False
  for i in range(3, int(math.sqrt(n)), 2):
    if n % i == 0:
      isPrime = False
    else:
      isPrime = True
      if isPrime:
        primes.append(i)
  print (primes)

#finds factors in primes list
def factors(n):
  for i in primes:
    if n % i == 0:
      prime_factors.append(i)
  print (factors)

#finds highest factor in factor list
def highest(n):
  answer = max(prime_factors)
  print (answer)

prime(13195)
factors(13195)




