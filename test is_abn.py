def test_is_adn(s):
    for y in s:
        
        if y=="a" or y=="t" or y=="g" or y=="c":
            return True
        elif y=="A" or y=="T" or y=="G" or y=="C":
            return True
        return False

def test_is_adn(s):
    for y in range(len(s)):
        
        if y=="a" or y=="t" or y=="g" or y=="c":
            return True
        elif y=="A" or y=="T" or y=="G" or y=="C":
            return True
    return False


def test_is_adn ():
  test(bioinfo.is_adn('atx')==False)
  test(bioinfo.is_adn('atg')==True )
 