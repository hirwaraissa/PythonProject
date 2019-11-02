import turtle                
tortue = turtle.Turtle()     
tortue.speed("fast")     

def square(size, color):
    tortue.color(color)
    tortue.pendown()
    tortue.begin_fill()
    for i in range(4):
        tortue.forward(size)
        tortue.right(90)
    tortue.end_fill()
    tortue.penup()

def rectangle(length, width, color):
    tortue.color(color)
    tortue.pendown()
    tortue.begin_fill()
    for i in range(2):
        tortue.forward(length)
        tortue.left(90)
        tortue.forward(width)
        tortue.left(90)
    tortue.end_fill()
    tortue.penup()
    

def belgian_flag(width):
    tortue.pendown()
    for color in ("Black","Yellow","Red"):
        tortue.color(color)
        tortue.begin_fill()
        for i in range (2):
                tortue.forward(width/3)
                tortue.left(90)
                tortue.forward(2/3 * width)
                tortue.left(90)
        tortue.end_fill()
        tortue.forward(width/3)
    tortue.penup()
    tortue.right(90)
    tortue.forward(width)
    tortue.left(90)
    
            
def three_color_flag(color1,color2,color3):
    tortue.pendown()
    for color in (color1,color2,color3):
        tortue.color(color)
        tortue.begin_fill()
        for i in range (2):
                tortue.forward(width/3)
                tortue.left(90)
                tortue.forward(2/3 * width)
                tortue.left(90)
        tortue.end_fill()
        tortue.forward(width/3)
    tortue.penup()
    tortue.right(90)
    tortue.forward(width)
    tortue.left(90)
    
    
def dutch_flag():
    tortue.pendown()
    for color in ("Blue","White","Red"):
        tortue.color(color)
        tortue.begin_fill()
        for i in range (2):
                tortue.forward(width)
                tortue.left(90)
                tortue.forward(width* 2/9)
                tortue.left(90)
        tortue.end_fill()
        tortue.left(90)
        tortue.forward(width*2/9)
        tortue.right(90)
    tortue.penup()
    tortue.right(90)
    tortue.forward(width*2/3)
    
    tortue.left(90)
    
    
def german_flag():
    tortue.pendown()
    for color in ("Orange","Red","Black"):
        tortue.color(color)
        tortue.begin_fill()
        for i in range (2):
                tortue.forward(width)
                tortue.left(90)
                tortue.forward(width *2/9)
                tortue.left(90)
        tortue.end_fill()
        tortue.left(90)
        tortue.forward(width*2/9)
        tortue.right(90)
    tortue.penup()
    tortue.right(90)
    tortue.forward(width*2/3)
    
    tortue.left(90)
    

def luxemburg_flag():
    tortue.pendown()
    for color in ("Lightblue","White","Red"):
        tortue.color(color)
        tortue.begin_fill()
        for i in range (2):
                tortue.forward(width)
                tortue.left(90)
                tortue.forward(width *2/9)
                tortue.left(90)
        tortue.end_fill()
        tortue.left(90)
        tortue.forward(width*2/9)
        tortue.right(90)
    tortue.penup()
    tortue.right(90)
    tortue.forward(width*2/3)
    
    tortue.left(90)
    
def french_flag(width):
    tortue.pendown()
    for color in ("Blue","White","Red"):
        tortue.color(color)
        tortue.begin_fill()
        for i in range (2):
                tortue.forward(width/3)
                tortue.left(90)
                tortue.forward(2/3 * width)
                tortue.left(90)
        tortue.end_fill()
        tortue.forward(width/3)
    tortue.penup()
    tortue.right(90)
    tortue.forward(width)
    tortue.left(90)

def rectangle(width,color):
    tortue.pendown()
    tortue.begin_fill()
    tortue.color(color)

    for i in range (2):
        tortue.forward(width *4/3)
        tortue.left(90)
        tortue.forward( width)
        tortue.left(90)
      
def draw_atriangle(l):        #function that draws one of the five triangles that make up a star( turtlename, length/size )
    tortue.begin_fill()
    tortue.forward(l/2)
    tortue.left(120)
    tortue.forward(l)
    tortue.left(120)
    tortue.forward(l)
    tortue.left(120)
    tortue.forward(l/2)
    tortue.end_fill()

    
def draw_astar(l):            #function to draw a star
    for i in range(5):
        draw_atriangle(l)     #call for the function 'draw_atriagnle'(turtle,lenghth)
        tortue.right(72)


def european_flag(l):         #function to draw a circle
    rectangle_blue(width)
    l = width / 20
    for i in range(12):
        tortue.color("Yellow")
        tortue.penup()
        tortue.forward(4 * l)
        draw_astar(l)
        tortue.left(30)
        tortue.penup()


def rectangle_blue(width):
    tortue.pendown()
    tortue.begin_fill()
    tortue.color("blue")
    tortue.forward(width *4/3)
    tortue.left(90)
    tortue.forward(width)
    tortue.left(90)
    tortue.forward(width *8/3)
    tortue.left(90)
    tortue.forward(2*width)
    tortue.left(90)
    tortue.forward(width *8/3)
    tortue.left(90)
    tortue.forward(width)
    tortue.left(90)
    tortue.forward(width *4/3 - width/3)
    tortue.right(90)
    tortue.end_fill()
    
def belgian_flag2(width):
    tortue.pendown()
    for color in ("Black","Yellow","Red"):
        tortue.color(color)
        tortue.begin_fill()
        for i in range (2):
                tortue.forward(width/3)
                tortue.left(90)
                tortue.forward(2/3 * width)
                tortue.left(90)
        tortue.end_fill()
        tortue.ht()
        tortue.forward(width/3)
       

           
width = 100


european_flag(width)

tortue.forward(width + 2/9* width)
tortue.left(90)
tortue.forward(2*width + 2/3* width)
tortue.left(180)

dutch_flag()
tortue.forward(width + 2/9* width)
german_flag()
tortue.forward(width + 2/9* width)
luxemburg_flag()
tortue.forward(width + 2/9* width)   
french_flag(width)
tortue.right(90)


tortue.forward( width + 4/9 * width )
tortue.right(90)
tortue.forward(4 *width + 4/3* width)
tortue.right(220)


belgian_flag2(width)
tortue.penup()
tortue.forward(4/9* width)
tortue.left(20)
    









