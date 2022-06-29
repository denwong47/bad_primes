def is_prime(c):
  for i in range(2, c):
    if (c % i == 0): return False
  return True
def list_primes(u):
  l = []
  for i in range(2, u+1):
    if (is_prime(i)):
      l.append(i)
  return l