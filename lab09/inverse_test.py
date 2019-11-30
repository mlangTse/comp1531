from inverse import inverse
from hypothesis import given, strategies

@given(strategies.dictionaries(keys=strategies.integers(), values=strategies.characters()))
def test_inverse(d):
    '''
    The result should be the actual inverse.
    '''
    d_inverse = inverse(d)
    for k in d:
        assert k in d_inverse[d[k]]

    for v in d_inverse:
        for k in d_inverse[v]:
            assert d[k] == v