import inspect

from divisors import divisors

def test_generator():
    '''
    Ensure it is generator function
    '''
    assert inspect.isgeneratorfunction(divisors), "divisors does not appear to be a generator"

def test_12():
    assert list(divisors(12)) == [1,2,3,4,6,12]

def test_13():
    assert list(divisors(13)) == [1,13]

def test_3600():
    assert list(divisors(3600)) == [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 25, 30, 36, 40, 45, 48, 50, 60, 72, 75, 80, 90, 100, 120, 144, 150, 180, 200, 225, 240, 300, 360, 400, 450, 600, 720, 900, 1200, 1800, 3600]
