class Subject :
    id = 0
    def __init__(self, subjectName, tests=[]) :
        self.subjectName = subjectName
        self.tests = tests
        self.courses = []
        self.id = Subject.id
        Subject.id = Subject.id + 1
