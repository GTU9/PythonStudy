from turtle import Turtle, Screen

t=Turtle()
screen = Screen()

def move_forward():
    t.forward(100)

def move_backward():
    t.backward(100)

def move_right_forward():
    t.setheading(t.heading()-90)

def move_left_forward():
    t.setheading(t.heading()+90)

def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()

screen.listen()
screen.onkey(key="Up",fun=move_forward)
screen.onkey(key="Right",fun=move_right_forward)
screen.onkey(key="Left",fun=move_left_forward)
screen.onkey(key="Down",fun=move_backward)
screen.onkey(key="Home",fun=clear)


screen.exitonclick()