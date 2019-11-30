from permutations import permutations
from hypothesis import given, strategies, assume
import inspect

def test_generator():
    '''
    Ensure it is generator function
    '''
    assert inspect.isgeneratorfunction(permutations), "permutations does not appear to be a generator"

def test_empty_permutation():
    assert sorted(list(permutations(''))) == []

def test_single_permutation():
    assert sorted(list(permutations('A'))) == ['A']

def test_two_permutation():
    assert sorted(list(permutations('AB'))) == ['AB', 'BA']

def test_simple_permutation():
    assert sorted(list(permutations('ABC'))) == ['ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA']

def test_duplicate_permutation():
    assert sorted(list(permutations('ABB'))) == ['ABB', 'ABB', 'BAB', 'BAB', 'BBA', 'BBA']

def test_number_permutation():
    assert sorted(list(permutations('123'))) == ['123', '132', '213', '231', '312', '321']