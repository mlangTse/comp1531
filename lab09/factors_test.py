from factors import factors, is_prime
from hypothesis import given, strategies
import inspect

def test_generator():
    '''
    Ensure it is generator function.
    '''
    assert inspect.isgeneratorfunction(factors), "factors does not appear to be a generator"

def test_0():
    assert list(factors(0)) == []

def test_36():
    assert list(factors(36)) == [2, 2, 3, 3]

def test_11():
    assert list(factors(11)) == [11]

def test_100():
    assert list(factors(100)) == [2, 2, 5, 5]

def test_121():
    assert list(factors(121)) == [11, 11]