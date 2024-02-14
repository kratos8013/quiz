from data import question_data
from question_model import Question
from quiz_brain import Quiz_brain

question_bank = []
for i in question_data:
    question_bank.append(Question(i["text"], i["answer"]))
quiz_brain1 = Quiz_brain(question_bank)

while quiz_brain1.has_still_question():
    quiz_brain1.next_question()

print(f"Your final score is {quiz_brain1.score}/{quiz_brain1.question_number}")



