from PyQt4 import QtGui, QtCore

class QuestionAnswersWidget(QtGui.QWidget):
    def __init__(self, question):
        super(QuestionAnswersWidget, self).__init__()
        self.question = question
        self.checkBoxes = []
        self.initUI()
        
    def initUI(self):
        self.layout = QtGui.QVBoxLayout()
        self.setLayout(self.layout)
        self.layout.setContentsMargins(0, 2, 0, 0)
        
        questionWrapper = QtGui.QWidget()
        questionWrapper.setProperty('class', 'questionsseparator')
        questionWrapper.setStyleSheet("""
            .questionsseparator{
                border : 1px solid black;
                border-radius: 8px;
                background-color: #E2E7F8;
                padding: 15px;
            }
        """)
        
        questionWrapper.layout = QtGui.QVBoxLayout()
        questionWrapper.setLayout(questionWrapper.layout)

        self.QuestionLabel = QtGui.QLabel("Question : " + str(self.question.question))
        self.QuestionLabel.setStyleSheet("""
            QLabel { 
                font-size :  16px;
                font-weight: bold;
            }
        """)
        questionWrapper.layout.addWidget(self.QuestionLabel)

        self.ResponseLabel = QtGui.QLabel("Responses : ")
        self.ResponseLabel.setStyleSheet("""
            QLabel { 
                font-size :  16px;
                font-weight: bold;
            }
        """)
        questionWrapper.layout.addWidget(self.ResponseLabel)

        self.btnsResponseWrapper = QtGui.QWidget()
        self.btnsResponseWrapper.layout = QtGui.QVBoxLayout()
        self.btnsResponseWrapper.setLayout(self.btnsResponseWrapper.layout)
        questionWrapper.layout.addWidget(self.btnsResponseWrapper)
        self.initResponsesBtn()

        self.layout.addWidget(questionWrapper)

    def initResponsesBtn(self):
        for response in self.question.responses :
            checkBoxBtn = QtGui.QCheckBox(response.label)
            checkBoxBtn.response = response
            self.checkBoxes.append(checkBoxBtn)
            checkBoxBtn.setCursor(QtCore.Qt.PointingHandCursor)
            self.btnsResponseWrapper.layout.addWidget(checkBoxBtn)
            
    def checkAnswerCorrectness(self):
        grade = 0
        for checkbox in self.checkBoxes:
            if(checkbox.response.isCorrect == checkbox.isChecked()):
                grade = grade + 0.25
        return grade