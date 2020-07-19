#Simple Pong Game using Python 3
#by @nmbaibhab

import turtle

#Screen area
win=turtle.Screen()
win.title("Simple Pong Game")
win.bgcolor("green")
win.setup(width=800,height=600)
win.tracer(0)

#Score
score_a=0
score_b=0

#Paddle A
paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_len=1,stretch_wid=5)
paddle_a.penup()
paddle_a.goto(-370,0)

#Paddle B
paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_len=1,stretch_wid=5)
paddle_b.penup()
paddle_b.goto(370,0)

#Ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.shapesize(stretch_len=1,stretch_wid=1)
ball.penup()
ball.goto(0,0)
ball.dx=0.3
ball.dy=-0.3

#Pen(Scoreboard)
pen=turtle.Turtle()
pen.speed(0)
pen.color("Yellow")
pen.penup()
pen.hideturtle()
pen.goto(0,250)
pen.write("Player A: 0   Player B: 0" , align="center",font=("Cursive",25,"normal"))


#Function to move the paddles
def paddle_a_up():
    y=paddle_a.ycor()
    y+=20
    paddle_a.sety(y)

def paddle_a_down():
    y=paddle_a.ycor()
    y-=20
    paddle_a.sety(y)

def paddle_b_up():
    y=paddle_b.ycor()
    y+=20
    paddle_b.sety(y)

def paddle_b_down():
    y=paddle_b.ycor()
    y-=20
    paddle_b.sety(y)

#Keyborad inputs
win.listen()
win.onkeypress(paddle_a_up,"w")
win.onkeypress(paddle_a_down,"s")
win.onkeypress(paddle_b_up,"Up")
win.onkeypress(paddle_b_down,"Down")


#Main Game
while (True):
    win.update()

    # Moving the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy*=-1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy*=-1

    if ball.xcor()> 390:
        ball.goto(0,0)
        ball.dx*=-1
        score_a+=1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(score_a,score_b) , align="center",font=("Cursive",25,"normal"))

    if ball.xcor()< -390:
        ball.goto(0,0)
        ball.dx*=-1
        score_b+=1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(score_a,score_b) , align="center",font=("Cursive",25,"normal"))
        
    
    #Paddle ball collision

    if (ball.xcor()> 350 and ball.xcor()<360)and(ball.ycor()<paddle_b.ycor()+50 and ball.ycor()>paddle_b.ycor()-50):
        ball.setx(350)
        ball.dx*=-1
    if (ball.xcor()< -350 and ball.xcor()>-360)and(ball.ycor()<paddle_a.ycor()+50 and ball.ycor()>paddle_a.ycor()-50):
        ball.setx(-350)
        ball.dx*=-1

        