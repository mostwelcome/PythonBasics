class Question:
    def __init__(self, qs, answer):
        self.qs = qs
        self.answer = answer


new_question = Question('first question', 'true')
print(new_question.answer)
