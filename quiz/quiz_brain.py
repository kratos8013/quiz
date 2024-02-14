class Quiz_brain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q {self.question_number}:{question.text} (true/false) ")
        self.check_answer(answer, question.answer)

    def has_still_question(self):
        return self.question_number != len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("you got it right")
        else:
            print("you got it wrong")

        print(f"The correct answer is {correct_answer}")
        print(f"score : {self.score}/{self.question_number}")
        print()

