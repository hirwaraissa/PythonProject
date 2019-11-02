import turtle
wn = turtle.Screen()         # Set up the window and its attributes
wn.bgcolor("lightgreen")
wn.title("Tess & Alex")
alex = turtle.Turtle()

for c in ["yellow", "red", "purple", "blue"]:
    alex.color(c)
    alex.forward(50)
    alex.left(90)
    
alex.penup()
alex.forward(100)     # This moves alex, but no line is drawn
alex.pendown()

for c in ["yellow", "red", "purple", "blue"]:
    alex.color(c)
    alex.forward(50)
    alex.left(90)
    
alex.penup()
alex.forward(-200)     # This moves alex, but no line is drawn
alex.pendown()

for c in ["yellow", "red", "purple", "blue"]:
    alex.color(c)
    alex.forward(50)
    alex.left(90)
    
wn.mainloop()
