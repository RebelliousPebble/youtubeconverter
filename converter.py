from pytube import YouTube
import pytube
from hurry.filesize import verbose
from hurry.filesize import size
import os
import subprocess
import sys
import time
import traceback

from PyQt5 import QtCore, QtGui, QtWidgets
from qt_mainwindow import Ui_MainWindow


class YTConverter(Ui_MainWindow):
    def __init__(self, MainWindow):
        self.yt = 0
        Ui_MainWindow.__init__(self)
        self.setupUi(MainWindow)
        self.processURL.clicked.connect(self.processurlpressed)

    def consolewrite(self, msg):
        '''Add msg to the console's output'''
        self.console.insertPlainText(msg)
        # Autoscroll
        self.console.moveCursor(QtGui.QTextCursor.End)


    def processurlpressed(self):
        ## TODO setup table creation
        url = self.urlBox.text()
        if not url:
            self.consolewrite("Insert a URL to continue\n")
        else:
            try:
                self.console.clear()
                self.consolewrite("Processing URL\n")
                time.sleep(0.5)
                self.yt = YouTube(url)
            except pytube.exceptions.RegexMatchError:
                traceback.print_exc()
                self.consolewrite("URL not valid\n")
        if self.fileType.currentText() == 'Video':
            try:
                self.vids = self.yt.streams.filter(only_video=True).order_by('resolution').all()
                self.fileTable.setColumnCount(4)
                self.fileTable.setHorizontalHeaderLabels(["Download?","Original Format","Resolution","Frame Rate"])
                for stream in self.vids:
                    rowPosition = self.fileTable.rowCount()
                    self.fileTable.insertRow(rowPosition)
                    self.fileTable.setItem(rowPosition, 0, QtWidgets.QCheckBox())
                    self.fileTable.setItem(rowPosition, 1, QtGui.QTableWidgetItem("text2"))
                    self.fileTable.setItem(rowPosition, 2, QtGui.QTableWidgetItem("text3"))
                    self.fileTable.setItem(rowPosition, 3, QtGui.QTableWidgetItem("text4"))

            except:
                traceback.print_exc()


    def downloadpressed(self):
        ## TODO implement download button method
        pass
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    prog = YTConverter(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

