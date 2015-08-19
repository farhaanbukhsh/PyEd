import sys
from PyQt4 import QtCore, QtGui
from my_editor import Ui_MainWindow

class StartQT4(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.menu_File, QtCore.SIGNAL("clicked()"), self.file_dialog)
    def file_dialog(self):
        self.ui.textEdit.setText("aaaaaaaaa")


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())
