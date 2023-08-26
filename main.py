import sys
from PyQt4 import QtGui
import interfaces.MainScreen as MainScreen

def main():
    app = QtGui.QApplication(sys.argv)
    window = MainScreen.Screen()
    window.show()

    sys.exit(app.exec_())

main()