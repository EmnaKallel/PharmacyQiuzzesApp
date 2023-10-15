class Test :
    id = 0
    def __init__(self, TestName, questions=[], successThreshold=0) :
        self.id = Test.id
        self.TestName = TestName
        self.questions = questions
        self.successThreshold = successThreshold
        Test.id = Test.id + 1
