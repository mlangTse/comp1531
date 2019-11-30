def divisors(n):
    '''
    Given some number n, this generator yields all positive integer divisors of n in ascending order. For example:
    >>> list(divisors(12))
    [1, 2, 3, 4, 6, 12]
    '''
    for i in range(1, n+1):
        if (n/i).is_integer():
            yield i
        i += 1
