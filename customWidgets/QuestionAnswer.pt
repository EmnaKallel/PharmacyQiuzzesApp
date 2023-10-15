from PyQt4 import QtGui, QtCore

class QuestionAnswerWidget(QtGui.QWidget):
    def __init__(self, question):
        super(QuestionAnswerWidget, self).__init__()
        self.question = question
        self.userResponse = None
        self.initUI()
        
    def initUI(self):
        self.layout = QtGui.QVBoxLayout()
        self.setLayout(self.layout)
        self.layout.setContentsMargins(0, 2, 0, 0)
        
        questionWrapper = QtGui.QWidget()
        questionWrapper.setProperty('class', 'bottomseparator')
        #to add a line only at the bottom use : "border-bottom : 1px solid black;""
        questionWrapper.setStyleSheet("""
            .bottomseparator{
                border : 1px solid black;
                border-radius: 8px;
                background-color: #E2E7F8;
                padding: 15px;
            }
        """)
        
        questionWrapper.layout = QtGui.QVBoxLayout()
        questionWrapper.setLayout(questionWrapper.layout)
        self.QuestionLabel = QtGui.QLabel("Question : " + str(self.question.Question))
        self.QuestionLabel.setStyleSheet("""
            QLabel { 
                font-size :  16px;
                font-weight: bold;
            }
        """)
        questionWrapper.layout.addWidget(self.QuestionLabel)
        self.ResponseLabel = QtGui.QLabel("Response : ")
        self.ResponseLabel.setStyleSheet("""
            QLabel { 
                font-size :  16px;
                font-weight: bold;
            }
        """)
        questionWrapper.layout.addWidget(self.ResponseLabel)
        self.btnsResponseWrapper = QtGui.QWidget()
        self.btnsResponseWrapper.layout = QtGui.QHBoxLayout()
        self.btnsResponseWrapper.setLayout(self.btnsResponseWrapper.layout)
        questionWrapper.layout.addWidget(self.btnsResponseWrapper)
        self.initYesBtn()
        self.initNoBtn()
        self.layout.addWidget(questionWrapper)
    
    def initYesBtn(self):
        self.YesBtn = QtGui.QRadioButton("Yes")
        self.YesBtn.setCursor(QtCore.Qt.PointingHandCursor)
        self.YesBtn.clicked.connect(self.YesBtnSystem)
        self.btnsResponseWrapper.layout.addWidget(self.YesBtn)

    def initNoBtn(self):
        self.NoBtn = QtGui.QRadioButton("No")
        self.NoBtn.setCursor(QtCore.Qt.PointingHandCursor)
        self.NoBtn.clicked.connect(self.NoBtnSystem)
        self.btnsResponseWrapper.layout.addWidget(self.NoBtn)
        
    def YesBtnSystem(self):
        self.userResponse = True

    def NoBtnSystem(self):
        self.userResponse = False
    
    def isCorrect(self):
        return (self.userResponse == self.question.Response)
        