from balanced import balanced
from hypothesis import given, strategies
import inspect

def test_generator():
    '''
    Ensure it is generator function
    '''
    assert inspect.isgeneratorfunction(balanced), "balanced does not appear to be a generator"

def test_3():
    assert sorted(list(balanced(3))) == []

def test_4():
    assert sorted(list(balanced(4))) == ['(())', '()()']

def test_6():
    assert sorted(list(balanced(6))) == ['((()))', '(()())', '(())()', '()(())', '()()()']

def test_9():
    assert sorted(list(balanced(3))) == []
