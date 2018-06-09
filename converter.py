from pytube import YouTube
import pytube
from hurry.filesize import verbose
from hurry.filesize import size
import os
import multiprocessing as mp
import sys
import time
import traceback
import tempfile

from PyQt5 import QtCore, QtGui, QtWidgets
from qt_mainwindow import Ui_MainWindow


class YTConverter(Ui_MainWindow):
    def __init__(self, MainWindow):
        self.yt = 0
        self.tempdir = tempfile.gettempdir()
        Ui_MainWindow.__init__(self)
        self.setupUi(MainWindow)
        self.processURL.clicked.connect(self.processurlpressed)
        self.browseDir.clicked.connect(self.browsepressed)
        self.download.clicked.connect(self.downloadpressed)

    def consolewrite(self, msg):
        '''Add msg to the console's output'''
        self.console.insertPlainText(msg)
        # Autoscroll
        self.console.moveCursor(QtGui.QTextCursor.End)


    def processurlpressed(self):
        #* TODO setup table creation
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
                self.vids = self.yt.streams.filter(adaptive=True).filter(only_video=True).asc().all()
                self.fileTable.setRowCount(0)
                self.fileTable.setColumnCount(6)
                self.fileTable.setHorizontalHeaderLabels(
                    ["Download?","iTag","Original Format","Resolution","Frame Rate","Filesize"])
                for stream in self.vids:
                    print('run')
                    rowPosition = self.fileTable.rowCount()
                    self.fileTable.insertRow(rowPosition)
                    chkBoxItem = QtWidgets.QTableWidgetItem()
                    chkBoxItem.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                    chkBoxItem.setCheckState(QtCore.Qt.Unchecked)
                    self.fileTable.setItem(rowPosition, 0, chkBoxItem)
                    self.fileTable.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(stream.itag))
                    self.fileTable.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(stream.mime_type.strip('video/')))
                    self.fileTable.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem(stream.resolution))
                    self.fileTable.setItem(rowPosition, 4, QtWidgets.QTableWidgetItem(str(stream.fps)))
                    self.fileTable.setItem(rowPosition, 5, QtWidgets.QTableWidgetItem(
                        size(stream.filesize, system=verbose)))

            except:
                traceback.print_exc()

        elif self.fileType.currentText() == 'Audio':
            try:
                self.vids = self.yt.streams.filter(adaptive=True).filter(only_audio=True).asc().all()
                self.fileTable.setRowCount(0)
                self.fileTable.setColumnCount(5)
                self.fileTable.setHorizontalHeaderLabels(
                    ["Download?","iTag","Original Format","Bit Rate", "Filesize"])
                for stream in self.vids:
                    print('run')
                    rowPosition = self.fileTable.rowCount()
                    self.fileTable.insertRow(rowPosition)
                    chkBoxItem = QtWidgets.QTableWidgetItem()
                    chkBoxItem.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                    chkBoxItem.setCheckState(QtCore.Qt.Unchecked)
                    self.fileTable.setItem(rowPosition, 0, chkBoxItem)
                    self.fileTable.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(stream.itag))
                    self.fileTable.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(stream.mime_type.strip('video/')))
                    self.fileTable.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem(stream.abr))
                    self.fileTable.setItem(rowPosition, 4,
                                           QtWidgets.QTableWidgetItem(size(stream.filesize, system=verbose)))

            except:
                traceback.print_exc()

    def browsepressed(self):
        file = str(QtWidgets.QFileDialog.getExistingDirectoryUrl(None, "Select Download Directory"))
        file = file.strip("PyQt5.QtCore.QUrl('file:///")
        file = file.strip("')")
        self.dlDirectory.setText(file)

    def downloadpressed(self):
        checked_list = []
        for i in range(self.fileTable.rowCount()):
            if self.fileTable.item(i, 0).checkState() == QtCore.Qt.Checked:
                checked_list.append(self.fileTable.item(i, 1).text().strip('iTag: '))
        processes = []
        directory = self.dlDirectory.text()
        for i in checked_list:
            print(i)
            p = mp.Process(target=download, args=(self.yt, int(i), self.tempdir, None))
            processes.append(p)
        p = mp.Process(target=download, args=(self.yt, 251, self.tempdir, None))
        processes.append(p)

        print(processes)
        for x in processes:
            x.start()
        for x in processes:
            x.join()



def download(yt, itag, directory, name):
    print('downloading ' + str(itag))
    stream = yt.streams.get_by_itag(itag)
    stream.download(directory)
    print('finished downloading ' + str(itag))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    prog = YTConverter(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

