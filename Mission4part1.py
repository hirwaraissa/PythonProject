def is_adn(s):
    for i in range (len(s)):
        if i=="a" or i=="t" or i=="c" or i=="g":
            return True
        elif i=="A" or i=="T" or i=="C" or i=="G":
            return True
    return False


def is_adn(s):
    for i in s:
        if i=="a" or i=="t" or i=="c" or i=="g":
            return True
        elif i=="A" or i=="T" or i=="C" or i=="G":
            return True
        
    return False


#Le code avant fait fonctionner toute type de reultat mais le code suivant ne fonctionne pas avec tout


def is_adn(s):
    for i in range (len(s)):
        if i=="a" or i=="t" or i=="c" or i=="g":
            return True
        elif i=="A" or i=="T" or i=="C" or i=="G":
            return True
    return False

    for i in s:
        if i=="a" or i=="t" or i=="c" or i=="g":
            return True
        elif i=="A" or i=="T" or i=="C" or i=="G":
            return True
        
    return False


