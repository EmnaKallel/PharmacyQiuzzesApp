class Quiz :
    id = 0
    def __init__(self, question, responses=[]) :
        self.id = Quiz.id
        self.question = question
        self.responses = responses
        Quiz.id = Quiz.id + 1

class QuestionOption :
    id = 0
    def __init__(self, label, isCorrect=False) :
        self.id = QuestionOption.id
        self.label = label
        self.isCorrect = isCorrect
        QuestionOption.id = QuestionOption.id + 1