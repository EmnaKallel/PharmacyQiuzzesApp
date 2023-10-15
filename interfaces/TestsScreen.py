from PyQt4 import QtGui, QtCore
from models.Data import list_of_subjects
from customWidgets.SubjectWidget import SubjectWidget
import interfaces.SubjectTestsScreen as SubjectTestsScreen
import MainScreen

class Screen(QtGui.QWidget):
    def __init__(self, callScreen):
        super(Screen, self).__init__()
        self.callScreen = callScreen
        self.user = callScreen.user
        self.initUI()
    
    def initUI(self):
        
        while (self.callScreen.layout.count()>1):
            widget = self.callScreen.layout.itemAt(1).widget()
            if(widget):
                self.callScreen.layout.removeWidget(widget)
                widget.setParent(None)
                widget.deleteLater()
        self.callScreen.layout.insertWidget(1, self)
        
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
        self.Wrapper.welcome = QtGui.QLabel("WELCOME " + str(self.callScreen.user.userName) + " !")
        self.Wrapper.welcome.setStyleSheet("""
                QLabel { 
                    font-size :  18px;
                    color: #6648B0; 
                    font-weight: bold; 
                }
            """)
        self.Wrapper.layout.addWidget(self.Wrapper.welcome)
        self.Wrapper.Label1 = QtGui.QLabel("List Of Subjects : ")
        self.Wrapper.Label1.setStyleSheet("""
                QLabel { 
                    font-size :  25px;
                    color : #9A48B0;
                    font-weight: bold;
                }
            """)
        self.Wrapper.layout.addWidget(self.Wrapper.Label1)

        for subject in list_of_subjects :
            widget = SubjectWidget(subject, self.onSubjectWidgetNotification)
            self.Wrapper.layout.addWidget(widget)

        self.Wrapper.btnsWrapper = QtGui.QWidget()
        self.Wrapper.btnsWrapper.layout = QtGui.QHBoxLayout()
        self.Wrapper.btnsWrapper.setLayout(self.Wrapper.btnsWrapper.layout)
        self.Wrapper.layout.addWidget(self.Wrapper.btnsWrapper)
        self.initLogOutBtn()
        self.ScrollArea.setWidget(self.Wrapper)

    def onSubjectWidgetNotification(self, subject):
        SubjectTestsScreen.Screen(self, subject)
    
    def initLogOutBtn(self):
        self.Wrapper.LogOutBtn = QtGui.QPushButton("Log Out")
        self.Wrapper.LogOutBtn.setCursor(QtCore.Qt.PointingHandCursor)
        self.Wrapper.LogOutBtn.setStyleSheet(
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
        self.Wrapper.LogOutBtn.clicked.connect(self.LogOutSystem)
        self.Wrapper.btnsWrapper.layout.addWidget(self.Wrapper.LogOutBtn)

    def LogOutSystem(self):
        self.MainScreen = MainScreen.Screen()
        self.MainScreen.show()
        self.callScreen.close()
