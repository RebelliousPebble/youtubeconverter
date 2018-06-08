# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Development\youtubeconverter\pydownload.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtQuickWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.urlBox = QtWidgets.QLineEdit(self.centralwidget)
        self.urlBox.setGeometry(QtCore.QRect(360, 270, 421, 21))
        self.urlBox.setObjectName("urlBox")
        self.download = QtWidgets.QPushButton(self.centralwidget)
        self.download.setGeometry(QtCore.QRect(664, 512, 101, 31))
        self.download.setObjectName("download")
        self.processURL = QtWidgets.QPushButton(self.centralwidget)
        self.processURL.setGeometry(QtCore.QRect(710, 410, 75, 23))
        self.processURL.setObjectName("processURL")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(360, 512, 291, 31))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.fileTable = QtWidgets.QTableWidget(self.centralwidget)
        self.fileTable.setGeometry(QtCore.QRect(10, 10, 331, 521))
        self.fileTable.setObjectName("fileTable")
        self.fileTable.setColumnCount(0)
        self.fileTable.setRowCount(0)
        self.fileType = QtWidgets.QComboBox(self.centralwidget)
        self.fileType.setGeometry(QtCore.QRect(710, 320, 69, 22))
        self.fileType.setObjectName("fileType")
        self.type = QtWidgets.QLabel(self.centralwidget)
        self.type.setGeometry(QtCore.QRect(616, 320, 81, 20))
        self.type.setObjectName("type")
        self.format = QtWidgets.QLabel(self.centralwidget)
        self.format.setGeometry(QtCore.QRect(600, 370, 91, 20))
        self.format.setObjectName("format")
        self.fileFormat = QtWidgets.QComboBox(self.centralwidget)
        self.fileFormat.setGeometry(QtCore.QRect(710, 370, 69, 22))
        self.fileFormat.setObjectName("fileFormat")
        self.dlDirectory = QtWidgets.QLineEdit(self.centralwidget)
        self.dlDirectory.setGeometry(QtCore.QRect(360, 460, 341, 21))
        self.dlDirectory.setObjectName("dlDirectory")
        self.chooseDirectory = QtWidgets.QLabel(self.centralwidget)
        self.chooseDirectory.setGeometry(QtCore.QRect(360, 440, 101, 16))
        self.chooseDirectory.setObjectName("chooseDirectory")
        self.browseURL = QtWidgets.QPushButton(self.centralwidget)
        self.browseURL.setGeometry(QtCore.QRect(710, 460, 75, 23))
        self.browseURL.setObjectName("browseURL")
        self.enterURL = QtWidgets.QLabel(self.centralwidget)
        self.enterURL.setGeometry(QtCore.QRect(360, 250, 47, 13))
        self.enterURL.setObjectName("enterURL")
        self.console = QtWidgets.QTextBrowser(self.centralwidget)
        self.console.setGeometry(QtCore.QRect(360, 10, 421, 231))
        self.console.setObjectName("console")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.download.clicked.connect(self.urlBox.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.urlBox, self.fileType)
        MainWindow.setTabOrder(self.fileType, self.fileFormat)
        MainWindow.setTabOrder(self.fileFormat, self.processURL)
        MainWindow.setTabOrder(self.processURL, self.browseURL)
        MainWindow.setTabOrder(self.browseURL, self.dlDirectory)
        MainWindow.setTabOrder(self.dlDirectory, self.download)
        MainWindow.setTabOrder(self.download, self.fileTable)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Python Youtube Downloader"))
        self.download.setText(_translate("MainWindow", "Download"))
        self.processURL.setText(_translate("MainWindow", "Process URL"))
        self.type.setText(_translate("MainWindow", "Choose Type"))
        self.format.setText(_translate("MainWindow", "Choose Format"))
        self.chooseDirectory.setText(_translate("MainWindow", "Choose Directory"))
        self.browseURL.setText(_translate("MainWindow", "Browse"))
        self.enterURL.setText(_translate("MainWindow", "Enter URL"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

