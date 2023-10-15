from PyQt4 import QtGui, QtCore

class TestWidget(QtGui.QWidget):
    def __init__(self, test, notifyCaller):
        super(TestWidget, self).__init__()
        self.test = test
        self.notifyCaller = notifyCaller
        self.initUI()
        
    def initUI(self):
        self.layout = QtGui.QVBoxLayout()
        self.setLayout(self.layout)
        self.layout.setContentsMargins(0, 2, 0, 0)
        
        testWrapper = QtGui.QWidget()
        testWrapper.setProperty('class', 'testWrapper')
        testWrapper.setStyleSheet("""
            .testWrapper{
                max-width: 470px;
                min-width: 470px;
                min-height: 50px;
                border : 1px solid black;
                border-radius: 8px;
                background-color: #7CC7B7;
                padding: 5px 20px;
            }
            .testWrapper:hover{
                background-color: #B1EDC2;
            }
        """)
        
        testWrapper.layout = QtGui.QVBoxLayout()
        testWrapper.setCursor(QtCore.Qt.PointingHandCursor)
        testWrapper.setLayout(testWrapper.layout)

        self.testLabel = QtGui.QLabel(str(self.test.TestName))
        self.testLabel.setStyleSheet("""
            QLabel { 
                color : #040404;
                font-size :  20px;
                font-weight: bold;
            }
        """)
        testWrapper.layout.addWidget(self.testLabel)
        self.layout.addWidget(testWrapper)

    def mousePressEvent(self, event):
        self.notifyCaller(self.test)