from PyQt4 import QtGui, QtCore
from models.Data import list_of_users
import MainScreen

class Screen(QtGui.QWidget):
    def __init__(self, user):
        self.user = user
        super(Screen, self).__init__()
        self.layout = QtGui.QVBoxLayout()
        self.setLayout(self.layout)
        self.initUI()
    def initUI(self):
        self.setWindowTitle("QuizApp")
        self.setFixedSize(500,500)
        self.Label = QtGui.QLabel("User Account")
        self.Label.setStyleSheet("""
                QLabel { 
                    font-size :  20px;
                    color: rgb(45, 188, 45); 
                    font-weight: bold; 
                }
            """)
        self.layout.addWidget(self.Label)
        self.welcome = QtGui.QLabel("WELCOME " + str(self.user.userName) + " !")
        self.welcome.setStyleSheet("""
                QLabel { 
                    font-size :  18px;
                    color: rgb(188, 45, 45); 
                    font-weight: bold; 
                }
            """)
        self.layout.addWidget(self.welcome)
        self.btnsWrapper = QtGui.QWidget()
        self.btnsWrapper.layout = QtGui.QVBoxLayout()
        self.btnsWrapper.setLayout(self.btnsWrapper.layout)
        self.layout.addWidget(self.btnsWrapper)
        self.initSubmitAnswersBtn()

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
        self.SubmitAnswersBtn.clicked.connect(self.SubmitAnswers)
        self.btnsWrapper.layout.addWidget(self.SubmitAnswersBtn, 1, QtCore.Qt.AlignRight)

    def SubmitAnswers(self):
        pass