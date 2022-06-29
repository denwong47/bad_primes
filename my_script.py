from tqdm import tqdm
from timeit import timeit

UPPER_LIMIT_TO_TEST = 1000000
NUMBER_OF_PRIMES    = 78498

# UPPER_LIMIT_TO_TEST = 10
# NUMBER_OF_PRIMES    = 4


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




def _task():
  assert len(list_primes(UPPER_LIMIT_TO_TEST)) == NUMBER_OF_PRIMES

print (f"Calculating all primes up to {UPPER_LIMIT_TO_TEST:,} had taken {timeit(_task, number=1):,.6f}s.")