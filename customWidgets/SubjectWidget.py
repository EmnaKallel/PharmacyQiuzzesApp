from PyQt4 import QtGui, QtCore
from models.Data import list_of_subjects

class SubjectWidget(QtGui.QWidget):
    def __init__(self, subject):
        super(SubjectWidget, self).__init__()
        self.subject = subject
        self.initUI()
        
    def initUI(self):
        self.layout = QtGui.QVBoxLayout()
        self.setLayout(self.layout)
        self.layout.setContentsMargins(0, 2, 0, 0)
        
        subjectWrapper = QtGui.QWidget()
        subjectWrapper.setProperty('class', 'bottomseparator')
        #to add a line only at the bottom use : "border-bottom : 1px solid black;""
        subjectWrapper.setStyleSheet("""
            .bottomseparator{
                border : 1px solid black;
                border-radius: 8px;
                background-color: #7CC7B7;
                padding: 5px 20px;
            }
        """)
        
        subjectWrapper.layout = QtGui.QVBoxLayout()
        subjectWrapper.setCursor(QtCore.Qt.PointingHandCursor)
        subjectWrapper.setLayout(subjectWrapper.layout)
        self.subjectLabel = QtGui.QLabel(str(self.subject.subjectsName))
        
        
        self.subjectLabel.setStyleSheet("""
            QLabel { 
                color : #040404;
                font-size :  20px;
                font-weight: bold;
            }
        """)
        subjectWrapper.layout.addWidget(self.subjectLabel)
        self.layout.addWidget(subjectWrapper)

    def mousePressEvent(self, event):
        print(self.subject.subjectsName)