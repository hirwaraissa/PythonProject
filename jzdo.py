import turtle                            #Drapeau de l europe
wn = turtle.Screen()
blgique = turtle.Turtle()
belgique_three_color("black","Yellow","Red")
size=100 #espace entre les etoiles

def rectangle(300,100):
    belgique_three_color("black","Yellow","Red")
    belgique.pensize("5")
    belgique.speed(7)
    
    belgique.penup()
    belgique.setpos(-550,500)
    belgique.pendown()
    belgique.begin_fill()
    for y in range("black","yellow","Red"):
        for z in range(4):
            belgique.forward(100)
            belgique.right(90)
            belgique.forward(100)
            belgique.right(90)
            belgique.forward(100)
            belgique.right(90)
            belgique.forward(100)
            
    belgique.end_fill()
    belgique.penup()
    

wn.mainloop()
    