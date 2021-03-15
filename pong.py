'''
Simple Pong Game for python beginners
Code adapted from @TokyoEdTech
@author Sagnik
@date 3/15/2021
'''
#dependency for simple graphics development
import turtle
import random

#(0,0) is the centre of the screen
window = turtle.Screen()
window.title("Pong Game MK 1.0")
window.bgcolor("black")
window.setup(width=800, height=600)

#stops the window from updating by itself
window.tracer(0)

'''Ball'''
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0,0)

#delta by which ball moves
#random.uniform(0, 1)
ball.dx = 0.16
ball.dy = 0.16

'''Paddle 1'''
paddle_1 = turtle.Turtle()

#speed of animation
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("gray")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
#prevent drawing lines
paddle_1.penup()

#where it starts
paddle_1.goto(-350, 0)

'''Paddle 2'''
paddle_2 = turtle.Turtle()

#speed of animation
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("gray")
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
#prevent drawing lines
paddle_2.penup()

#where it starts
paddle_2.goto(+350, 0)

'''paddle controllers'''
def paddle_1_up():
    y = paddle_1.ycor()
    y += 20
    paddle_1.sety(y)

def paddle_1_down():
    y = paddle_1.ycor()
    y -= 20
    paddle_1.sety(y)

def paddle_2_up():
    y = paddle_2.ycor()
    y += 20
    paddle_2.sety(y)

def paddle_2_down():
    y = paddle_2.ycor()
    y -= 20
    paddle_2.sety(y)


''' keyboard listeners'''
window.listen()
window.onkeypress(paddle_1_up, "w")
window.onkeypress(paddle_1_down, "s")

window.onkeypress(paddle_2_up, "Up")
window.onkeypress(paddle_2_down, "Down")

#Game loop
while True:
    #we update manually here
    window.update()

    #move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


    #border check
    #window dimensions width: 800 heigh: 600
    #thus, +300 & -300 y axis. ball is 10 units

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= - 1

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= - 1

    #paddle collisions
    if ( ball.xcor() > 340 and ball.xcor() < 350 ) and ( ball.ycor() < paddle_2.ycor() + 40 and ball.ycor() > paddle_2.ycor() -40 ):
        ball.setx(340)
        ball.dx *= -1

    if ( ball.xcor() < -340 and ball.xcor() > -350 ) and ( ball.ycor() < paddle_2.ycor() + 40 and ball.ycor() > paddle_2.ycor() -40 ):
        ball.setx(340)
        ball.dx *= -1