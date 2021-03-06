# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pydownload.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1106, 631)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.browseDir = QtWidgets.QPushButton(self.centralwidget)
        self.browseDir.setObjectName("browseDir")
        self.gridLayout.addWidget(self.browseDir, 8, 4, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 10, 1, 1, 1)
        self.chooseDirectory = QtWidgets.QLabel(self.centralwidget)
        self.chooseDirectory.setObjectName("chooseDirectory")
        self.gridLayout.addWidget(self.chooseDirectory, 8, 1, 1, 1)
        self.urlBox = QtWidgets.QLineEdit(self.centralwidget)
        self.urlBox.setObjectName("urlBox")
        self.gridLayout.addWidget(self.urlBox, 2, 1, 1, 4)
        self.fileTable = QtWidgets.QTableWidget(self.centralwidget)
        self.fileTable.setObjectName("fileTable")
        self.fileTable.setColumnCount(0)
        self.fileTable.setRowCount(0)
        self.gridLayout.addWidget(self.fileTable, 0, 0, 15, 1)
        self.enterURL = QtWidgets.QLabel(self.centralwidget)
        self.enterURL.setObjectName("enterURL")
        self.gridLayout.addWidget(self.enterURL, 1, 1, 1, 1)
        self.download = QtWidgets.QPushButton(self.centralwidget)
        self.download.setObjectName("download")
        self.gridLayout.addWidget(self.download, 13, 4, 1, 1)
        self.filename = QtWidgets.QLineEdit(self.centralwidget)
        self.filename.setObjectName("filename")
        self.gridLayout.addWidget(self.filename, 11, 1, 1, 4)
        self.fileFormat = QtWidgets.QComboBox(self.centralwidget)
        self.fileFormat.setObjectName("fileFormat")
        self.fileFormat.addItem("")
        self.gridLayout.addWidget(self.fileFormat, 12, 4, 1, 1)
        self.format = QtWidgets.QLabel(self.centralwidget)
        self.format.setObjectName("format")
        self.gridLayout.addWidget(self.format, 12, 1, 1, 3)
        self.processURL = QtWidgets.QPushButton(self.centralwidget)
        self.processURL.setObjectName("processURL")
        self.gridLayout.addWidget(self.processURL, 7, 4, 1, 1)
        self.dlDirectory = QtWidgets.QLineEdit(self.centralwidget)
        self.dlDirectory.setFrame(True)
        self.dlDirectory.setDragEnabled(True)
        self.dlDirectory.setObjectName("dlDirectory")
        self.gridLayout.addWidget(self.dlDirectory, 9, 1, 1, 4)
        self.type = QtWidgets.QLabel(self.centralwidget)
        self.type.setObjectName("type")
        self.gridLayout.addWidget(self.type, 3, 3, 1, 1)
        self.fileType = QtWidgets.QComboBox(self.centralwidget)
        self.fileType.setObjectName("fileType")
        self.fileType.addItem("")
        self.fileType.addItem("")
        self.gridLayout.addWidget(self.fileType, 3, 4, 1, 1)
        self.console = QtWidgets.QTextEdit(self.centralwidget)
        self.console.setObjectName("console")
        self.gridLayout.addWidget(self.console, 0, 1, 1, 4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")

        self.retranslateUi(MainWindow)
        self.download.clicked.connect(self.urlBox.clear)
        self.urlBox.returnPressed.connect(self.processURL.click)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.urlBox, self.fileFormat)
        MainWindow.setTabOrder(self.fileFormat, self.dlDirectory)
        MainWindow.setTabOrder(self.dlDirectory, self.fileTable)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Python Youtube Downloader"))
        self.browseDir.setText(_translate("MainWindow", "Browse"))
        self.label.setText(_translate("MainWindow", "Type Filename (or leave blank for default)"))
        self.chooseDirectory.setText(_translate("MainWindow", "Choose Directory"))
        self.enterURL.setText(_translate("MainWindow", "Enter URL"))
        self.download.setText(_translate("MainWindow", "Download"))
        self.fileFormat.setItemText(0, _translate("MainWindow", "x264"))
        self.format.setText(_translate("MainWindow", "Choose Video Encoder (when using video type only)"))
        self.processURL.setText(_translate("MainWindow", "Process URL"))
        self.type.setText(_translate("MainWindow", "Choose Type"))
        self.fileType.setItemText(0, _translate("MainWindow", "Video"))
        self.fileType.setItemText(1, _translate("MainWindow", "Audio"))
        self.console.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))

