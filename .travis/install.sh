#!/bin/bash

if [[ $TRAVIS_OS_NAME == 'osx' ]]; then
    brew update
    brew outdates xctool || brew upgrade xctool
    brew install python
    pip3 install pyqt5 moviepy requests pytube imageio pyinstaller
else
    sudo apt-get install python3 python3-pip
    pip3 install requests pytube imageio pyinstaller pyqt5
fi


