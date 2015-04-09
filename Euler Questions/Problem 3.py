########### Problem 3 ############
import math
primes = [2]
prime_factors = []

#finds prime numbers
def prime(n):
  if n < 2:
    isPrime = False
  for i in range(3, int(math.sqrt(n)), 2):
    #The divisibility of n by i says more about the
    # prime-ness of n than it does about the prime-ness
    # of i.  If n is divisible by any of the numbers in
    # the above range, then n is not prime, but it
    # doesn't follow that i is prime if the division is
    # not even. You'll need to perform a different test
    # on each number in the range (nice job skipping the
    # even numbers, btw) to test their prime-ness.
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
  #I think this should be print(prime_factors)
  print (factors)

#finds highest factor in factor list
def highest(n):
  answer = max(prime_factors)
  print (answer)

prime(13195)
factors(13195)




