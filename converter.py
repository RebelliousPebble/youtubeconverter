from pytube import YouTube
import pytube
from filesize import verbose
from filesize import size
import os
import subprocess
import sys
import time
import traceback
import tempfile
import moviepy.editor as mp



from PyQt5 import QtCore, QtGui, QtWidgets
from qt_mainwindow import Ui_MainWindow


class MergeAudioVideo(QtCore.QRunnable):
    def __init__(self, audio_path, video_path, output_path):
        QtCore.QRunnable.__init__(self)
        self.audio_path = audio_path
        self.video_path = video_path
        self.output_path = output_path

    def run(self):
        '''
        cmd = ('ffmpeg -i ' + '"' + self.audio_path + '"' + ' -i ' + '"' + self.video_path + '"' + ' -y -acodec aac -b:a 160k -vcodec libx264 -preset fast -crf 20 ' + '"' + self.output_path + '"')
        print(cmd)
        subprocess.run(cmd)
        '''
        audio = mp.AudioFileClip(self.audio_path)
        #newaudiopath = self.audio_path[:5]+'.mp3'
        #audio.write_audiofile(newaudiopath, codec=)
        final = mp.VideoFileClip(self.video_path).set_audio(audio)
        final.write_videofile(self.output_path, codec='libx264', audio_codec='libmp3lame')

class ConvertAudio(QtCore.QRunnable):
    def __init__(self, audio_path, output_path):
        QtCore.QRunnable.__init__(self)
        self.audio_path = audio_path
        self.output_path = output_path

    def run(self):
        if os.path.isfile(self.output_path):
            os.remove(self.output_path)
        cmd = ('ffmpeg -i ' + '"' + self.audio_path + '"' + ' -vn -ab 320k -ar 44100 -f mp3 ' + '"' + self.output_path + '"')
        print(cmd)
        subprocess.run(cmd)

class DownloadFileThread(QtCore.QRunnable):
    def __init__(self, yt, itag, directory, name=None):
        QtCore.QRunnable.__init__(self)
        self.yt = yt
        self.itag = itag
        self.directory = directory
        self. name = name



    def run(self):
        print('downloading ' + str(self.itag))
        stream = self.yt.streams.get_by_itag(self.itag)
        stream.download(self.directory, self.name)



class YTConverter(Ui_MainWindow):
    def __init__(self, MainWindow):
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



    def finishdownload(self):
        self.download.setEnabled(True)
        QtWidgets.QMessageBox.information(self, "Done!", "Finished Downloading!!")

    def processurlpressed(self):
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
                self.vids = self.yt.streams.filter(adaptive=True).filter(subtype='webm').filter(only_video=True).asc().all()
                self.fileTable.setRowCount(0)
                self.fileTable.setColumnCount(5)
                self.fileTable.setHorizontalHeaderLabels(
                    ["Download?","iTag","Resolution","Frame Rate","Filesize"])
                for stream in self.vids:
                    rowPosition = self.fileTable.rowCount()
                    self.fileTable.insertRow(rowPosition)
                    chkBoxItem = QtWidgets.QTableWidgetItem()
                    chkBoxItem.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                    chkBoxItem.setCheckState(QtCore.Qt.Unchecked)
                    self.fileTable.setItem(rowPosition, 0, chkBoxItem)
                    self.fileTable.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(stream.itag))
                    self.fileTable.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(stream.resolution))
                    self.fileTable.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem(str(stream.fps)))
                    self.fileTable.setItem(rowPosition, 4, QtWidgets.QTableWidgetItem(
                        size(stream.filesize, system=verbose)))

            except:
                traceback.print_exc()

        elif self.fileType.currentText() == 'Audio':
            try:
                self.vids = self.yt.streams.filter(adaptive=True).filter(subtype='webm').filter(only_audio=True).asc().all()
                self.fileTable.setRowCount(0)
                self.fileTable.setColumnCount(4)
                self.fileTable.setHorizontalHeaderLabels(
                    ["Download?","iTag","Bit Rate", "Filesize"])
                for stream in self.vids:
                    rowPosition = self.fileTable.rowCount()
                    self.fileTable.insertRow(rowPosition)
                    chkBoxItem = QtWidgets.QTableWidgetItem()
                    chkBoxItem.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                    chkBoxItem.setCheckState(QtCore.Qt.Unchecked)
                    self.fileTable.setItem(rowPosition, 0, chkBoxItem)
                    self.fileTable.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(stream.itag))
                    self.fileTable.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(stream.abr))
                    self.fileTable.setItem(rowPosition, 3,
                                           QtWidgets.QTableWidgetItem(size(stream.filesize, system=verbose)))

            except:
                traceback.print_exc()

    def browsepressed(self):
        file = QtWidgets.QFileDialog.getExistingDirectoryUrl(None, "Select Download Directory")
        file = file.toString()
        file=file[8:]
        self.dlDirectory.setText(file)


    def downloadpressed(self):
        self.download.setEnabled(True)
        checked_list = []
        filename = self.filename.text()
        for i in range(self.fileTable.rowCount()):
            if self.fileTable.item(i, 0).checkState() == QtCore.Qt.Checked:
                checked_list.append(self.fileTable.item(i, 1).text().strip('iTag: '))
        self.consolewrite('Downloading Content\n')
        if self.fileType.currentText() == 'Video':
            try:
                self.threadpool = QtCore.QThreadPool()
                print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())
                if filename:
                    for i in checked_list:
                        p = DownloadFileThread(self.yt, int(i), self.tempdir, str(filename + ' - ' + self.yt.streams.get_by_itag(int(i)).resolution))
                        self.threadpool.start(p)
                    p = DownloadFileThread(self.yt, 251, self.tempdir, filename + ' - audio')
                    self.threadpool.start(p)
                else:
                    for i in checked_list:
                        p = DownloadFileThread(self.yt, int(i), self.tempdir,  str(self.yt.title + ' - ' + self.yt.streams.get_by_itag(int(i)).resolution))
                        self.threadpool.start(p)
                    p = DownloadFileThread(self.yt, 251, self.tempdir, self.yt.title + ' - audio')
                    self.threadpool.start(p)
            except:
                traceback.print_exc()
        elif self.fileType.currentText() == 'Audio':
            try:
                self.threadpool = QtCore.QThreadPool()
                print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())
                if filename:
                    for i in checked_list:
                        p = DownloadFileThread(self.yt, int(i), self.tempdir, str(filename + ' - ' + self.yt.streams.get_by_itag(int(i)).abr))
                        self.threadpool.start(p)
                else:
                    for i in checked_list:
                        p = DownloadFileThread(self.yt, int(i), self.tempdir,  str(self.yt.title + ' - ' + self.yt.streams.get_by_itag(int(i)).abr))
                        self.threadpool.start(p)
            except:
                traceback.print_exc()
        self.threadpool.waitForDone()
        self.threadpool = QtCore.QThreadPool()
        try:
            if self.fileType.currentText() == 'Video':
                if filename:
                    self.consolewrite('Converting Video\n')
                    for i in checked_list:
                        p = MergeAudioVideo(
                            self.tempdir + '\\' + filename + ' - audio.webm',
                            self.tempdir + '\\' + filename + ' - ' + self.yt.streams.get_by_itag(int(i)).abr + '.webm',
                            self.dlDirectory.text() + '\\' + filename + ' - ' + self.yt.streams.get_by_itag(int(i)).abr + '.mp4'
                        )
                        self.threadpool.start(p)
                else:
                    self.consolewrite('Converting Video\n')
                    for i in checked_list:
                        p = MergeAudioVideo(
                            self.tempdir + '\\' + self.yt.title + ' - audio.webm',
                            self.tempdir + '\\' + self.yt.title + ' - ' + self.yt.streams.get_by_itag(int(i)).resolution + '.webm',
                            self.dlDirectory.text() + '/' + self.yt.title + ' - ' + self.yt.streams.get_by_itag(int(i)).resolution + '.mp4',
                        )
                        self.threadpool.start(p)
            elif self.fileType.currentText() == 'Audio':
                if filename:
                    self.consolewrite('Converting Audio')
                    for i in checked_list:
                        p = ConvertAudio(
                            self.tempdir + '\\' + filename + ' - ' + self.yt.streams.get_by_itag(int(i)).abr + '.webm',
                            str(self.dlDirectory.text() + '/' + filename + ' - ' + str(self.yt.streams.get_by_itag(int(i)).abr) + '.mp3')
                        )
                        self.threadpool.start(p)
                else:
                    self.consolewrite('Converting Audio\n')
                    for i in checked_list:
                        p = ConvertAudio(
                            self.tempdir + '\\' + self.yt.title + ' - ' + self.yt.streams.get_by_itag(int(i)).abr + '.webm',
                            str(self.dlDirectory.text() + '/' + self.yt.name + ' - ' + str(self.yt.streams.get_by_itag(int(i)).abr) + '.mp3')
                        )
                        self.threadpool.start(p)
        except:
            traceback.print_exc()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    prog = YTConverter(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

