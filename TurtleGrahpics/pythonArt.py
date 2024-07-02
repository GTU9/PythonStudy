import turtle as turtle_module
import random

turtle_module.colormode(255)


t = turtle_module.Turtle()
t.shape("turtle")
t.speed(0)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    random_rgb_color = (r, g, b)
    return random_rgb_color

def draw_spirograph(size_of_gap):
    for i in range(round(360/size_of_gap)):
        t.forward(10)
        t.right(90)
        t.forward(15+i*size_of_gap)
        t.color(random_color())
        t.setheading(t.heading()+size_of_gap)

t.pensize(5)
draw_spirograph(5)

my_screen = turtle_module.Screen()
my_screen.exitonclick()
