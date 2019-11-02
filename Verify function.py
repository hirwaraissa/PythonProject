from sorted_belgian_communes import*
def verify_order(all_communes):
    """ Détermine si les communes sont ordonnées par ordre alphabétique.

    Une liste est considérée ordonnée par ordre alphabétique si a[0] < c[e[1]][0]
    Args:
        communes:  une liste de tuples, dont chacun se compose d'une chaîne de caractères et un nombre entier .
    Returns:
        True si communes sont ordonnés, False si non.
    """
    
    ord=0
    for i in all_communes:
        y=i+1
        if i[0][0]<y:
            return True
        print("La liste est en ordre")
    