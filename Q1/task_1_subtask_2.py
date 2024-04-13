import turtle


wn=turtle.Screen()            #created a window
wn.title("Turtlepong")        #named the window
wn.bgcolor("blue")            #color coding the background
wn.setup(width=800,height=600)  #choosing the dimensions of the window
wn.tracer(0)                  #sops the window from updating, we manually update ,
                                #speeds up the process
#Paddle A
paddle_a=turtle.Turtle()        #defining paddleA as a turtle
paddle_a.speed(0)               #In turtle library , 0 is the mapped to the fastest speed possible
paddle_a.shape("turtle")
paddle_a.color("yellow")
paddle_a.goto(-350,0)       # defining initial position
#Ball=moving turtle
ball=turtle.Turtle()
ball.speed(0)
ball.shape("turtle")
ball.color("yellow")
ball.goto(0,0)
ball.dx=2             #every time ball moves by 2 pixels
ball.dy=-2           #( we give random dx,dy values for defining how much they move)
#Function
def paddle_a_up():
    #we define a function which moves the paddle up by 20
    y = paddle_a.ycor()
    y=y+20
    paddle_a.sety(y)
def paddle_a_down():          #we define a function which moves the paddle down by 20
    y=paddle_a.ycor()
    y=y-20
    paddle_a.sety(y)
#keyboaard binding                       # we are controlling the paddle with the keyboard
wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
#Main game loop
while True:
    wn.update()                    #this updates the window every time this loop is run

    #moving the ball, this gives the new position of the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #border check,        """every time a wall is hit ball needs to bounce back """
    if ball.ycor()>290:     # we take 290 and not  300 , since ball has dimensions 10x10
        ball.sety(290)       # we reset the coordinate as it reaches the boundary
        ball.dy*=-1          #this line basically changes the direction of the ball
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy*=-1

    if (ball.xcor()>390) :     #this block of code ensures the collision with the right wall
        ball.setx(390)
        ball.dx *= -1
     # paddle and ball collisions   """ the if condition given here is that, when the ball snould not go behind the paddle and bounce back before it does"

    if (ball.xcor()<-340 and ball.xcor()>-350) :
        ball.setx(-340)
        ball.dx *= -1

