import turtle
from turtle import Turtle, Screen

turtle1 = Turtle()
turtle2 = Turtle()
bullet1=Turtle(visible=False)
bullet2=Turtle(visible=False)
screen = Screen()
screen.listen()
screen.setup(1200, 700)



def turtle_start():
    turtle1.color('blue')
    turtle2.color('red')

    turtle1.shape('turtle')
    turtle1.penup()
    turtle1.goto(-500, 0)

    turtle2.shape('turtle')
    turtle2.left(180)
    turtle2.penup()
    turtle2.goto(500, 0)


def turtle1_move_up():
    if (turtle1.ycor() < 300):
        turtle1.speed(0)
        turtle1.left(90)
        turtle1.forward(100)
        turtle1.right(90)


def turtle1_move_down():
    if (turtle1.ycor() > -300):
        turtle1.speed(0)
        turtle1.right(90)
        turtle1.forward(100)
        turtle1.left(90)

def turtle2_move_down():
    if (turtle2.ycor() < 300):
        turtle2.speed(0)
        turtle2.left(90)
        turtle2.forward(100)
        turtle2.right(90)


def turtle2_move_up():
    if (turtle2.ycor() > -300):
        turtle2.speed(0)
        turtle2.right(90)
        turtle2.forward(100)
        turtle2.left(90)


def bul1():
    bullet = Turtle(visible=False)
    bullet.shape("circle")
    bullet.speed(0)
    bullet.penup()
    bullet.goto(turtle1.xcor(), turtle1.ycor())
    bullet.showturtle()
    for _ in range(30):
     bullet.forward(40)

def bul2():
    bullet2 = Turtle(visible=False)
    bullet2.shape("circle")
    bullet2.speed(0)
    bullet2.penup()
    bullet2.goto(turtle2.xcor(), turtle2.ycor())
    bullet2.showturtle()
    for _ in range(30):
     bullet2.backward(40)




screen.onkey(key="w", fun=turtle1_move_up)
screen.onkey(key="s", fun=turtle1_move_down)
screen.onkey(key="d", fun=bul1)

screen.onkey(key="Up", fun=turtle2_move_up)
screen.onkey(key="Down", fun=turtle2_move_down)
screen.onkey(key="Left", fun=bul2)

turtle_start()

screen.exitonclick()
