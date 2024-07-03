from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


question_bank=[]
for key in question_data["results"]:
    question_text=key["question"]
    question_answer=key["correct_answer"]
    question=Question(question_text,question_answer)
    question_bank.append(question)

quizBrain=QuizBrain(question_bank)

while quizBrain.still_has_question():
    quizBrain.next_question()

print("---------------------------------")
print("모든 문제를 풀었습니다!")
print(f"최종 점수는 {quizBrain.score}/{quizBrain.question_number} 입니다.")
