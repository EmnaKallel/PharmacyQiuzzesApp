from PyQt4 import QtGui, QtCore
from models.Data import list_of_users
from models.Data import list_of_questions
import Style

class Screen(QtGui.QWidget):
    def __init__(self, callScreen):
        super(Screen, self).__init__()
        self.callScreen = callScreen 
        self.initUI()
    
    def initUI(self):
        self.layout = QtGui.QVBoxLayout()
        self.setLayout(self.layout)
        self.layout.setContentsMargins(0, 0, 0, 0)
        
        while (self.callScreen.layout.count()>1):
            widget = self.callScreen.layout.itemAt(1).widget()
            if(widget):
                self.callScreen.layout.removeWidget(widget)
                widget.setParent(None)
                widget.deleteLater()
        self.callScreen.layout.insertWidget(1, self)
        self.Label = QtGui.QLabel("Welcome To Your Statistics")
        self.Label.setStyleSheet("""
                QLabel { 
                    font-size :  20px;
                    color: rgb(45, 188, 45); 
                    font-weight: bold; 
                }
            """)
        self.layout.addWidget(self.Label)