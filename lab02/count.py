
def count_char(input):
    '''
    Counts the number of occurrences of each character in a string. The result should be a dictionary where the key is the character and the dictionary is its count.

    For example,
    >>> count_char("HelloOo!")
    {'H': 1, 'e': 1, 'l': 2, 'o': 2, 'O': 1, '!': 1}
    '''
    new_dic = {}
    
    for l in input:
        if l not in new_dic.keys():
            new_dic[l] = 1
        else:
            new_dic[l] += 1
            
    return new_dic
