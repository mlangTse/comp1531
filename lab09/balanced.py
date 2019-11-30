def balanced(n):
    '''
    Given a positive number n, yield all strings of length n, in any order, that only contain balanced brackets. For example:
    >>> sorted(list(balanced(6)))
    ['((()))', '(()())', '(())()', '()(())', '()()()']
    '''
    string = ''
    if n % 2 == 0:
        for i in range(n):
            if i < n/2:
                string += '('
            else:
                string += ')'

    balanced_list = []
    for i in helper(string):
        if is_balance(i) and i not in balanced_list:
            balanced_list.append(i)
            yield i

def is_balance(string):
    if string[0] == ')' or string[len(string)-1] == '(':
        return False
    count = 0
    for i in string:
        if count < 0:
            return False
        if i == '(':
            count += 1
        elif i == ')':
            count -= 1

    return True

def helper(string):
    lst = list(string)
    if len(string) in range(2):
        return string
    l = [] # empty list that will store current permutation

    # Iterate the input(lst) and calculate the permutation
    for i in range(len(lst)):
        m = lst[i]

        # Extract lst[i] or m from the list.  remLst is
        # remaining list
        remLst = lst[:i] + lst[i+1:]
        # Generating all permutations where m is first
        # element
        for p in helper(remLst):
            l.append(m+p)
    return l
