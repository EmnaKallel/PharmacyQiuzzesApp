from PyQt4 import QtGui, QtCore
import ProfileScreen


class Screen(QtGui.QWidget):
    def __init__(self, callScreen):
        super(Screen, self).__init__()
        self.callScreen = callScreen
        self.layout = QtGui.QVBoxLayout()
        self.setLayout(self.layout)
        self.initUI()
    def initUI(self):
        self.setWindowTitle("Result")
        self.setFixedSize(350,500)
        self.Label = QtGui.QLabel("Good Job Your Score Is : ")
        self.layout.addWidget(self.Label)
        self.btnsWrapper = QtGui.QWidget()
        self.btnsWrapper.layout = QtGui.QHBoxLayout()
        self.btnsWrapper.setLayout(self.btnsWrapper.layout)
        self.layout.addWidget(self.btnsWrapper)
        self.initCloseBtn()

    def initCloseBtn(self):
        self.CloseBtn = QtGui.QPushButton("Close")
        self.CloseBtn.setStyleSheet(
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
        self.CloseBtn.clicked.connect(self.initiateCloseSystem)
        self.btnsWrapper.layout.addWidget(self.CloseBtn)

    def initiateCloseSystem (self):
        self.callScreen.callScreen.show()
        self.close()