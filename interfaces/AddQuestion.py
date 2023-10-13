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
        self.adminResponse = None
        self.initUI()
    def initUI(self):
        self.setWindowTitle("Add Question")
        self.setFixedSize(350,500)
        self.QuestionLabel = QtGui.QLabel("Enter Question Detail : ")
        self.QuestionLabel.setStyleSheet("""
                QLabel { 
                    font-weight: bold; 
                }
            """)
        self.layout.addWidget(self.QuestionLabel)
        self.QuestionField = QtGui.QLineEdit("", self)
        self.layout.addWidget(self.QuestionField)
        self.ResponseLabel = QtGui.QLabel("Enter The Response : ")
        self.ResponseLabel.setStyleSheet("""
                QLabel { 
                    font-weight: bold; 
                }
            """)
        self.layout.addWidget(self.ResponseLabel)

        self.btnsResponseWrapper = QtGui.QWidget()
        self.btnsResponseWrapper.layout = QtGui.QHBoxLayout()
        self.btnsResponseWrapper.setLayout(self.btnsResponseWrapper.layout)
        self.layout.addWidget(self.btnsResponseWrapper)
        self.initYesBtn()
        self.initNoBtn()

        self.NoteLabel = QtGui.QLabel("Enter The Note : ")
        self.NoteLabel.setStyleSheet("""
                QLabel { 
                    font-weight: bold; 
                }
            """)
        self.layout.addWidget(self.NoteLabel)
        self.NoteField = QtGui.QLineEdit("", self)
        int_validator = QtGui.QIntValidator()
        self.NoteField.setValidator(int_validator)
        self.layout.addWidget(self.NoteField)
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
        self.initCancelBtn()

    def initCancelBtn(self):
        self.CancelBtn = QtGui.QPushButton("Cancel")
        self.CancelBtn.setCursor(QtCore.Qt.PointingHandCursor)
        self.CancelBtn.setStyleSheet(
            """
                QPushButton { 
                    height: 30px; 
                    background-color: #485EB0; 
                    font-weight: bold; 
                    border-radius:15px;
                    padding: 3px 10px;
                }
                QPushButton:hover {
                    background-color: #7CB1C7; 
                }
            """
        )
        self.CancelBtn.clicked.connect(self.CancelBtnSystem)
        self.btnsWrapper.layout.addWidget(self.CancelBtn)

    def CancelBtnSystem(self):
        self.callScreen.show()
        self.close()

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
        self.adminResponse = True

    def NoBtnSystem(self):
        self.adminResponse = False


    def initSubmitBtn(self):
        self.SubmitBtn = QtGui.QPushButton("Submit")
        self.SubmitBtn.setCursor(QtCore.Qt.PointingHandCursor)
        self.SubmitBtn.setStyleSheet(
            """
                QPushButton { 
                    height: 30px; 
                    background-color: #4AAD67; 
                    font-weight: bold; 
                    border-radius:15px;
                    padding: 3px 10px;
                }
                QPushButton:hover {
                    background-color: #7CC7B7; 
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
            self.adminResponse!= None and
            self.NoteField.text()!=""    
        ):
            list_of_questions.append(
                Quiz(
                    self.QuestionField.text(),
                    self.adminResponse,
                    int(self.NoteField.text()),
                )
            )
            return True
        else :
            self.errorLabel.setText("Please fill in all fields")
        return False