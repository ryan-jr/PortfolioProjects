import math

def primeCheck(size):
  """Returns a list of prime numbers using the sieve of Eratosthenes
  
  """
  # Intializing the sieve
  sieve = [True] * size
  sieve[0] = False
  sieve[1] = False
  
  for i in range(2, int(math.sqrt(size)) + 1):
    pointer = i * 2 
    while pointer < size:
      sieve[pointer] = False
      pointer += i
      
  primes = []
  for i in range(size):
    if sieve[i] == True:
      primes.append(i)
  print(len(primes))
  return primes