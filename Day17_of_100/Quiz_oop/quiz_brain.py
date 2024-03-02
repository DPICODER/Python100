class QuizBrain:
    def __init__(self, q_list):
        self.question_no = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self):
        return self.question_no < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_no]
        self.question_no += 1
        answer = input(f"Q.{self.question_no} : {current_question.text} (True / False)")
        self.check_answer(answer, current_question.answer)

    def check_answer(self, answer, correct_ans):
        if answer.lower() == correct_ans.lower():
            self.score += 1
            print("You Got it Right")

        else:
            print("That's Wrong")

        print(f"The Correct answer : {correct_ans}")
        print(f"Your Current Score : {self.score}/{self.question_no}")
        print("\n")
