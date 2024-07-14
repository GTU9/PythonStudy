import tkinter as tk
import random

class SelectNumberGame:
    def __init__(self):
        self.select_num = []
        self.result = 0
        self.total_problems = 5  # 총 문제 수
        self.current_problem = 0  # 현재 문제 번호
        self.correct_answers = 0  # 정답 개수

    #문제 생성 로직
    def make_num(self):
        while True:
            temp = random.randint(100, 1000)  # 문제의 결과값 범위를 조정할 수 있습니다.
            temp_list = []
            for i in range(1, temp):
                if temp % i == 0 and i != 1:
                    temp_list.append(i)
            if len(temp_list) > 1:
                break

        num1 = random.choice(temp_list)
        num2 = temp // num1

        self.select_num = [num1, num2]
        self.result = temp

    #정답 확인
    def check_answer(self, num1, num2):
        actual_num1, actual_num2 = self.select_num
        if num1 == actual_num1 and num2 == actual_num2:
            return True
        return False

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.game = SelectNumberGame()
        self.create_widgets()
        self.num1 = None
        self.num2 = None
        self.result = None
        self.current_problem = 0  
        self.canvas.pack_forget()  
        for button in self.answer_buttons:
            button.pack_forget()  #시작 버튼을 누르기 전 항목들 숨김

    #UI 설정
    def create_widgets(self):
        self.start_button = tk.Button(self.master, text="시작", command=self.start_game)
        self.start_button.pack()

        self.canvas = tk.Canvas(self.master, width=300, height=100, bg='white')  # 초기 배경색은 흰색
        self.quiz_text_id = self.canvas.create_text(150, 30, text="", font=("Helvetica", 18), anchor='center')

        self.answer_label = tk.Label(self.master, text="올바른 인수 선택 게임")
        self.answer_label.pack()

        self.answer_buttons = []
        for i in range(4):
            button = tk.Button(self.master, text="", command=lambda idx=i: self.select_button(idx))
            self.answer_buttons.append(button)

        self.result_label = tk.Label(self.master, text="", font=("Helvetica", 14))

    #게임 시작
    def start_game(self):
        self.start_button.configure(state=tk.DISABLED)  # 시작 버튼 비활성화
        self.canvas.pack()
        for button in self.answer_buttons:
            button.pack()
        self.next_problem()

    #문제 생성
    def create_problem(self):
        self.game.make_num()
        self.num1 = None
        self.num2 = None
        self.result = self.game.result  # 문제의 결과값 설정
        self.update_canvas()

        num1, num2 = self.game.select_num
        answer_choices = [num1, num2] + random.sample(range(1, 100), 2)
        random.shuffle(answer_choices)

        for i in range(4):
            self.answer_buttons[i].configure(text=answer_choices[i], state=tk.NORMAL)

    #캔버스 값 업데이트
    def update_canvas(self):
        if self.num1 is None or self.num2 is None:
            self.canvas.itemconfig(self.quiz_text_id, text=f"_ X _ = {self.result}")
        else:
            self.canvas.itemconfig(self.quiz_text_id, text=f"{self.num1} X {self.num2} = {self.result}")

    #두가지 버튼 선택 후 문제 위에 출력
    def select_button(self, idx):
        selected_value = int(self.answer_buttons[idx]['text'])
        if self.num1 is None:
            self.num1 = selected_value
        elif self.num2 is None:
            self.num2 = selected_value
            if self.num1 is not None and self.num2 is not None:
                self.check_answer()

        self.update_canvas()

    #입력한 값이 올바른지 확인
    def check_answer(self):
        if self.game.check_answer(self.num1, self.num2):
            self.canvas.configure(bg='green')  # 정답일 경우 초록색 배경으로변경
            self.game.correct_answers += 1
        else:
            self.canvas.configure(bg='red')  # 오답일 경우 빨간색 배경으로변경

        self.current_problem += 1

        # 다섯 문제를 모두 풀었으면 게임 종료
        if self.current_problem < self.game.total_problems:
            self.after(1000, self.next_problem) 
        else:
            self.end_game()

    #다음 문제 초기화
    def next_problem(self):
        self.num1 = None
        self.num2 = None
        self.canvas.configure(bg='white')  # 배경을 다시 흰색으로 설정
        self.create_problem()  # 다음 문제 생성

    #게임 결과 출력
    def end_game(self):
        self.result_label.configure(text=f"총 {self.game.total_problems}문제 중 {self.game.correct_answers}문제 맞추셨습니다!")
        self.result_label.pack()

#실행
if __name__ == "__main__":
    root = tk.Tk()
    root.title(" 올바른 인수 선택 게임")
    app = Application(master=root)
    app.mainloop()
