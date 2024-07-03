class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer=input(f"Q{self.question_number}. {current_question.text} (True/False): ")
        self.check_answer(answer,current_question.answer)

    def still_has_question(self):
        return (self.question_number<len(self.question_list))

    def check_answer(self,answer,current_answer):
        if answer==current_answer:
            self.score += 1
            print("정답입니다!")
        else:
            print("오답입니다.")

