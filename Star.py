import turtle
wn = turtle.Screen()
star = turtle.Turtle()
star.color("yellow")
size=100 #espace entre les etoiles

rectangle = turtle.Turtle()
rectangle.pensize("5")
rectangle.color("blue")

rectangle.penup()
rectangle.setpos(-470,300)

rectangle.begin_fill()
rectangle.pendown()
rectangle.forward(930)
rectangle.right(90)
rectangle.forward(600)
rectangle.right(90)
rectangle.forward(930)
rectangle.right(90)
rectangle.forward(600)
rectangle.right(90)
rectangle.end_fill()
rectangle.hideturtle()

star.penup()
star.setpos(-49,200)
star.pendown()


star.begin_fill()
for i in range(5):
                             #1
    star.forward(50)
    star.right(144)
    
star.end_fill()


star.penup()
star.forward(size)       
star.right(30)           
star.pendown()

star.begin_fill()
for i in range(5):
    star.forward(50)        #2
    star.right(144)
    
star.end_fill()

star.penup()
star.forward(size)       
star.right(30)           
star.pendown()

star.begin_fill()
for i in range(5):
    star.forward(50)        #3
    star.right(144)
    

star.end_fill()

star.penup()
star.forward(size)       
star.right(30)           
star.pendown()

star.begin_fill()
for i in range(5):
    star.forward(50)      #4
    star.right(144)

star.end_fill()
star.penup()
star.forward(size)       
star.right(30)           
star.pendown()

star.begin_fill()
for i in range(5):
    star.forward(50)      #5
    star.right(144)
    

star.end_fill()

star.penup()
star.forward(size)       
star.right(30)           
star.pendown()

star.begin_fill()
for i in range(5):
    star.forward(50)       #6
    star.right(144)

star.end_fill()

star.penup()
star.forward(size)       
star.right(30)           
star.pendown()

star.begin_fill()
for i in range(5):
    star.forward(50)          #7
    star.right(144)
    

star.end_fill()

star.penup()
star.forward(size)       
star.right(30)            
star.pendown()

star.begin_fill()    
for i in range(5):
    star.forward(50)          #8
    star.right(144)

star.end_fill()

star.penup()
star.forward(size)       
star.right(30)           
star.pendown()

star.begin_fill()
for i in range(5):
    star.forward(50)         #9
    star.right(144)
    

star.end_fill()

star.penup()
star.forward(size)       
star.right(30)           
star.pendown()

star.begin_fill()
for i in range(5):
    star.forward(50)        #10
    star.right(144)
    
    
star.end_fill()

star.penup()
star.forward(size)       
star.right(30)           
star.pendown()

star.begin_fill()
for i in range(5):
    star.forward(50)      #11
    star.right(144)
    
star.end_fill()    

star.penup()
star.forward(size)       
star.right(30)           
star.pendown()

star.begin_fill()
for i in range(5):
    star.forward(50)      #12
    star.right(144)
star.end_fill()
star.hideturtle()

rectangle = turtle.Turtle()
rectangle.pensize("5")
rectangle.color("black")

rectangle.penup()

rectangle.setpos(-470,300)
rectangle.pendown()

rectangle.forward(930)
rectangle.right(90)
rectangle.forward(600)
rectangle.right(90)
rectangle.forward(930)
rectangle.right(90)
rectangle.forward(600)
rectangle.right(90)

rectangle.hideturtle()
    
    



    
wn.mainloop()