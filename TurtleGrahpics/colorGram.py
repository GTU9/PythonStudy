import colorgram
import turtle as turtle_module
import random

turtle_module.colormode(255)
rgb_colors = []
colors = colorgram.extract('image.jpg',8)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_colors.append(new_color)

t = turtle_module.Turtle()
t.speed('fastest')
t.penup()
t.hideturtle()

t.setheading(225)
t.forward(250)
t.setheading(0)
num_of_dots = 100

for dot_count in range(1, num_of_dots + 1):
    t.dot(20, random.choice(rgb_colors))
    t.forward(50)
    if dot_count % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()