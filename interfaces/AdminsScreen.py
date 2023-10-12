from PyQt4 import QtGui, QtCore
from models.Data import list_of_users
from models.Data import list_of_questions
from models.Quiz import Quiz
from models.User import User
import MainScreen
import AddQuestion
import AddUser

class Screen(QtGui.QWidget):
    def __init__(self, admin):
        super(Screen, self).__init__()
        self.admin = admin
        self.layout = QtGui.QVBoxLayout()
        self.setLayout(self.layout)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QuizApp")
        self.setFixedSize(700,700)
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
        self.LogOutBtn.clicked.connect(self.LogOutSystem)
        self.headerWrapper.layout.addWidget(self.LogOutBtn, 1, QtCore.Qt.AlignRight)

    def LogOutSystem(self):
        self.MainScreen = MainScreen.Screen()
        self.MainScreen.show()
        self.close()

    def initDividedWindows(self):
        self.dividedWidget = QtGui.QWidget()
        self.dividedWidget.layout = QtGui.QHBoxLayout()
        self.dividedWidget.setLayout(self.dividedWidget.layout)

        self.leftWindow = QtGui.QScrollArea()
        self.leftWindow.layout = QtGui.QVBoxLayout()
        self.leftWindow.setLayout(self.leftWindow.layout)
        self.leftWindow.setMinimumSize(200,200)
        self.initLeftWindow()
        self.dividedWidget.layout.addWidget(self.leftWindow)

        self.rightWindow = QtGui.QScrollArea()
        self.rightWindow.layout = QtGui.QVBoxLayout()
        self.rightWindow.setLayout(self.rightWindow.layout)
        self.rightWindow.setMinimumSize(200,200)
        self.initRightWindow()
        self.dividedWidget.layout.addWidget(self.rightWindow)

        self.layout.addWidget(self.dividedWidget)

    def initLeftWindow(self):
        self.leftWindow.Label1 = QtGui.QLabel("List Of Users : ")
        self.leftWindow.Label1.setStyleSheet("""
                QLabel { 
                    font-size :  25px;
                }
            """)
        self.leftWindow.layout.addWidget(self.leftWindow.Label1)

        for user in list_of_users :
            userWrapper = QtGui.QWidget()
            userWrapper.layout = QtGui.QHBoxLayout()
            userWrapper.setLayout(userWrapper.layout)
            
            self.leftWindow.userNameLabel = QtGui.QLabel(str(user.userName))
            self.leftWindow.userNameLabel.setStyleSheet("""
                QLabel { 
                    font-size :  20px;
                }
            """)
            userWrapper.layout.addWidget(self.leftWindow.userNameLabel, 1)
            self.initXBtn(userWrapper, user)
            self.leftWindow.layout.addWidget(userWrapper)

        self.leftWindow.btnsWrapper = QtGui.QWidget()
        self.leftWindow.btnsWrapper.layout = QtGui.QHBoxLayout()
        self.leftWindow.btnsWrapper.setLayout(self.leftWindow.btnsWrapper.layout)
        self.leftWindow.layout.addWidget(self.leftWindow.btnsWrapper)
        self.initAddUserBtn()

    def initRightWindow(self):
        self.rightWindow.Label1 = QtGui.QLabel("List Of Questions : ")
        self.rightWindow.Label1.setStyleSheet("""
                QLabel { 
                    font-size :  25px;
                }
            """)
        self.rightWindow.layout.addWidget(self.rightWindow.Label1)

        for question in list_of_questions :
            questionWrapper = QtGui.QWidget()
            questionWrapper.layout = QtGui.QVBoxLayout()
            questionWrapper.setLayout(questionWrapper.layout)
            self.rightWindow.QuestionLabel = QtGui.QLabel("Question : " + str(question.Question))
            self.rightWindow.QuestionLabel.setStyleSheet("""
                QLabel { 
                    font-size :  16px;
                }
            """)
            questionWrapper.layout.addWidget(self.rightWindow.QuestionLabel)
            self.rightWindow.ResponseLabel = QtGui.QLabel("Response : " + ("Yes" if question.Response else "No"), self.rightWindow)
            self.rightWindow.ResponseLabel.setStyleSheet("""
                QLabel { 
                    font-size :  16px;
                }
            """)
            questionWrapper.layout.addWidget(self.rightWindow.ResponseLabel)
            self.rightWindow.EspacementLabel = QtGui.QLabel("--------------------------------------------", self.rightWindow)
            self.rightWindow.EspacementLabel.setStyleSheet("""
                QLabel { 
                    font-size :  15px;
                }
            """)
            questionWrapper.layout.addWidget(self.rightWindow.EspacementLabel)
            self.rightWindow.layout.addWidget(questionWrapper)

        self.rightWindow.btnsWrapper = QtGui.QWidget()
        self.rightWindow.btnsWrapper.layout = QtGui.QHBoxLayout()
        self.rightWindow.btnsWrapper.setLayout(self.rightWindow.btnsWrapper.layout)
        self.rightWindow.layout.addWidget(self.rightWindow.btnsWrapper)
        self.initAddQuestionBtn()

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

    def initAddQuestionBtn(self):
        self.rightWindow.AddQuestionBtn = QtGui.QPushButton("+ Add Question")
        self.rightWindow.AddQuestionBtn.setStyleSheet(
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
        self.rightWindow.AddQuestionBtn.clicked.connect(self.initAddQuestionSystem)
        self.rightWindow.btnsWrapper.layout.addWidget(self.rightWindow.AddQuestionBtn, 1, QtCore.Qt.AlignCenter)
    
    def initAddUserSystem(self):
        self.AddUserScreen = AddUser.Screen(self)
        self.AddUserScreen.show()
        self.close()
        
    def resetUserList(self):
        while self.leftWindow.layout.count():
            item = self.leftWindow.layout.takeAt(0)
            widget = item.widget()
            self.leftWindow.layout.removeWidget(widget)
            widget.setParent(None)
            widget.deleteLater()
        self.initLeftWindow()

    def initAddQuestionSystem(self):
        self.AddQuestionScreen = AddQuestion.Screen(self)
        self.AddQuestionScreen.show()
        self.close()

    def resetQuestionsList(self):
        while self.rightWindow.layout.count():
            item = self.rightWindow.layout.takeAt(0)
            widget = item.widget()
            self.rightWindow.layout.removeWidget(widget)
            widget.setParent(None)
            widget.deleteLater()
        self.initRightWindow()

    def initXBtn(self, userWrapper, user):
        Xbtn = QtGui.QPushButton("X")
        Xbtn.user = user
        Xbtn.setStyleSheet(
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
        Xbtn.clicked.connect(self.XBtnSystem)
        userWrapper.layout.addWidget(Xbtn, 1, QtCore.Qt.AlignRight)

    def XBtnSystem(self):
        list_of_users.remove(self.sender().user)
        while self.leftWindow.layout.count():
            item = self.leftWindow.layout.takeAt(0)
            widget = item.widget()
            self.leftWindow.layout.removeWidget(widget)
            widget.setParent(None)
            widget.deleteLater()
        self.initLeftWindow()
