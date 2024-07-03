from turtle import Turtle,Screen
import random

screen = Screen()
screen.setup(500,400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
start_Y_position=-120
all_turtles=[]

bet_color=screen.textinput("make your bet", "Which turtle will win the race? Enter a color: ")


for turtle_index in range(0,len(colors)):
    new_turtle=Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=start_Y_position)
    start_Y_position += 50
    all_turtles.append(new_turtle)

is_False=True

while is_False:
    for turtle in all_turtles:
        turtle.forward(random.randint(1,10))
        if(turtle.xcor()>200):
            is_False=False
            winner=turtle.pencolor()
            if(bet_color==winner):
                print("승리하셨습니다.")
            else:
                print("패배하셨습니다.")






screen.exitonclick()