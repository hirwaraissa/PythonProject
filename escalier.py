import turtle
t=turtle.Turtle()
t.color("blue")

longueur_marche=20
for i in range(3):
    t.forward(longueur_marche)
    t.right(90)
    t.forward(longueur_marche)
    t.left(90)
    
    