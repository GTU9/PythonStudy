from turtle import Turtle, Screen
import random

screen = Screen()

screen.setup(width=500, height=500)
screen.delay(0)
colors = ['red', 'orange', 'green', 'blue']
shapes = ['circle', 'square', 'turtle']

turtle_list = []


def show_question(color, shape):  # screen에 선행 질문을 그림
    turtle = Turtle(visible=False)
    turtle.penup()
    turtle.goto(0, -200)
    turtle.write(f"{color} {shape}은(는) 몇개 일까요?", align='center', font=('Arial', 24, 'normal'))


def make_turtle(shape):  # 터틀생성
    turtle = Turtle(visible=False)
    turtle.shape(shape)
    turtle.speed(0)
    turtle.penup()
    turtle.goto(random.randint(-200, 200), random.randint(-100, 200))
    turtle.color(random.choice(colors))
    turtle.showturtle()

    return turtle


def hide_turtle():  #모든 turtle을 숨김
    for turtle in turtle_list:
        turtle.hideturtle()


def check_answer(correct_color, correct_shape, correct):  # 정답 확인후 메세지 출력
    answer = int(screen.textinput("", f"{correct_color} {correct_shape}은(는) 몇개 일까요?"))
    turtle = Turtle(visible=False)
    turtle.penup()
    turtle.goto(0, 0)
    turtle.write(f"화면에 나타난 {correct_color} {correct_shape}은(는) {correct}개", align='center',
                 font=('Arial', 16, 'normal'))
    turtle.goto(0, -50)
    if (answer == correct):
        turtle.write(f"작성하신 답은 {answer}개 정답입니다!", align='center', font=('Arial', 16, 'normal'))
    else:
        turtle.write(f"작성하신 답은 {answer}개 오답입니다!", align='center', font=('Arial', 16, 'normal'))


def normal_mode():  # 노말 모드 게임실행, 모양을 turtle로 고정

    correct_color = random.choice(colors)
    correct_shape = "turtle"
    correct = 0

    show_question(correct_color, correct_shape)
    for i in range(20):
        turtle_list.append(make_turtle("turtle"))
        if turtle_list[i].pencolor() == correct_color and turtle_list[i].shape() == correct_shape:
            correct += 1

    screen.ontimer(hide_turtle, 3500)
    screen.ontimer(lambda: check_answer(correct_color, correct_shape, correct), 4000)

def hard_mode():  # 하드 모드 게임실행
    correct_color = random.choice(colors)  #랜덤으로 정답 색을 선택
    correct_shape = random.choice(shapes)  #랜덤으로 정답 모양을 선택
    correct = 0  #정답에 해당하는 turtle 숫자

    show_question(correct_color, correct_shape)  #선택된 색과 모양을 출력
    for i in range(30):  #turtle을 30개 생성하고  screen안에 무작위로 배치
        turtle_list.append(make_turtle(random.choice(shapes)))  #생성된 각 turtle의 정보를 리스트에 저장
        if turtle_list[i].pencolor() == correct_color and turtle_list[
            i].shape() == correct_shape:  #선택된 색과 모양이 생성된 turtle과 일치하면 correct 스택 증가
            correct += 1

    screen.ontimer(hide_turtle, 2500)  #2.5초 후 모든 turtle을 숨김
    screen.ontimer(lambda: check_answer(correct_color, correct_shape, correct), 3000)  #사용자가 답을 입력후 결과 출력

# def continue_game():
#     cont=screen.textinput("","계속하시겠습니까? yes or no")
#     if cont == "yes":
#         return True
#     else:
#         return False

def main(): #게임실행
    select_level = int(screen.textinput("", "난이도를 선택해주세요 (normal mode)1/(hard mode)2 :"))
    if select_level == 1:
        normal_mode()

    if select_level == 2:
        hard_mode()

main()

screen.exitonclick()
