class QuizBrain:
    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = questions_list

    def next_question(self):
        self.question_number += 1
        choice = input(
            f'qs{self.question_number} : {self.questions_list[self.question_number-1].qs} . True or False? ')
        return choice

    def still_have_questions(self):
        if self.question_number < len(self.questions_list):
            return True
        return False

    def check_answer(self, answer):
        if self.questions_list[self.question_number-1].answer == answer.title():
            return True
        return False
