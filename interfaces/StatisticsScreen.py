from PyQt4 import QtGui

class Screen(QtGui.QWidget):
    def __init__(self, callScreen):
        super(Screen, self).__init__()
        self.callScreen = callScreen 
        self.initUI()
    
    def initUI(self):
        self.layout = QtGui.QVBoxLayout()
        self.setLayout(self.layout)
        self.ScrollArea = QtGui.QScrollArea()
        self.layout.addWidget(self.ScrollArea)
        self.Wrapper = QtGui.QWidget()
        self.Wrapper.layout = QtGui.QVBoxLayout()
        self.Wrapper.setLayout(self.Wrapper.layout)
        self.Wrapper.layout.setContentsMargins(10, 5, 5, 5)
        
        while (self.callScreen.layout.count()>1):
            widget = self.callScreen.layout.itemAt(1).widget()
            if(widget):
                self.callScreen.layout.removeWidget(widget)
                widget.setParent(None)
                widget.deleteLater()
        self.callScreen.layout.insertWidget(1, self)

        self.Wrapper.Label = QtGui.QLabel("User Account")
        self.Wrapper.Label.setStyleSheet("""
                QLabel { 
                    font-size :  20px;
                    color: #2A7640; 
                    font-weight: bold; 
                }
            """)
        self.Wrapper.layout.addWidget(self.Wrapper.Label)
        self.Wrapper.welcome = QtGui.QLabel("WELCOME " + str(self.callScreen.user.userName) + " !")
        self.Wrapper.welcome.setStyleSheet("""
                QLabel { 
                    font-size :  18px;
                    color: #6648B0; 
                    font-weight: bold; 
                }
            """)
        self.Wrapper.layout.addWidget(self.Wrapper.welcome)
        self.Wrapper.Label1 = QtGui.QLabel("Statistical Graphics : ")
        self.Wrapper.Label1.setStyleSheet("""
                QLabel { 
                    font-size :  25px;
                    color : #9A48B0;
                    font-weight: bold;
                }
            """)
        self.Wrapper.layout.addWidget(self.Wrapper.Label1)

        self.ScrollArea.setWidget(self.Wrapper)