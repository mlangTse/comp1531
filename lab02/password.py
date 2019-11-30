def check_password(password):
    '''
    Takes in a password, and returns a string based on the strength of that password.

    The returned value should be:
    * "Strong password", if at least 12 characters, contains at least one number, at least one uppercase letter, at least one lowercase letter.
    * "Moderate password", if at least 8 characters, contains at least one number.
    * "Poor password", for anything else
    * "Horrible password", if the user enters "password", "iloveyou", or "123456"
    '''
    
    if password is "password" or password is "iloveyou" or password is "123456":
        return "Horrible password"
        
    len = 0
    num = False
    upper = False
    lower = False
    
    for l in password:
        if l.isdigit():
            num = True
        if l.isupper():
            upper = True
        if l.islower():
            lower = True
        len += 1
        
    if len >= 12 and num and upper and lower:
        return "Strong password"
    elif len >= 8 and num:
        return "Moderate password"
    else: 
        return "Poor password"
        
if __name__ == '__main__':
    print(check_password("ihearttrimesters"))
    
#test for password.py
def test_password1():
    assert check_password("iloveyou") == "Horrible password"
    assert check_password("lol :)wsajdiloveyou435287") == "Moderate password"
    assert check_password("LOL :)wsajdiloveyou435287") == "Strong password"
    
def test_password2():    
    assert check_password("QWERTYUIOPL,MNBVCXZASDFGHJK12345") == "Moderate password"
    assert check_password("QWERTYUIOPL,MNBVCXZASDFGHJK12345abc") == "Strong password"
    
def test_password3():  
    assert check_password("9-0-'/.;]..[") == "Moderate password"
    assert check_password("9-0-[") == "Poor password"
    assert check_password("------*^%&$#^%@#*[") == "Poor password"
    
