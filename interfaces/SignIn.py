from PyQt4 import QtGui, QtCore
from models.Data import list_of_users
import MainScreen
from models.User import User

class Screen(QtGui.QWidget):
    def __init__(self, callScreen):
        super(Screen, self).__init__()
        self.callScreen = callScreen
        self.layout = QtGui.QVBoxLayout()
        self.setLayout(self.layout)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Sign In")
        self.setFixedSize(350,400)
        self.titleLabel = QtGui.QLabel("Enter Your Informations : ")
        self.titleLabel.setStyleSheet("""
                QLabel { 
                    font-weight: bold; 
                }
            """)
        self.layout.addWidget(self.titleLabel)
        self.FullNameLabel = QtGui.QLabel("Full Name : ")
        self.FullNameLabel.setStyleSheet("""
                QLabel { 
                    font-weight: bold; 
                }
            """)
        self.layout.addWidget(self.FullNameLabel)
        self.FullNameField = QtGui.QLineEdit("", self)
        regex_validator1 = QtGui.QRegExpValidator(QtCore.QRegExp('^[a-zA-Z\s]+$'))
        self.FullNameField.setValidator(regex_validator1)
        self.layout.addWidget(self.FullNameField)
        self.PasswordLabel = QtGui.QLabel("Password : ")
        self.PasswordLabel.setStyleSheet("""
                QLabel { 
                    font-weight: bold; 
                }
            """)
        self.layout.addWidget(self.PasswordLabel)
        self.PasswordField = QtGui.QLineEdit("", self)
        self.PasswordField.setEchoMode(QtGui.QLineEdit.Password)
        self.layout.addWidget(self.PasswordField)
        self.ConfirmPasswordLabel = QtGui.QLabel("Confirm Your Password : ")
        self.ConfirmPasswordLabel.setStyleSheet("""
                QLabel { 
                    font-weight: bold; 
                }
            """)
        self.layout.addWidget(self.ConfirmPasswordLabel)
        self.ConfirmPasswordField = QtGui.QLineEdit("", self)
        self.ConfirmPasswordField.setEchoMode(QtGui.QLineEdit.Password)
        self.layout.addWidget(self.ConfirmPasswordField)
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
        self.initResetBtn()
        self.initCancelBtn()

    def initCancelBtn(self):
        self.CancelBtn = QtGui.QPushButton("Cancel")
        self.CancelBtn.setCursor(QtCore.Qt.PointingHandCursor)
        self.CancelBtn.setStyleSheet(
            """
                QPushButton { 
                    width:95px;
                    height: 30px; 
                    background-color: #485EB0; 
                    font-weight: bold; 
                    border-radius:15px;
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

    def initSubmitBtn(self):
        self.SubmitBtn = QtGui.QPushButton("Submit")
        self.SubmitBtn.setCursor(QtCore.Qt.PointingHandCursor)
        self.SubmitBtn.setStyleSheet(
            """
                QPushButton {
                    width:95px; 
                    height: 30px; 
                    background-color: #4AAD67; 
                    font-weight: bold; 
                    border-radius:15px;
                }
                QPushButton:hover {
                    background-color: #7CC7B7; 
                }
            """
        )
        self.SubmitBtn.clicked.connect(self.initiateSubmit)
        self.btnsWrapper.layout.addWidget(self.SubmitBtn)

    def initResetBtn(self):
        self.ResetBtn = QtGui.QPushButton("Reset")
        self.ResetBtn.setCursor(QtCore.Qt.PointingHandCursor)
        self.ResetBtn.setStyleSheet(
            """
                QPushButton {
                    width:95px; 
                    height: 30px; 
                    background-color: #BB6CB9; 
                    font-weight: bold; 
                    border-radius:15px;
                }
                QPushButton:hover {
                    background-color: #EDB1D4; 
                }
            """
        )
        self.ResetBtn.clicked.connect(self.initiateReset)
        self.btnsWrapper.layout.addWidget(self.ResetBtn)
    
    def initiateSubmit (self):
        added = self.addUserSystem()
        if(added):
            self.callScreen.show()
            self.close()

    def initiateReset (self):
        self.FullNameField.setText("")
        self.PasswordField.setText("")
        self.ConfirmPasswordField.setText("")

    def addUserSystem(self):
        if(
            self.FullNameField.text()!="" and 
            self.PasswordField.text()!="" and 
            self.ConfirmPasswordField.text()!=""
        ):
            if(self.PasswordField.text() == self.ConfirmPasswordField.text()):
                list_of_users.append(
                    User(
                        self.FullNameField.text(),
                        self.ConfirmPasswordField.text(),
                    )
                )
                return True
            else :
                self.errorLabel.setText("Check Passwords")
        else :
            self.errorLabel.setText("Please fill in all fields")
        return False