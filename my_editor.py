# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MyEditor.ui'
#
# Created: Thu Aug 20 01:30:20 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(867, 636)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(180, 0, 691, 521))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.textEdit_2 = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(180, 520, 681, 41))
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.treeView = QtGui.QTreeView(self.centralwidget)
        self.treeView.setGeometry(QtCore.QRect(0, 0, 181, 561))
        self.treeView.setObjectName(_fromUtf8("treeView"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 867, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName(_fromUtf8("menu_File"))
        self.menu_Edit = QtGui.QMenu(self.menubar)
        self.menu_Edit.setObjectName(_fromUtf8("menu_Edit"))
        self.menu_View = QtGui.QMenu(self.menubar)
        self.menu_View.setObjectName(_fromUtf8("menu_View"))
        self.menuSelection = QtGui.QMenu(self.menubar)
        self.menuSelection.setObjectName(_fromUtf8("menuSelection"))
        self.menu_Help = QtGui.QMenu(self.menubar)
        self.menu_Help.setObjectName(_fromUtf8("menu_Help"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.action_open = QtGui.QAction(MainWindow)
        self.action_open.setObjectName(_fromUtf8("action_open"))
        self.action_Open_File = QtGui.QAction(MainWindow)
        self.action_Open_File.setObjectName(_fromUtf8("action_Open_File"))
        self.action_Open_Folder = QtGui.QAction(MainWindow)
        self.action_Open_Folder.setObjectName(_fromUtf8("action_Open_Folder"))
        self.action_Svae = QtGui.QAction(MainWindow)
        self.action_Svae.setObjectName(_fromUtf8("action_Svae"))
        self.action_Save_As = QtGui.QAction(MainWindow)
        self.action_Save_As.setObjectName(_fromUtf8("action_Save_As"))
        self.action_Quit = QtGui.QAction(MainWindow)
        self.action_Quit.setObjectName(_fromUtf8("action_Quit"))
        self.action_Undo = QtGui.QAction(MainWindow)
        self.action_Undo.setObjectName(_fromUtf8("action_Undo"))
        self.action_Redo = QtGui.QAction(MainWindow)
        self.action_Redo.setObjectName(_fromUtf8("action_Redo"))
        self.action_Cut = QtGui.QAction(MainWindow)
        self.action_Cut.setObjectName(_fromUtf8("action_Cut"))
        self.action_Copy = QtGui.QAction(MainWindow)
        self.action_Copy.setObjectName(_fromUtf8("action_Copy"))
        self.action_Paste = QtGui.QAction(MainWindow)
        self.action_Paste.setObjectName(_fromUtf8("action_Paste"))
        self.action_Find = QtGui.QAction(MainWindow)
        self.action_Find.setObjectName(_fromUtf8("action_Find"))
        self.action_Find_and_Replace = QtGui.QAction(MainWindow)
        self.action_Find_and_Replace.setObjectName(_fromUtf8("action_Find_and_Replace"))
        self.menu_File.addAction(self.action_open)
        self.menu_File.addAction(self.action_Open_File)
        self.menu_File.addAction(self.action_Open_Folder)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Svae)
        self.menu_File.addAction(self.action_Save_As)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Quit)
        self.menu_Edit.addAction(self.action_Undo)
        self.menu_Edit.addAction(self.action_Redo)
        self.menu_Edit.addSeparator()
        self.menu_Edit.addAction(self.action_Cut)
        self.menu_Edit.addAction(self.action_Copy)
        self.menu_Edit.addAction(self.action_Paste)
        self.menuSelection.addAction(self.action_Find)
        self.menuSelection.addAction(self.action_Find_and_Replace)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Edit.menuAction())
        self.menubar.addAction(self.menu_View.menuAction())
        self.menubar.addAction(self.menuSelection.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())
        self.toolBar.addAction(self.action_Redo)
        self.toolBar.addAction(self.action_Cut)
        self.toolBar.addAction(self.action_Paste)
        self.toolBar.addAction(self.action_Find)
        self.toolBar.addAction(self.action_Find_and_Replace)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.menu_File.setTitle(_translate("MainWindow", "&File", None))
        self.menu_Edit.setTitle(_translate("MainWindow", "&Edit", None))
        self.menu_View.setTitle(_translate("MainWindow", "&View", None))
        self.menuSelection.setTitle(_translate("MainWindow", "&Find", None))
        self.menu_Help.setTitle(_translate("MainWindow", "&Help", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.action_open.setText(_translate("MainWindow", "&New File", None))
        self.action_Open_File.setText(_translate("MainWindow", "&Open File", None))
        self.action_Open_Folder.setText(_translate("MainWindow", "&Open Folder", None))
        self.action_Svae.setText(_translate("MainWindow", "&Save", None))
        self.action_Save_As.setText(_translate("MainWindow", "&Save As", None))
        self.action_Quit.setText(_translate("MainWindow", "&Quit", None))
        self.action_Undo.setText(_translate("MainWindow", "&Undo", None))
        self.action_Redo.setText(_translate("MainWindow", "&Redo", None))
        self.action_Cut.setText(_translate("MainWindow", "&Cut", None))
        self.action_Copy.setText(_translate("MainWindow", "&Copy", None))
        self.action_Paste.setText(_translate("MainWindow", "&Paste", None))
        self.action_Find.setText(_translate("MainWindow", "&Find", None))
        self.action_Find_and_Replace.setText(_translate("MainWindow", "&Find and Replace", None))
