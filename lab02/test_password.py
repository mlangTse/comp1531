from password import check_password

def test_password():
    assert check_password("iloveyou") == "Horrible password"
    assert check_password("lol :)wsajdiloveyou435287") == "Moderate password"
    assert check_password("LOL :)wsajdiloveyou435287") == "Strong password"
    
    assert check_password("QWERTYUIOPL,MNBVCXZASDFGHJK12345") == "Moderate password"
    assert check_password("QWERTYUIOPL,MNBVCXZASDFGHJK12345abc") == "Strong password"
    
    assert check_password("9-0-'/.;]..[") == "Moderate password"
    assert check_password("9-0-[") == "Poor password"
    assert check_password("------*^%&$#^%@#*[") == "Poor password"
    
