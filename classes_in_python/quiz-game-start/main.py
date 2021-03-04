from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_model = Question(question.get('text'), question.get('answer'))
    question_bank.append(question_model)

quiz_brain = QuizBrain(question_bank)
count = 0
score = 0
while True:
    if not quiz_brain.still_have_questions():
        break
    else:
        answer = quiz_brain.next_question()
        if quiz_brain.check_answer(answer):
            score += 1
            print('You got it right')
        print(
            f'Your currentscore is: {score}')
