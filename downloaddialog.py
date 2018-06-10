# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Development\youtubeconverter\downloaddialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DownloadDialog(object):
    def setupUi(self, DownloadDialog):
        DownloadDialog.setObjectName("DownloadDialog")
        DownloadDialog.resize(400, 172)
        self.gridLayout = QtWidgets.QGridLayout(DownloadDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.filedownloading = QtWidgets.QLabel(DownloadDialog)
        self.filedownloading.setObjectName("filedownloading")
        self.gridLayout.addWidget(self.filedownloading, 0, 0, 1, 1)
        self.bytesleft = QtWidgets.QLabel(DownloadDialog)
        self.bytesleft.setObjectName("bytesleft")
        self.gridLayout.addWidget(self.bytesleft, 1, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(DownloadDialog)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 2, 0, 1, 1)

        self.retranslateUi(DownloadDialog)
        QtCore.QMetaObject.connectSlotsByName(DownloadDialog)

    def retranslateUi(self, DownloadDialog):
        _translate = QtCore.QCoreApplication.translate
        DownloadDialog.setWindowTitle(_translate("DownloadDialog", "Downloading..."))
        self.filedownloading.setText(_translate("DownloadDialog", "Downloading"))
        self.bytesleft.setText(_translate("DownloadDialog", "bytes left"))

