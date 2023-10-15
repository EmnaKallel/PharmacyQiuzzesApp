from PyQt4 import QtGui, QtCore

class Screen(QtGui.QWidget):
    def __init__(self, callScreen, totalGrade, userGrade):
        super(Screen, self).__init__()
        self.callScreen = callScreen
        self.totalGrade = totalGrade
        self.userGrade = userGrade
        self.layout = QtGui.QVBoxLayout()
        self.setLayout(self.layout)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Result")
        self.setFixedSize(400,150)

        self.Label1 = QtGui.QLabel( "Good Job Your Score Is :" + str(float(self.userGrade)) + "/" + str(float(self.totalGrade)) )
        self.Label1.setStyleSheet("""
                QLabel { 
                    font-weight: bold; 
                }
            """)
        self.Label1.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.Label1)

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
        self.close()
        self.callScreen.reDisplay()

    def initResponsesBtn(self):
        pass