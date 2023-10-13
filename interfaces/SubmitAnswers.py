from PyQt4 import QtGui, QtCore
import ProfileScreen


class Screen(QtGui.QWidget):
    def __init__(self, callScreen, totalQuestions, correctAnswers, totalScore, userScore):
        super(Screen, self).__init__()
        self.callScreen = callScreen
        self.totalQuestions = totalQuestions
        self.correctAnswers = correctAnswers
        self.totalScore = totalScore
        self.userScore = userScore
        self.layout = QtGui.QVBoxLayout()
        self.setLayout(self.layout)
        self.initUI()
    def initUI(self):
        self.setWindowTitle("Result")
        self.setFixedSize(400,150)
        self.Label1 = QtGui.QLabel( "Good Job Your Number Of Correct Answers Is : " + str(self.correctAnswers) + "/" + str(self.totalQuestions) )
        self.Label1.setStyleSheet("""
                QLabel { 
                    font-weight: bold; 
                }
            """)
        self.Label1.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.Label1)
        self.Label2 = QtGui.QLabel( "Good Job Your Score Is : " + str(self.userScore) + "/" + str(self.totalScore) )
        self.Label2.setStyleSheet("""
                QLabel { 
                    font-weight: bold; 
                }
            """)
        self.Label2.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.Label2)
        self.btnsWrapper = QtGui.QWidget()
        self.btnsWrapper.layout = QtGui.QHBoxLayout()
        self.btnsWrapper.setLayout(self.btnsWrapper.layout)
        self.layout.addWidget(self.btnsWrapper)
        self.initCloseBtn()

    def initCloseBtn(self):
        self.CloseBtn = QtGui.QPushButton("Close")
        self.CloseBtn.setCursor(QtCore.Qt.PointingHandCursor)
        self.CloseBtn.setStyleSheet(
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
        self.CloseBtn.clicked.connect(self.initiateCloseSystem)
        self.btnsWrapper.layout.addWidget(self.CloseBtn)

    def initiateCloseSystem (self):
        self.callScreen.callScreen.show()
        self.close()