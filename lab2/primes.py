import math


def get_primes(n):
    return [x for x in xrange(1, n) if is_prime(x)]


def is_prime(x):
    for i in xrange(2, int(math.sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True

