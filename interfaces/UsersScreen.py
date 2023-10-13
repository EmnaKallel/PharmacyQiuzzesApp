from PyQt4 import QtGui, QtCore
import Style
import ProfileScreen
import TestsHistoryScreen
import StatisticsScreen
import MainScreen

class Screen(QtGui.QWidget):
    def __init__(self, user):
        self.user = user
        super(Screen, self).__init__()
        self.layout = QtGui.QVBoxLayout()
        self.setLayout(self.layout)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QuizApp")
        self.setFixedSize(600,800)
        self.toolBarBtns = []
        self.initToolBar()
        self.initProfileScreen()

    def initToolBar(self):
        toolbar = QtGui.QToolBar()
        toolbar.setMovable(False)
        self.layout.addWidget(toolbar)

        button1 = QtGui.QPushButton('Profile', self)
        button1.clicked.connect(self.initProfileScreen)
        button1.setCursor(QtCore.Qt.PointingHandCursor)
        button2 = QtGui.QPushButton('Tests History', self)
        button2.clicked.connect(self.initTestsHistoryScreen)
        button2.setCursor(QtCore.Qt.PointingHandCursor)
        button3 = QtGui.QPushButton('Statistics', self)
        button3.clicked.connect(self.initStatisticsScreen)
        button3.setCursor(QtCore.Qt.PointingHandCursor)

        toolbar.addWidget(button1)
        toolbar.addWidget(button2)
        toolbar.addWidget(button3)

        self.toolBarBtns.extend([button1, button2, button3])
        for btn in self.toolBarBtns:
            btn.setStyleSheet(Style.TOOLBAR_BTN_OFF)
    
    def initProfileScreen(self):
        self.toolBarBtns[0].setStyleSheet(Style.TOOLBAR_BTN_ON)
        ProfileScreen.Screen(self)
        self.toolBarBtns[1].setStyleSheet(Style.TOOLBAR_BTN_OFF)
        self.toolBarBtns[2].setStyleSheet(Style.TOOLBAR_BTN_OFF)

    def initTestsHistoryScreen(self):
        self.toolBarBtns[1].setStyleSheet(Style.TOOLBAR_BTN_ON)
        TestsHistoryScreen.Screen(self)
        self.toolBarBtns[0].setStyleSheet(Style.TOOLBAR_BTN_OFF)
        self.toolBarBtns[2].setStyleSheet(Style.TOOLBAR_BTN_OFF)

    def initStatisticsScreen(self):
        self.toolBarBtns[2].setStyleSheet(Style.TOOLBAR_BTN_ON)
        StatisticsScreen.Screen(self)
        self.toolBarBtns[0].setStyleSheet(Style.TOOLBAR_BTN_OFF)
        self.toolBarBtns[1].setStyleSheet(Style.TOOLBAR_BTN_OFF)