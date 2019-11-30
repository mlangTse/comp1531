from list_exercises import *

def test_reverse():
    l = [0]
    reverse_list(l)
    assert l == [0]

    l = [-3, -2, -1, 0, 1, 2, 3]
    reverse_list(l)
    assert l == [3, 2, 1, 0, -1, -2, -3]
    
def test_reverse2():
    # TODO Write more tests for reverse
    l = [-100000000000000000000, 1111000, 0]
    reverse_list(l)
    assert l == [0, 1111000, -100000000000000000000]
    
    l = ["hi", "you", "are", "how", "hi"]
    reverse_list(l)
    assert l == ["hi", "how", "are", "you", "hi"]
    
    l = ['lol', ':)', '', ' ']
    reverse_list(l)
    assert l == [' ', '', ':)', 'lol']

def test_min():
    assert minimum([0]) == 0
    assert minimum([-3, -2, -1, 0, 1, 2, 3]) == -3
    # TODO Write more tests for minimum
    
def test_min2():   
    assert minimum([-100000000000000000000, 1111000, 0]) == -100000000000000000000
    assert minimum([234234234324.23, 234234234324.21, 234234234324.20]) == 234234234324.20
    #can't contain string or char
    #assert minimum(['sdaf', -1]) == -1

def test_sum():
    assert sum_list([0]) == 0
    assert sum_list([-3, -2, -1, 0, 1, 2, 3]) == 0
    # TODO Write more tests for sum
    assert sum_list([5.6, 4.4]) == 10
    
