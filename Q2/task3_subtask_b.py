import turtle
import random


wn=turtle.Screen()            #created a window
wn.title("Chasing Bhai")        #named the window
wn.bgcolor("black")            #color coding the background
wn.setup(width=600,height=400)  #choosing the dimensions of the window
              #sops the window from updating, we manually update ,
                                #speeds up the process
bhai=turtle.Turtle()

# Function to draw a white circle at a given position
def draw_circle(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("white")
    turtle.circle(1)

def draw_bhai(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("blue")
    turtle.circle(5)

# Set up the Turtle
turtle.speed(0)  # Set the fastest drawing speed
turtle.hideturtle()  # Hide the turtle icon

a=[]
# Draw 10 white circles at random positions
for _ in range(10):
    x = random.randint(-280, 280)  # Generate random x-coordinate
    y = random.randint(-180, 180)  # Generate random y-coordinate
    draw_circle(x, y)
    a=turtle.Turtle()


#spawn bhai
x = random.randint(-280, 280)  # Generate random x-coordinate
y = random.randint(-180, 180)  # Generate random y-coordinate
draw_bhai(x, y)
bhai.speed(0)
bhai.dx=2
bhai.dy=-2
# Keep the window open until it is manually closed
turtle.done()


#main game loop
while True:
    wn.update()
    # moving the ball, this gives the new position of the ball
    bhai.setx(bhai.xcor() + bhai.dx)
    bhai.sety(bhai.ycor() + bhai.dy)

