
def reverse_words(string_list):
    '''
    Given a list of strings, return a new list where the order of the words is reversed.

    For example,
    >>> reverse_words(["Hello World", "I am here"])
    ['World Hello', 'here am I']
    '''
    new = []
    for string in string_list:
        if string is not ' ':
            s = string.split()
            s.reverse()
            new.append(' '.join(s))
        else:
            new.append(string) 
	        
    return new
    

if __name__ == '__main__':
    reverse_words(["Hello World", "I am here"])
    
#test for reverse.py
def test_reverse1():
    word = ['ABCDEFG', 'hello world']
    word = reverse_words(word)
    assert word == ['ABCDEFG', 'world hello']
    
def test_reverse2():
    word = ['adsf42234 09']
    word = reverse_words(word)
    assert word == ['09 adsf42234'] 
    
def test_reverse3():
    word = ['uoy evol i', 'i love you']
    word = reverse_words(word)
    assert word == ['i evol uoy', 'you love i'] 
    
def test_reverse4():   
    word = ['234 safs2 23 a23 dsf', '234 987 is digit']
    word = reverse_words(word)
    assert word == ['dsf a23 23 safs2 234', 'digit is 987 234'] 

#confuse
def test_reverse5():    
    word = ['', " "]
    word = reverse_words(word)
    assert word == ['', ' ']
    
