from reverse import reverse_words

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

def test_reverse5():    
    word = ['', " "]
    word = reverse_words(word)
    assert word == ['', ' ']
