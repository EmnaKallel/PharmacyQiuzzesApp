from PyQt4 import QtGui, QtCore
from models.Data import list_of_users
from models.Data import list_of_questions
import Style
import SubmitAnswers

class Screen(QtGui.QWidget):
    def __init__(self, callScreen):
        super(Screen, self).__init__()
        self.callScreen = callScreen 
        self.initUI()
    
    def initUI(self):
        self.layout = QtGui.QVBoxLayout()
        self.setLayout(self.layout)
        self.layout.setContentsMargins(0, 0, 0, 0)
        
        while (self.callScreen.layout.count()>1):
            widget = self.callScreen.layout.itemAt(1).widget()
            if(widget):
                self.callScreen.layout.removeWidget(widget)
                widget.setParent(None)
                widget.deleteLater()
        self.callScreen.layout.insertWidget(1, self)

        self.Label = QtGui.QLabel("User Account")
        self.Label.setStyleSheet("""
                QLabel { 
                    font-size :  20px;
                    color: rgb(45, 188, 45); 
                    font-weight: bold; 
                }
            """)
        self.layout.addWidget(self.Label)
        self.welcome = QtGui.QLabel("WELCOME " + str(self.callScreen.user.userName) + " !")
        self.welcome.setStyleSheet("""
                QLabel { 
                    font-size :  18px;
                    color: rgb(188, 45, 45); 
                    font-weight: bold; 
                }
            """)
        self.layout.addWidget(self.welcome)
        self.Label1 = QtGui.QLabel("List Of Questions : ")
        self.Label1.setStyleSheet("""
                QLabel { 
                    font-size :  25px;
                }
            """)
        self.layout.addWidget(self.Label1)

        for question in list_of_questions :
            questionWrapper = QtGui.QWidget()
            questionWrapper.layout = QtGui.QVBoxLayout()
            questionWrapper.setLayout(questionWrapper.layout)
            self.QuestionLabel = QtGui.QLabel("Question : " + str(question.Question))
            self.QuestionLabel.setStyleSheet("""
                QLabel { 
                    font-size :  16px;
                }
            """)
            questionWrapper.layout.addWidget(self.QuestionLabel)
            self.ResponseLabel = QtGui.QLabel("Response : ", self)
            self.ResponseLabel.setStyleSheet("""
                QLabel { 
                    font-size :  16px;
                }
            """)
            questionWrapper.layout.addWidget(self.ResponseLabel)
            self.btnsResponseWrapper = QtGui.QWidget()
            self.btnsResponseWrapper.layout = QtGui.QHBoxLayout()
            self.btnsResponseWrapper.setLayout(self.btnsResponseWrapper.layout)
            questionWrapper.layout.addWidget(self.btnsResponseWrapper)
            self.initYesBtn()
            self.initNoBtn()
            self.EspacementLabel = QtGui.QLabel("-----------------------------------------------------------------------------", self)
            self.EspacementLabel.setStyleSheet("""
                QLabel { 
                    font-size :  15px;
                }
            """)
            questionWrapper.layout.addWidget(self.EspacementLabel)
            self.layout.addWidget(questionWrapper)
        self.btnsWrapper = QtGui.QWidget()
        self.btnsWrapper.layout = QtGui.QVBoxLayout()
        self.btnsWrapper.setLayout(self.btnsWrapper.layout)
        self.layout.addWidget(self.btnsWrapper)
        self.initSubmitAnswersBtn()

    def initYesBtn(self):
        self.YesBtn = QtGui.QRadioButton("Yes")
        self.YesBtn.clicked.connect(self.YesBtnSystem)
        self.btnsResponseWrapper.layout.addWidget(self.YesBtn)

    def initNoBtn(self):
        self.NoBtn = QtGui.QRadioButton("No")
        self.NoBtn.clicked.connect(self.NoBtnSystem)
        self.btnsResponseWrapper.layout.addWidget(self.NoBtn)

    def initSubmitAnswersBtn(self):
        self.SubmitAnswersBtn = QtGui.QPushButton("Submit Answers")
        self.SubmitAnswersBtn.setStyleSheet(
            """
                QPushButton { 
                    height: 30px; 
                    background-color: rgb(188, 45, 45); 
                    font-weight: bold; 
                    border-radius:15px;
                    padding: 3px 20px;
                }
                QPushButton:hover {
                    background-color: rgb(220, 45, 45); 
                }
            """
        )
        self.SubmitAnswersBtn.clicked.connect(self.SubmitAnswersSystem)
        self.btnsWrapper.layout.addWidget(self.SubmitAnswersBtn, 1, QtCore.Qt.AlignRight)

    def SubmitAnswersSystem(self):
        self.SubmitAnswersScreen = SubmitAnswers.Screen(self)
        self.SubmitAnswersScreen.show()
        self.callScreen.close()

    def YesBtnSystem(self):
        pass

    def NoBtnSystem(self):
        pass
