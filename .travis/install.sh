#!/bin/bash

if [[ $TRAVIS_OS_NAME == 'osx' ]]; then
    brew update
    brew outdates xctool || brew upgrade xctool
    brew install python36
    sudo pip3 install pyqt5 moviepy requests pytube imageio pyinstaller
else
    sudo apt get install python36
    sudo apt-get install python3-pyqt5
    sudo pip install requests pytube imageio pyinstaller
fi


