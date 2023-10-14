from PyQt4 import QtGui, QtCore
import Style
import TestsScreen
import CoursesScreen
import ActivitiesHistory
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
        self.setWindowTitle("PharmacyQuizzesApp")
        self.setFixedSize(600,850)
        self.toolBarBtns = []
        self.initToolBar()
        self.initTestsScreen()

    def initToolBar(self):
        toolbar = QtGui.QToolBar()
        toolbar.setMovable(False)
        self.layout.addWidget(toolbar)

        button1 = QtGui.QPushButton('Tests', self)
        button1.clicked.connect(self.initTestsScreen)
        button1.setCursor(QtCore.Qt.PointingHandCursor)
        button2 = QtGui.QPushButton('Courses', self)
        button2.clicked.connect(self.initCoursesScreen)
        button2.setCursor(QtCore.Qt.PointingHandCursor)
        button3 = QtGui.QPushButton('Activities History', self)
        button3.clicked.connect(self.initActivitiesHistoryScreen)
        button3.setCursor(QtCore.Qt.PointingHandCursor)
        button4 = QtGui.QPushButton('Statistics', self)
        button4.clicked.connect(self.initStatisticsScreen)
        button4.setCursor(QtCore.Qt.PointingHandCursor)

        toolbar.addWidget(button1)
        toolbar.addWidget(button2)
        toolbar.addWidget(button3)
        toolbar.addWidget(button4)

        self.toolBarBtns.extend([button1, button2, button3, button4])
        for btn in self.toolBarBtns:
            btn.setStyleSheet(Style.TOOLBAR_BTN_OFF)
    
    def initTestsScreen(self):
        self.toolBarBtns[0].setStyleSheet(Style.TOOLBAR_BTN_ON)
        TestsScreen.Screen(self)
        self.toolBarBtns[1].setStyleSheet(Style.TOOLBAR_BTN_OFF)
        self.toolBarBtns[2].setStyleSheet(Style.TOOLBAR_BTN_OFF)
        self.toolBarBtns[3].setStyleSheet(Style.TOOLBAR_BTN_OFF)

    def initCoursesScreen(self):
        self.toolBarBtns[1].setStyleSheet(Style.TOOLBAR_BTN_ON)
        CoursesScreen.Screen(self)
        self.toolBarBtns[0].setStyleSheet(Style.TOOLBAR_BTN_OFF)
        self.toolBarBtns[2].setStyleSheet(Style.TOOLBAR_BTN_OFF)
        self.toolBarBtns[3].setStyleSheet(Style.TOOLBAR_BTN_OFF)

    def initActivitiesHistoryScreen(self):
        self.toolBarBtns[2].setStyleSheet(Style.TOOLBAR_BTN_ON)
        ActivitiesHistory.Screen(self)
        self.toolBarBtns[0].setStyleSheet(Style.TOOLBAR_BTN_OFF)
        self.toolBarBtns[1].setStyleSheet(Style.TOOLBAR_BTN_OFF)
        self.toolBarBtns[3].setStyleSheet(Style.TOOLBAR_BTN_OFF)

    def initStatisticsScreen(self):
        self.toolBarBtns[3].setStyleSheet(Style.TOOLBAR_BTN_ON)
        StatisticsScreen.Screen(self)
        self.toolBarBtns[0].setStyleSheet(Style.TOOLBAR_BTN_OFF)
        self.toolBarBtns[1].setStyleSheet(Style.TOOLBAR_BTN_OFF)
        self.toolBarBtns[2].setStyleSheet(Style.TOOLBAR_BTN_OFF)