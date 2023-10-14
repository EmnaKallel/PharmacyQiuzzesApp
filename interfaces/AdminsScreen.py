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
        self.setWindowTitle("PharmacyQuizzesApp")
        self.setFixedSize(700,700)
        self.headerWrapper = QtGui.QWidget()
        self.headerWrapper.layout = QtGui.QHBoxLayout()
        self.headerWrapper.setLayout(self.headerWrapper.layout)
        self.Label = QtGui.QLabel("Admin Account")
        self.Label.setStyleSheet("""
                QLabel { 
                    font-size :  20px;
                    color: #2A7640; 
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
                    color: #6648B0; 
                    font-weight: bold; 
                }
            """)
        self.layout.addWidget(self.welcome)
        self.initDividedWindows()
        

    def initLogOutBtn(self):
        self.LogOutBtn = QtGui.QPushButton("Log Out")
        self.LogOutBtn.setCursor(QtCore.Qt.PointingHandCursor)
        self.LogOutBtn.setStyleSheet(
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
        self.leftWindow.Wrapper = QtGui.QWidget()
        self.leftWindow.Wrapper.layout = QtGui.QVBoxLayout()
        self.leftWindow.Wrapper.setLayout(self.leftWindow.Wrapper.layout)
        self.leftWindow.Wrapper.Label1 = QtGui.QLabel("List Of Users : ")
        self.leftWindow.Wrapper.Label1.setStyleSheet("""
                QLabel { 
                    font-size :  25px;
                    color : #9A48B0;
                    font-weight: bold;
                }
            """)
        self.leftWindow.Wrapper.layout.addWidget(self.leftWindow.Wrapper.Label1)

        for user in list_of_users :
            userWrapper = QtGui.QWidget()
            userWrapper.layout = QtGui.QHBoxLayout()
            userWrapper.setLayout(userWrapper.layout)
            userWrapper.setProperty('class', 'bottomseparator')
            userWrapper.setStyleSheet("""
                .bottomseparator{
                    border : 1px solid black;
                    border-radius: 8px;
                    background-color: #E2E7F8;
                }
            """)
            
            self.leftWindow.Wrapper.userNameLabel = QtGui.QLabel(str(user.userName))
            self.leftWindow.Wrapper.userNameLabel.setStyleSheet("""
                QLabel { 
                    font-size :  20px;
                    font-weight: bold;
                }
            """)
            userWrapper.layout.addWidget(self.leftWindow.Wrapper.userNameLabel, 1)
            self.initXBtn(userWrapper, user)
            self.leftWindow.Wrapper.layout.addWidget(userWrapper)

        self.leftWindow.Wrapper.btnsWrapper = QtGui.QWidget()
        self.leftWindow.Wrapper.btnsWrapper.layout = QtGui.QHBoxLayout()
        self.leftWindow.Wrapper.btnsWrapper.setLayout(self.leftWindow.Wrapper.btnsWrapper.layout)
        self.leftWindow.Wrapper.layout.addWidget(self.leftWindow.Wrapper.btnsWrapper)
        self.initAddUserBtn()
        self.leftWindow.setWidget(self.leftWindow.Wrapper)

    def initRightWindow(self):
        self.rightWindow.Wrapper = QtGui.QWidget()
        self.rightWindow.Wrapper.layout = QtGui.QVBoxLayout()
        self.rightWindow.Wrapper.setLayout(self.rightWindow.Wrapper.layout)
        self.rightWindow.Wrapper.Label1 = QtGui.QLabel("List Of Questions : ")
        self.rightWindow.Wrapper.Label1.setStyleSheet("""
                QLabel { 
                    font-size :  25px;
                    color : #9A48B0;
                    font-weight: bold;
                }
            """)
        self.rightWindow.Wrapper.layout.addWidget(self.rightWindow.Wrapper.Label1)

        for question in list_of_questions :
            questionWrapper = QtGui.QWidget()
            questionWrapper.setProperty('class', 'bottomseparator')
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
            self.rightWindow.Wrapper.QuestionLabel = QtGui.QLabel("Question : " + str(question.Question))
            self.rightWindow.Wrapper.QuestionLabel.setStyleSheet("""
                QLabel { 
                    font-size :  16px;
                    font-weight: bold;
                }
            """)
            questionWrapper.layout.addWidget(self.rightWindow.Wrapper.QuestionLabel)
            self.rightWindow.Wrapper.ResponseLabel = QtGui.QLabel("Response : " + ("Yes" if question.Response else "No"), self.rightWindow)
            self.rightWindow.Wrapper.ResponseLabel.setStyleSheet("""
                QLabel { 
                    font-size :  16px;
                    font-weight: bold;
                }
            """)
            questionWrapper.layout.addWidget(self.rightWindow.Wrapper.ResponseLabel)
            self.rightWindow.Wrapper.layout.addWidget(questionWrapper)

        self.rightWindow.Wrapper.btnsWrapper = QtGui.QWidget()
        self.rightWindow.Wrapper.btnsWrapper.layout = QtGui.QHBoxLayout()
        self.rightWindow.Wrapper.btnsWrapper.setLayout(self.rightWindow.Wrapper.btnsWrapper.layout)
        self.rightWindow.Wrapper.layout.addWidget(self.rightWindow.Wrapper.btnsWrapper)
        self.initAddQuestionBtn()
        self.rightWindow.setWidget(self.rightWindow.Wrapper)

    def initAddUserBtn(self):
        self.leftWindow.Wrapper.AddUserBtn = QtGui.QPushButton("+ Add User")
        self.leftWindow.Wrapper.AddUserBtn.setCursor(QtCore.Qt.PointingHandCursor)
        self.leftWindow.Wrapper.AddUserBtn.setStyleSheet(
            """
                QPushButton {
                    background-color: #4AAD67; 
                    font-weight: bold; 
                    border-radius:15px;
                    padding: 5px 20px;
                }
                QPushButton:hover {
                    background-color: #7CC7B7; 
                }
            """
        )
        self.leftWindow.Wrapper.AddUserBtn.clicked.connect(self.initAddUserSystem)
        self.leftWindow.Wrapper.btnsWrapper.layout.addWidget(self.leftWindow.Wrapper.AddUserBtn, 1, QtCore.Qt.AlignCenter)

    def initAddQuestionBtn(self):
        self.rightWindow.Wrapper.AddQuestionBtn = QtGui.QPushButton("+ Add Question")
        self.rightWindow.Wrapper.AddQuestionBtn.setCursor(QtCore.Qt.PointingHandCursor)
        self.rightWindow.Wrapper.AddQuestionBtn.setStyleSheet(
            """
                QPushButton {
                    background-color: #4AAD67; 
                    font-weight: bold; 
                    border-radius:15px;
                    padding: 5px 20px;
                }
                QPushButton:hover {
                    background-color: #7CC7B7; 
                }
            """
        )
        self.rightWindow.Wrapper.AddQuestionBtn.clicked.connect(self.initAddQuestionSystem)
        self.rightWindow.Wrapper.btnsWrapper.layout.addWidget(self.rightWindow.Wrapper.AddQuestionBtn, 1, QtCore.Qt.AlignCenter)
    
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
        Xbtn.setCursor(QtCore.Qt.PointingHandCursor)
        Xbtn.user = user
        Xbtn.setStyleSheet(
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
