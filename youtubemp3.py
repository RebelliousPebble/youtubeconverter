from pytube import YouTube
import os
import subprocess
from halo import Halo
from prettytable import PrettyTable
import tkinter as tk
from tkinter import filedialog as fd
from hurry.filesize import verbose
from hurry.filesize import size

filesize=None

convertspinner = Halo(text='Converting File', spinner='dots')

def setdir():
    print('Use dialogue to select a folder to download to.\n\n')
    root = tk.Tk()
    root.withdraw()
    root.update()
    directory = fd.askdirectory(parent=root)
    root.update()
    root.destroy()
    return directory



def downloadaudio():
    videourl = input("Enter video URL: \t")
    yt = YouTube(videourl)
    yt.register_on_progress_callback(show_progress_bar)
    vids = yt.streams.filter(only_audio=True).filter(subtype='webm').all()
    print(makeTable(vids, 1))

    vnum = int(input("Enter vid num: "))

    global filesize
    filesize = vids[vnum].filesize
    vids[vnum].download()
    

    default_filename = vids[vnum].default_filename


    new_filename = default_filename.strip('.webm')
    new_filename = new_filename + '.mp3'

    if os.path.exists(os.path.join('/Volumes/', directory, new_filename)):
        os.remove(os.path.join('/Volumes/', directory, new_filename))

    convertspinner.start()
    subprocess.run(['/Volumes/Data/Scripts/YoutubeConverter/ffmpeg', '-hide_banner', '-loglevel', 'error', '-i', os.path.join(default_filename), '-vn', '-ab', '320k', '-ar', '44100', '-f', 'mp3',               # or subprocess.run (Python 3.5+)
        os.path.join('/Volumes/', directory, new_filename)
    ])
    convertspinner.stop()
    
    os.remove(default_filename)

    choice = input('Convert another video to mp3 into same directory? Y/N:\t')
    if choice.upper() == 'Y':
        downloadaudio()
    

def downloadvideo():
    videourl = input("Enter video URL: \t")
    yt = YouTube(videourl)
    yt.register_on_progress_callback(show_progress_bar)
    vids = yt.streams.filter(only_video=True).filter(subtype='mp4').all()
    print(vids)
    print(makeTable(vids, 2))

    vnum = int(input("Enter vid num: "))

    global filesize
    filesize = vids[vnum].filesize
    vids[vnum].download(directory)
    

    choice = input('Convert another video to mp4 into same directory? Y/N:\t')
    if choice.upper() == 'Y':
        downloadvideo()

def menu():
    print('\n\nSelect an Option.\n1. Convert to MP3\n2. Convert to MP4\n3. Change Directory\n4. Exit')
    choice = int(input())
    if choice == 1:
        downloadaudio()
    elif choice == 2:
        downloadvideo()
    elif choice == 3:
        directory = setdir()
    elif choice == 4:
        exit()
    else:
        print('Make a valid choice')

def roundnum(x, base=5):
    return int(base * round(float(x)/base))


def show_progress_bar(stream, chunk, file_handle, bytes_remaining):
    downloaded=filesize-bytes_remaining
    downloadpercent = (downloaded/filesize) * 100
    baramount=(roundnum(downloadpercent))/5
    print(str(int(downloadpercent)) + '%  ' + str(downloaded) + '/' + str(filesize) + '   ' + '[' + ('='*(int(baramount))) + (' '*(20-(int(baramount)))) + ']', end='\r')
    
    
def makeTable(streamlist, type):
    table=PrettyTable()
    if type==1:
        table.field_names = ['Video Number', 'Bit Rate', 'Size']
        for i in range(len(streamlist)):
            vidnum = i
            brate = streamlist[i].abr
            dlsize = size(streamlist[i].filesize, system=verbose)
            table.add_row([vidnum, brate, dlsize])
        return table
    else:
        table.field_names = ['Video Number', 'Resolution', 'Frame Rate', 'Size']
        for i in range(len(streamlist)):
            vidnum = i
            res = str(streamlist[i].res)
            fps = streamlist[i].fps
            dlsize = size(streamlist[i].filesize, system=verbose)
            table.add_row([vidnum, res, fps, dlsize])
        return table



directory=setdir()
while True:
    try:
        menu()
    except KeyboardInterrupt:
        menu()
