from PyQt4 import QtGui, QtCore
from models.Data import list_of_users
import UsersScreen
import SignIn

class Screen(QtGui.QWidget):
    def __init__(self):
        super(Screen, self).__init__()
        self.layout = QtGui.QVBoxLayout()
        self.setLayout(self.layout)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("PharmacyQuizzesApp")
        self.setFixedSize(400,250)
        self.Label0 = QtGui.QLabel("LOGIN PAGE")
        self.layout.addWidget(self.Label0)
        self.Label0.setAlignment(QtCore.Qt.AlignCenter)
        self.Label0.setStyleSheet("""
                QLabel { 
                    color: #2A7640; 
                    font-weight: bold; 
                }
            """)
        self.Label1 = QtGui.QLabel("User Name : ")
        self.Label1.setStyleSheet("""
                QLabel { 
                    font-weight: bold; 
                }
            """)
        self.layout.addWidget(self.Label1)
        self.userNameField = QtGui.QLineEdit("", self)
        self.layout.addWidget(self.userNameField)
        self.Label2 = QtGui.QLabel("Password : ")
        self.Label2.setStyleSheet("""
                QLabel { 
                    font-weight: bold; 
                }
            """)
        self.layout.addWidget(self.Label2)
        self.passwordField = QtGui.QLineEdit("", self)
        self.passwordField.setEchoMode(QtGui.QLineEdit.Password)
        self.layout.addWidget(self.passwordField)
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
        self.initLogInBtn()
        self.initSignInBtn()

    def initSignInBtn(self):
        self.SignInBtn = QtGui.QPushButton("Sign In")
        self.SignInBtn.setStyleSheet(
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
        self.SignInBtn.clicked.connect(self.initiateSignIn)
        self.btnsWrapper.layout.addWidget(self.SignInBtn)
    
    def initiateSignIn(self):
        self.SignInScreen = SignIn.Screen(self)
        self.SignInScreen.show()
        self.close()

    def initLogInBtn(self):
        self.LogInBtn = QtGui.QPushButton("Log In")
        self.LogInBtn.setCursor(QtCore.Qt.PointingHandCursor)
        self.LogInBtn.setStyleSheet(
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
        self.LogInBtn.clicked.connect(self.initiateLogIn)
        self.btnsWrapper.layout.addWidget(self.LogInBtn)
    
    def initiateLogIn(self):
        currentUser = self.LogInUserSysteme()
        """if (currentUser != None) :
            if(currentUser.isAdmin):
                self.AdminsScreen = AdminsScreen.Screen(currentUser)
                self.AdminsScreen.show()
                self.close()
            else:"""
        self.UsersScreen = UsersScreen.Screen(currentUser)
        self.UsersScreen.show()
        self.close()

    def LogInUserSysteme(self):
        userExists = False
        for user in list_of_users :
            if (self.userNameField.text() == user.userName and self.passwordField.text() == user.password):
                return user
            elif (self.userNameField.text() == user.userName):
                userExists = True
        if(userExists):
            self.errorLabel.setText("Wrong Password")
        else: 
            self.errorLabel.setText("User Don't Exist")
        return None