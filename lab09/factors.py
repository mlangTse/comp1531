'''
NOTE: This exercise assumes you have completed divisors.py
'''

from divisors import divisors

# You may find this helpful
def is_prime(n):
    return list(divisors(n)) == [1, n]

def factors(n):
    '''
    A generator that yields all the prime factors of n. The prime factors are in ascending order with factors repeated as necessary. For example:
    >>> list(factors(36))
    [2, 2, 3, 3]
    '''
    tmp = n
    for i in range(1, n+1):
        if is_prime(i):
            while (tmp/i).is_integer():
                yield i
                tmp = tmp/i
