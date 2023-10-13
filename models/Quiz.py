class Quiz :
    id = 0
    def __init__(self, Question, Response, Note) :
        self.id = Quiz.id
        self.Question = Question
        self.Response = Response
        self.Note = Note
        Quiz.id = Quiz.id + 1