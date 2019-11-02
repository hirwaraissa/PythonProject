#greeting = "Hello, world!"
#greeting[0] = 'J'            # ERROR!
#print(greeting)

greeting = "Hello, world!"
new_greeting = "J" + greeting[1:]
print(new_greeting)

def find(strng, ch):
    """
      Find and return the index of ch in strng.
      Return -1 if ch does not occur in strng.
    """
    ix = 0
    while ix < len(strng):
        if strng[ix] == ch:
            return ix
        ix += 1
    return -1

print(find("Raïssa","R"))


def count_a(text):
    count = 0
    for c in text:
        if c == "f":
            count += 1
    return(count)
print(count_a("rfiiefifbzeçhzifneoçfehoeihefihfiofejizhfsdneisovsovnsioedzo"))



a="Hey, Jonathan, i know we discuss much but i do love you bro"
w=a.split()
print(w)
print(a.split())