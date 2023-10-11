from PyQt4 import QtGui, QtCore
from models.Data import list_of_questions
import MainScreen
import AdminsScreen
from models.Quiz import Quiz

class Screen(QtGui.QWidget):
    def __init__(self, callScreen):
        super(Screen, self).__init__()
        self.callScreen = callScreen
        self.layout = QtGui.QVBoxLayout()
        self.setLayout(self.layout)
        self.initUI()
    def initUI(self):
        self.setWindowTitle("Add Question")
        self.setFixedSize(350,500)
        self.QuestionLabel = QtGui.QLabel("Enter Question Detail : ")
        self.layout.addWidget(self.QuestionLabel)
        self.QuestionField = QtGui.QLineEdit("", self)
        self.layout.addWidget(self.QuestionField)
        self.ResponseLabel = QtGui.QLabel("Enter The Response : ")
        self.layout.addWidget(self.ResponseLabel)
        self.ResponseField = QtGui.QLineEdit("", self)
        self.layout.addWidget(self.ResponseField)
        self.errorLabel = QtGui.QLabel()
        self.errorLabel.setStyleSheet(
            """
                QLabel { 
                    color: rgb(188, 45, 45); 
                    font-weight: bold; 
                }
            """
        )
        self.layout.addWidget(self.errorLabel)
        self.btnsWrapper = QtGui.QWidget()
        self.btnsWrapper.layout = QtGui.QHBoxLayout()
        self.btnsWrapper.setLayout(self.btnsWrapper.layout)
        self.layout.addWidget(self.btnsWrapper)
        self.initSubmitBtn()

    def initSubmitBtn(self):
        self.SubmitBtn = QtGui.QPushButton("Submit")
        self.SubmitBtn.setStyleSheet(
            """
                QPushButton {
                    width:95px; 
                    height: 30px; 
                    background-color: rgb(45, 108, 75); 
                    font-weight: bold; 
                    border-radius:15px;
                }
                QPushButton:hover {
                    background-color: rgb(175, 220, 75); 
                }
            """
        )
        self.SubmitBtn.clicked.connect(self.initiateSubmit)
        self.btnsWrapper.layout.addWidget(self.SubmitBtn)

    def initiateSubmit (self):
        added = self.addQuestionSystem()
        if(added):
            self.callScreen.show()
            self.callScreen.resetQuestionsList()
            self.close()
        
    def addQuestionSystem(self):
        if(
            self.QuestionField.text()!="" and 
            self.ResponseField.text()!=""     
        ):
            list_of_questions.append(
                Quiz(
                    self.QuestionField.text(),
                    self.ResponseField.text()
                )
            )
            return True
        else :
            self.errorLabel.setText("Please fill in all fields")
        return False