def sum(list):
    """pré: la liste peut être vide, peut contenir autre que des nombres et elle peut aussi contenir des floats
       post: le program doit affciher la somme des nombres dans la liste(nombre entiers ou décimaux) et si la,liste est vide au départ
       le program doit doit retourn la sum qui est est égal à 0"""
    s=0
    if len(list)==0:
        return s
    for i in list:
        if i==str or i==float:
            return s
        else:
            s+=i

    return s