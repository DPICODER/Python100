from question_model import QuestionModel
from data import question_data
from quiz_brain import QuizBrain


question_bank = []
for questions in question_data:
    question_text = questions['text']
    question_answer = questions['answer']
    new_question = QuestionModel(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)


while quiz.still_has_questions():
    quiz.next_question()

print("You Have Completed the QUIZ ")
print(f"Your Final Score is {quiz.score} / {quiz.question_no}")