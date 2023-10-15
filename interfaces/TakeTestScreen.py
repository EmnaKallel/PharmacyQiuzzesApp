from PyQt4 import QtGui, QtCore
from customWidgets.QuestionAnswersWidget import QuestionAnswersWidget
import SubmitAnswersScreen

class Screen(QtGui.QWidget):
    def __init__(self, callScreen, test):
        super(Screen, self).__init__()
        self.callScreen = callScreen 
        self.test = test 
        self.questionAnswerWidgets = []
        self.initUI()
    
    def initUI(self):
        
        while (self.callScreen.layout.count()>0):
            widget = self.callScreen.layout.itemAt(0).widget()
            if(widget):
                self.callScreen.layout.removeWidget(widget)
                widget.setParent(None)
                widget.deleteLater()
        self.callScreen.layout.insertWidget(0, self)
        
        self.layout = QtGui.QVBoxLayout()
        self.setLayout(self.layout)
        self.ScrollArea = QtGui.QScrollArea()
        self.layout.addWidget(self.ScrollArea)

        self.Wrapper = QtGui.QWidget()
        self.Wrapper.layout = QtGui.QVBoxLayout()
        self.Wrapper.setLayout(self.Wrapper.layout)
        self.Wrapper.layout.setContentsMargins(10, 5, 5, 5)

        self.Wrapper.Label = QtGui.QLabel("User Account")
        self.Wrapper.Label.setStyleSheet("""
                QLabel { 
                    font-size :  20px;
                    color: #2A7640; 
                    font-weight: bold; 
                }
            """)
        self.Wrapper.layout.addWidget(self.Wrapper.Label)

        self.Wrapper.welcome = QtGui.QLabel("WELCOME " + str(self.callScreen.callScreen.user.userName) + " !")
        self.Wrapper.welcome.setStyleSheet("""
                QLabel { 
                    font-size :  18px;
                    color: #6648B0; 
                    font-weight: bold; 
                }
            """)
        self.Wrapper.layout.addWidget(self.Wrapper.welcome)

        self.Wrapper.test = QtGui.QLabel(str(self.test.TestName))
        self.Wrapper.test.setStyleSheet("""
                QLabel { 
                    font-size :  18px;
                    color: #A55AD5; 
                    font-weight: bold; 
                }
            """)
        self.Wrapper.layout.addWidget(self.Wrapper.test)

        for question in self.test.questions :
            widget = QuestionAnswersWidget (question)
            self.questionAnswerWidgets.append(widget)
            self.Wrapper.layout.addWidget(widget)

        self.Wrapper.btnsWrapper = QtGui.QWidget()
        self.Wrapper.btnsWrapper.layout = QtGui.QHBoxLayout()
        self.Wrapper.btnsWrapper.setLayout(self.Wrapper.btnsWrapper.layout)
        self.Wrapper.layout.addWidget(self.Wrapper.btnsWrapper)
        self.initSubmitAnswersBtn()
        self.initCancelBtn()

        self.ScrollArea.setWidget(self.Wrapper)

    def initCancelBtn(self):
        self.Wrapper.CancelBtn = QtGui.QPushButton("Cancel")
        self.Wrapper.CancelBtn.setCursor(QtCore.Qt.PointingHandCursor)
        self.Wrapper.CancelBtn.setStyleSheet(
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
        self.Wrapper.CancelBtn.clicked.connect(self.CancelBtnSystem)
        self.Wrapper.btnsWrapper.layout.addWidget(self.Wrapper.CancelBtn)

    def CancelBtnSystem(self):
        pass
    
    def initSubmitAnswersBtn(self):
        self.Wrapper.SubmitAnswersBtn = QtGui.QPushButton("Submit Answers")
        self.Wrapper.SubmitAnswersBtn.setCursor(QtCore.Qt.PointingHandCursor)
        self.Wrapper.SubmitAnswersBtn.setStyleSheet(
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
        self.Wrapper.SubmitAnswersBtn.clicked.connect(self.SubmitAnswersBtnSystem)
        self.Wrapper.btnsWrapper.layout.addWidget(self.Wrapper.SubmitAnswersBtn)

    def SubmitAnswersBtnSystem(self):
        userGrade = 0
        totalGrade = 0
        for questionOtionWidget in self.questionAnswerWidgets:
            userGrade = userGrade + questionOtionWidget.checkAnswerCorrectness()
            totalGrade = totalGrade + 1
        self.SubmitAnswersScreen = SubmitAnswersScreen.Screen(self, totalGrade, userGrade)
        self.SubmitAnswersScreen.show()
        self.callScreen.callScreen.callScreen.close()
        
    def reDisplay(self):
        userScreen = self.callScreen.callScreen.callScreen
        userScreen.show()
        testScreen = self.callScreen.callScreen
        testScreen.redraw()
        