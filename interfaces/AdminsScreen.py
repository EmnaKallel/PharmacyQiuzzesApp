from PyQt4 import QtGui, QtCore
from models.Data import list_of_users
import MainScreen

class Screen(QtGui.QWidget):
    def __init__(self, admin):
        super(Screen, self).__init__()
        self.admin = admin
        self.layout = QtGui.QVBoxLayout()
        self.setLayout(self.layout)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QuizApp")
        self.setFixedSize(500,500)
        self.headerWrapper = QtGui.QWidget()
        self.headerWrapper.layout = QtGui.QHBoxLayout()
        self.headerWrapper.setLayout(self.headerWrapper.layout)
        self.Label = QtGui.QLabel("Admin Account")
        self.Label.setStyleSheet("""
                QLabel { 
                    font-size :  20px;
                    color: rgb(45, 188, 45); 
                    font-weight: bold; 
                }
            """)
        self.headerWrapper.layout.addWidget(self.Label, 1)
        self.initLogOutBtn()
        self.layout.addWidget(self.headerWrapper)
        self.welcome = QtGui.QLabel("WELCOME " + str(self.admin.userName) + " !")
        self.welcome.setStyleSheet("""
                QLabel { 
                    font-size :  18px;
                    color: rgb(188, 45, 45); 
                    font-weight: bold; 
                }
            """)
        self.layout.addWidget(self.welcome)
        self.initDividedWindows()
        

    def initLogOutBtn(self):
        self.LogOutBtn = QtGui.QPushButton("Log Out")
        self.LogOutBtn.setStyleSheet(
            """
                QPushButton { 
                    height: 30px; 
                    background-color: rgb(188, 45, 45); 
                    font-weight: bold; 
                    border-radius:15px;
                    padding: 3px 10px;
                }
                QPushButton:hover {
                    background-color: rgb(220, 45, 45); 
                }
            """
        )
        self.LogOutBtn.clicked.connect(self.LogOut)
        self.headerWrapper.layout.addWidget(self.LogOutBtn, 1, QtCore.Qt.AlignRight)

    def LogOut(self):
        pass

    def initDividedWindows(self):
        self.dividedWidget = QtGui.QWidget()
        self.dividedWidget.layout = QtGui.QHBoxLayout()
        self.dividedWidget.setLayout(self.dividedWidget.layout)

        self.leftWindow = QtGui.QScrollArea()
        self.leftWindow.layout = QtGui.QVBoxLayout()
        self.leftWindow.setLayout(self.leftWindow.layout)
        self.leftWindow.setMinimumSize(150,150)
        self.initListOfUsers()
        self.leftWindow.btnsWrapper = QtGui.QWidget()
        self.leftWindow.btnsWrapper.layout = QtGui.QHBoxLayout()
        self.leftWindow.btnsWrapper.setLayout(self.leftWindow.btnsWrapper.layout)
        self.leftWindow.layout.addWidget(self.leftWindow.btnsWrapper)
        self.initAddUserBtn()
        self.dividedWidget.layout.addWidget(self.leftWindow)

        self.rightWindow = QtGui.QScrollArea()
        self.rightWindow.layout = QtGui.QVBoxLayout()
        self.rightWindow.setLayout(self.rightWindow.layout)
        self.rightWindow.setMinimumSize(150,150)
        self.initListOfQuestions()
        self.dividedWidget.layout.addWidget(self.rightWindow)

        self.layout.addWidget(self.dividedWidget)

    def initListOfUsers(self):
        self.leftWindow.Label1 = QtGui.QLabel("List Of Users : ")
        self.leftWindow.Label1.setStyleSheet("""
                QLabel { 
                    font-size :  18px;
                }
            """)
        self.leftWindow.layout.addWidget(self.leftWindow.Label1)

    def initListOfQuestions(self):
        self.rightWindow.Label1 = QtGui.QLabel("List Of Questions : ")
        self.rightWindow.Label1.setStyleSheet("""
                QLabel { 
                    font-size :  18px;
                }
            """)
        self.rightWindow.layout.addWidget(self.rightWindow.Label1)

    def initAddUserBtn(self):
        self.leftWindow.AddUserBtn = QtGui.QPushButton("+ Add User")
        self.leftWindow.AddUserBtn.setStyleSheet(
            """
                QPushButton {
                    background-color: rgb(45, 188, 45); 
                    font-weight: bold; 
                    border-radius:15px;
                    padding: 5px 20px;
                }
                QPushButton:hover {
                    background-color: rgb(45, 220, 45); 
                }
            """
        )
        self.leftWindow.AddUserBtn.clicked.connect(self.initAddUserSystem)
        self.leftWindow.btnsWrapper.layout.addWidget(self.leftWindow.AddUserBtn, 1, QtCore.Qt.AlignCenter)
    
    def initAddUserSystem(self):
        pass