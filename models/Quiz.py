class Quiz :
    id = 0
    def __init__(self, Question, Response) :
        self.id = Quiz.id
        self.Question = Question
        self.Response = Response
        Quiz.id = Quiz.id + 1