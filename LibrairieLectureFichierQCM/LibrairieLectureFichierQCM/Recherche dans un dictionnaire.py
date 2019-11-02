def linear_search(name, list_of_name):
    for list_name in list_of_name:
        if name==list_name:
            return True
        
    return False
        
print()
print()


def binary_search ( name, list_of_names ):
    first = 0
    last = len(list_of_names)-1
    found = False
    while first<=last and not found:
        middle = (first + last)//2
        if list_of_names[middle] == name:
            found = True
        else:
            if name < list_of_names[middle]:
                last = middle-1
            else:
                first = middle+1
    return found