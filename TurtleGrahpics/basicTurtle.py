import random
from turtle import Turtle, Screen

colors = ["blue", "red", "chocolate", "lime", "purple", "dark slate blue", "light slate gray", "light sky blue", "navajo white"]
directions = [0, 90, 180, 270]

screen = Screen()
screen.colormode(255)

t = Turtle()

def forward():
    # 거북이 색을 내가 좋아하는 색으로 변경하기
    t.color("green")
    # 거북이를 100만큼 전진하기
    t.forward(100)
    # 점선그리기
    for _ in range(20):
        t.forward(10)
    t.penup()
    t.forward(10)
    t.pendown()

def drawTriangle():
    # 삼각형
    # 100만큼 전진
    # 회전
    for _ in range(3):
        t.forward(100)
        t.left(120)

# n각형
def draw_shape(rotates):
    for _ in range(rotates):
        t.forward(100)
        t.left(360 / rotates)
        for i in range(3, 11):
            t.color(random.choice(colors))

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)

    random_rgb_color = (r, g, b)
    return random_rgb_color

def random_walk(walk_length, amount_of_time):
    for i in range(amount_of_time):
        t.setheading(random.choice(directions))
        t.forward(walk_length)
        # t.color(random.choice(colors))
        t.color(random_color())


def draw_spirograph(size_of_gap):
    for _ in range(round(360/size_of_gap)):
        t.circle(200)
        t.color(random_color())
        t.setheading(t.heading()+size_of_gap)

# t.pensize(5)
# t.shape("turtle")
# t.speed(0)
#
# draw_spirograph(5)

draw_shape(8)
screen.exitonclick()